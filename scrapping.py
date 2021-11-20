import requests
from bs4 import BeautifulSoup

page=requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
#All conttents of title, company and locations
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
#However we need the specific job related to python
#I tried this but it gave me I expected value which is empty list
python_jobs = results.find_all("h2", string="Python")
print(python_jobs)#gives empty list rather than we expected
#But this is the solution for the above empty list problem
python_jobs=results.find_all("h2",string=lambda text: 'python' in text.lower() )
for python_job in python_jobs:
    print(python_job.text.strip()) #this code gives the expected values for the jobs related to python
