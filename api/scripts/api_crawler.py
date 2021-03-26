import requests
from jobs.models import Job
from dateutil.parser import parse


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



def crawler():
    remoteimpact()