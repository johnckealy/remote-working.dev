# from celery import shared_task
from scripts.collect_jobs import run as run_collect_jobs
from celery.decorators import task



@task(name="query_jobsites")
def query_jobsites():
    message = run_collect_jobs()
    return message
