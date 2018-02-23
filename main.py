from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from io import BytesIO
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from lxml import html
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *


def scraping(first_name="", last_name=""):

    url = "https://directory.fau.edu/"
    url = url + "dir/send_name?fn={}&ln={}".format(first_name, last_name)

    r = requests.post(url)
    html = r.content.decode()
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("ul.deptPhoneEmail")

    if table:

        try:
            # phone_num = soup.select_one("li:nth-of-type(5)").text.strip()
            phone_num = soup.select_one("i.fa-phone").parent.select_one("a").text.strip()
        except:
            phone_num = ""
        try:
            email = soup.select_one("i.fa-envelope").parent.select_one("a").text.strip()
        except:
            email = ""

    else:
        phone_num = ""
        email = ""

    print(phone_num)
    print(email)
    return [phone_num, email]

scraping(first_name="STEVEN", last_name="ABBOTT")
# scraping(first_name="ANTHONY", last_name="ABBATE")