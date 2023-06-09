import requests
from bs4 import BeautifulSoup
import schedule
import time


def update_resume(url, headers):
    page = requests.get(url, headers=headers).text
    html = BeautifulSoup(page, 'html.parser')
    button = html.select('div.applicant-resumes-card-wrapper div.applicant-resumes-action')[1].click()


def start_update():
    url = 'https://spb.hh.ru/applicant/resumes'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Cookie': '__ddg1_=Q4ynGvgpVjulQHBO8jIY; _xsrf=73c3ef5866b77f4336a8c7641cb605c2; regions=2; region_clarified=NOT_SET; display=desktop; crypted_hhuid=8C0CED5D405374D74711DAD8F598BA6AE9BE52454AC34915F60FC1F70716E54D; hhtoken=UZHFJVZFDf0lFKRmOZfUrwUO01UJ; hhuid=fhXpbDhqyzksd2Pj1BIo8A--; GMT=3; tmr_lvid=5da0fff5c7c3e22e6adbb65237076b24; tmr_lvidTS=1675875348253; _ym_uid=1675875348604633338; _ym_d=1675875348; iap.uid=bcb6eb75d9a94b118f42aced9c9ff0ce; hhul=9ac6e27e6c29d9af6c0f2e1445b0b55003dfec3e394f971d67e8fb867513af27; redirect_host=spb.hh.ru; hhrole=applicant; crypted_id=A545F3AC14383E09F32AA85D00C0AE5AA5471C6F722104504734B32F0D03E9F8; _hi=107024088; total_searches=2; _ga=GA1.2.1639627682.1675875348; _ga_44H5WGZ123=GS1.1.1679851010.41.0.1679851010.60.0.0; _ym_isad=1; tmr_detect=1%7C1679911473210; __zzatgib-w-hh=MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS90c3tdbR9RY3wTVUoRUjdbHhc1cipVDjxdPUMqdiw/HyNoSV9QRBILayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXIsWAgMX0RGcnMsN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LEndyI1ELC2NFM2llaXA'
    }
    schedule.every(4).hours.do(update_resume(url, headers))
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    start_update()