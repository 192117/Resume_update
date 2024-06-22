from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def selenium_driver() -> webdriver:
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')
    service = Service()  # /usr/local/bin/chromedriver путь к драйверу
    driver = webdriver.Chrome(service=service, options=options)
    return driver
