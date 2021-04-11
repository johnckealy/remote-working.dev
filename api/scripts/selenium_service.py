
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime

# Create your tests here.
class SeleniumScrape:

    def __init__(self, url):
        options = Options()
        self.base_url = url
        options.add_argument("user-data-dir=selenium")
        options.binary_location = '/usr/bin/brave-browser'
        # options.headless = True
        options.add_argument('ignore-certificate-errors')
        self.selenium = webdriver.Chrome(options=options)

    def get_linkedin_jobs(self):
        self.selenium.get(self.base_url)
        jobs = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "li")))

        jobs_list = []
        for job in jobs:
            direct_link = job.find_element_by_tag_name('a').get_attribute('href')
            role = job.find_element_by_tag_name('h3').text
            company = job.find_element_by_tag_name('h4').text
            post_date = job.find_element_by_tag_name('time').get_attribute('datetime')
            post_date = datetime.strptime(post_date, '%Y-%m-%d')

            jobs_list.append({
                "direct_link": direct_link,
                "company": company,
                "role": role,
                "direct_link": direct_link,
                "post_date": post_date
            })
        return jobs_list



if __name__=="__main__":

    url = 'https://www.linkedin.com/jobs/search?keywords=Full%2BStack&location=remote&trk=public_jobs_jobs-search-bar_search-submit&f_E=2&position=1&pageNum=0'
    linkedin = SeleniumScrape(url)
    jobs_list = linkedin.get_linkedin_jobs()