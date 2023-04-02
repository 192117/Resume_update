import requests
from bs4 import BeautifulSoup
import schedule
import time


URL = 'https://spb.hh.ru/applicant/resumes'

headers = {
        'User-Agent': '',
        'Cookie': ''
    }

def update_resume():
    page = requests.get(URL, headers=headers).text
    html = BeautifulSoup(page, 'html.parser')
    buttons = html.select('div.applicant-resumes-card-wrapper div.applicant-resumes-card div.applicant-resumes-recommendations-button')
    for button in buttons:
        click = button.find('button', {'data-qa': 'resume-update-button_actions'})
        if click:
            click.click()

# Обновляем резюме каждые 4 часа
schedule.every(4).hours.do(update_resume)

# Запускаем бесконечный цикл для выполнения заданий по расписанию
while True:
    schedule.run_pending()
    time.sleep(60)