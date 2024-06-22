import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException, TimeoutException, WebDriverException
from src.client import tg_send_message
from src.selenium_helper import selenium_driver
from src.settings import Settings
from src.exceptions import InvalidTokenError, TelegramConnectionError, SendMessageError


def update_resume():
    """Функция для поднятия резюме."""

    settings = Settings()
    driver = selenium_driver()
    try:
        driver.get(settings.hh_url)
        email_input = driver.find_element(By.NAME, 'login')
        phone = input('Введите номер телефона ')
        email_input.send_keys(phone)
        email_input.send_keys(Keys.RETURN)
        code = input('Введите код ')
        code_input = driver.find_element(By.XPATH, '//input[@type="number"]')
        code_input.send_keys(code)
        code_input.send_keys(Keys.RETURN)
        while True:
            try:
                time.sleep(5)
                driver.refresh()
                update_button = driver.find_element(By.XPATH, '//button[@data-qa="resume-update-button_actions"]')
                time.sleep(10)
                if update_button.text == 'Поднять в поиске':
                    update_button.click()
                    tg_send_message(settings.tg_bot_token, settings.tg_user_id, 'Поднял резюме')
                    time.sleep(4 * 60 * 60)
                else:
                    time.sleep(60)
            except (InvalidTokenError, TelegramConnectionError, SendMessageError) as exc:
                print(exc)
                break
            except (NoSuchElementException, TimeoutException, WebDriverException) as exc:
                tg_send_message(settings.tg_bot_token, settings.tg_user_id, str(exc))
                break
    except Exception as exc:
        print(exc)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    update_resume()
