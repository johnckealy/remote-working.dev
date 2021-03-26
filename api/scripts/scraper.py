import json
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from jobs.models import Job


def grow_remote():
    page = requests.get('https://jobs.growremote.ie/software-development-jobs')
    soup = BeautifulSoup(page.content, 'html.parser')
    jsonstr = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(jsonstr.contents[0])
    jobs = data['props']['pageProps']['jobs']

    for job in jobs:
        fields = job['fields']
        tags = fields['tags_strings'] if 'tags_strings' in fields.keys() else []
        if fields['companyUrl'][0:4] != 'http':
            fields['companyUrl'] = f"http://{fields['companyUrl']}"
        if fields['jobCategory'] == 'Software Development':
            Job.objects.create(
                direct_link = fields['companyUrl'],
                jobsite_link = 'https://jobs.growremote.ie/software-development-jobs',
                jobsite = 'growremote.ie',
                tags = tags,
                date = parse(fields['datePosted']),
                company = fields['companyName'],
                role = fields['jobTitle']
            )

def scraper():
    grow_remote()