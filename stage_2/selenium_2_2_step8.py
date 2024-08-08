"""Задание: работа с выпадающим списком https://stepik.org/lesson/228249/step/3?unit=200781."""  # noqa: RUF002

import sys
import time
from pathlib import Path

from loguru import logger
from selenium.webdriver.common.by import By

from common import browser

try:
    LINK = "http://suninjuly.github.io/file_input.html"

    browser.get(LINK)
    field_firstname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    field_lastname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    field_email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    file_to_upload = Path(Path.cwd()) / "for_upload.txt"
    logger.debug(file_to_upload)
    input_file = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')

    field_firstname.send_keys("Jena")
    field_lastname.send_keys("Ziemann")
    field_email.send_keys("Caroline_Cummerata@gmail.com")
    input_file.send_keys(str(file_to_upload))
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()




except Exception as e:
    logger.debug(e)
    sys.exit(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
