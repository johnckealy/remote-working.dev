from jobs.models import Job
from utils import L, LOG
from .scraper import scraper
from .api_crawler import crawler
from datetime import datetime, timedelta
from dateutil.tz import tzlocal


def run():
    LOG.info(f"\n{L.SUCCESS} Cleaning all job entries...{L.ENDC}")
    Job.objects.all().delete()
    LOG.info(f"{L.SUCCESS} Running the API crawler...{L.ENDC}")
    crawler()
    LOG.info(f"{L.SUCCESS} Running the scraper...{L.ENDC}\n")
    scraper()

    earliest_job =datetime.now(tzlocal()) - timedelta(days=45)
    Job.objects.filter(date__lt=earliest_job).delete()
    LOG.info(f"{L.SUCCESS} Done{L.ENDC}\n")

