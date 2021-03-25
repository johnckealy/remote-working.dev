import requests
from jobs.models import Job



def remoteimpact():
    Job.objects.all().delete()
    url = 'https://remoteimpact-api.vercel.app/api?page=1&limit=50'
    page = requests.get('https://remoteimpact-api.vercel.app/api?page=1&limit=50')
    jobs = page.json()
    for job in jobs:
        Job.objects.create(
            direct_link = job['link'],
            jobsite_link = 'https://www.remoteimpact.io',
            jobsite = 'remoteimpact.io',
            tags = job['tags'],
            date = job['date'],
            company = job['company'],
            role = job['role']
        )



def run():
    remoteimpact()