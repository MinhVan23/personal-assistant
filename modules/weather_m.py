import sys

import requests
from bs4 import BeautifulSoup

def weather_scrape():
    url='https://e.vnexpress.net/weather/tp-hcm'
    web_data=requests.get(url)
    html=web_data.text
    soup=BeautifulSoup(html, 'html.parser')
    print(soup.find('div', class_="name"))
    sys.exit(0)

def fetch_weather():
    weather_status=weather_scrape()
    return weather_status