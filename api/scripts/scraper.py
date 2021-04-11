import json
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import datetime
from jobs.models import Job
from dateutil.tz import tzlocal


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


def remoteok():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
    page = requests.post('https://remoteok.io/remote-dev-jobs', headers=headers)
    page.raise_for_status()

    soup = BeautifulSoup(page.content, 'html.parser')
    trs = soup.find_all("tr", {"class": "job"})
    for tr in trs:
        roleh2 = tr.find("h2")
        role = roleh2.text
        direct_link = 'https://remoteok.io' + roleh2.parent['href']
        date = tr.find('time')['datetime']
        jobsite_link = 'https://remoteok.io/remote-dev-jobs'
        company = tr.find("h3").text
        h3tags = tr.find("td", {"class": "tags"})
        tags = []
        for tag in h3tags:
            tags.append(tag.find("h3").text)

        Job.objects.create(
            direct_link = direct_link,
            jobsite_link = jobsite_link,
            jobsite = 'remoteok.io',
            tags = tags,
            date = parse(date),
            company =company,
            role = role
        )


def weworkremotely():
    page = requests.get('https://weworkremotely.com/categories/remote-programming-jobs')
    soup = BeautifulSoup(page.content, 'html.parser')
    lis = soup.find_all("li", {"class": "feature"})
    for li in lis:
        try:
            timetag = li.findChild("time", recursive=True)
            if timetag:
                date = parse(timetag.get('datetime'))
            else:
                date = datetime.now(tzlocal())
            region_tags = li.find("span", {"class": "region"})
            if region_tags:
                tags = region_tags.text.split('/')
            else:
                tags = []
            company = li.find("span", {"class": "company"}).text
            role = li.find("span", {"class": "title"}).text
            Job.objects.create(
                direct_link = f"https://weworkremotely.com{li.find_all('a')[1].get('href')}",
                jobsite_link = 'https://weworkremotely.com/categories/remote-programming-jobs',
                jobsite = 'weworkremotely.com',
                tags = tags,
                date = date,
                company = company,
                role = role
            )
        except:
            pass

    return



def scraper():
    weworkremotely()
    grow_remote()
    remoteok()