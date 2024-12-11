from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.files.base import ContentFile
from .jobs import TechnodomParser
from .models import *
import requests
import re
from urllib.parse import urlparse


logger = get_task_logger(__name__)\


def sync_data(data):
    shop, created = Shop.objects.get_or_create(name = "Technodom", defaults={'url': "https://www.technodom.kz/", 'rate': 1})
    print(created)
    product_data = data
    response = requests.get(product_data["image"])
    if response.status_code == 200:
        image_name = urlparse(product_data["image"]).path.split('/')[-1]
        image_content = ContentFile(response.content, name=image_name)
    else:
        image_content = None
    product = Product.objects.create(name = product_data["name"][:200], 
                                        cost = re.sub(r'[^\d.]', '', product_data["price"]), 
                                        image = image_content, 
                                        specs = product_data["specs"],
                                        is_present = True,
                                        )
    product.shops.add(shop)

@shared_task
def parse_technodom():
    parser = TechnodomParser()
    for data in parser.parse_outer_catalog():
        sync_data(data)
    return 1


@shared_task
def add(x, y):
    logger.info(x + y)
    print(x + y)
    return x + y

if __name__ == '__main__':
    parse_technodom()