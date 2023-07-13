import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def update_resume(url: str):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')
    service = Service(executable_path="path") # /usr/local/bin/chromedriver

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        email_input = driver.find_element(By.NAME, 'login')
        phone = input('Введите номер телефона ')
        email_input.send_keys(phone)
        email_input.send_keys(Keys.RETURN)
        code = input('Введите код ')
        code_input = driver.find_element(By.XPATH, '//input[@type="number"]')
        code_input.send_keys(code)
        code_input.send_keys(Keys.RETURN)
        while True:
            time.sleep(10)
            driver.refresh()
            update_button = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button_actions"]')
            time.sleep(10)
            if update_button.text == 'Поднять в поиске':
                update_button.click()
                requests.get(
                    f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL}&text=Поднял резюме!'
                )
                time.sleep(4 * 60 * 60)
            else:
                time.sleep(60)
    except Exception as exception:
        requests.get(
            f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL}&text={exception}'
        )
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    update_resume("https://spb.hh.ru/applicant/resumes")
