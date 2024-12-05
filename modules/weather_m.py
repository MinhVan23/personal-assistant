import sys

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def weather_scrape():
    url='https://e.vnexpress.net/weather/tp-hcm'
    service=Service(ChromeDriverManager().install())
    options=Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    driver=webdriver.Chrome(service=service, options=options)
    driver.get(url)
    element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="name"]')))
    weather_status=element.text.lower()
    driver.quit()
    return weather_status

def fetch_weather():
    weather_status=weather_scrape()
    return weather_status