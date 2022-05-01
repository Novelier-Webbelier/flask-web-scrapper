import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination_li_list = soup.find("div", { "class": "pagination" }).find("ul", { "class": "pagination-list" }).find_all("li")

    links = []

    for page_item in pagination_li_list:
        a_tag = page_item.find("a")

        if a_tag != -1 and a_tag != None:
            content = a_tag.string

            if content != None:
                links.append(content)

        elif a_tag == None:
            content = page_item.string
            links.append(content)

    max_page = int(links[-1])

    return max_page

def extract_job(html):
    job_obj = {}
    job = html.select_one("div:nth-child(1)")
    company = html.select_one("div:nth-child(2)")

    job_name = job.find("h2").find("span", { "class" : None }).string

    try:
        job_id = job.find("h2").find("a")["data-jk"]
    except:
        job_id = -1

    company_name = company.find("span", { "class": "companyName" }).string
    company_location = company.find("div", { "class": "companyLocation" }).string

    job_obj["job_name"] = job_name
    job_obj["company_name"] = company_name
    job_obj["company_location"] = company_location
    job_obj["link"] = f"https://kr.indeed.com/viewjob?jk={job_id}"

    return job_obj

def extract_jobs(last_page, url):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        result_contents = soup.find_all("td", { "class": "resultContent" })
        print(f"Scrapping Indeed page {page+1}")

        for result_content in result_contents:
            job = extract_job(result_content)
            jobs.append(extract_job(result_content))

    return jobs

def get_jobs(word):
    url = f'https://kr.indeed.com/jobs?q={word}&limit=50&radius=100&start={LIMIT}'
    last_page = get_last_page(url)
    job = extract_jobs(last_page, url)

    return job
