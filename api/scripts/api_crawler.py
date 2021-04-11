import requests
from jobs.models import Job
from dateutil.parser import parse
from .selenium_service import SeleniumScrape

def remoteimpact():
    page = requests.get('https://remoteimpact-api.vercel.app/api?page=1&limit=100')
    jobs = page.json()
    for job in jobs:
        Job.objects.create(
            direct_link = job['link'],
            jobsite_link = 'https://www.remoteimpact.io',
            jobsite = 'remoteimpact.io',
            tags = job['tags'],
            date = parse(job['date']),
            company = job['company'],
            role = job['role']
        )

def linkedin():
    url = 'https://www.linkedin.com/jobs/search?keywords=Full%2BStack&location=remote&trk=public_jobs_jobs-search-bar_search-submit&f_E=2&position=1&pageNum=0'
    linkedin = SeleniumScrape(url)
    jobs_list = linkedin.get_linkedin_jobs()
    pass

def crawler():
    remoteimpact()