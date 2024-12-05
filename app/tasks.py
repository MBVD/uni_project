from celery import shared_task
from celery.utils.log import get_task_logger
from .jobs.thd_parse import *


logger = get_task_logger(__name__)\


@shared_task
def parse_technodom():
    parser = TechnodomParser()
    parser.parse_outer_catalog()
    parsed_data = parser.product_data_list 
    return 1

@shared_task
def add(x, y):
    logger.info(x + y)
    print(x + y)
    return x + y