"""Задание: работа с выпадающим списком https://stepik.org/lesson/228249/step/3?unit=200781."""  # noqa: RUF002

import time
from venv import logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from common import browser

try:
    LINK = "https://suninjuly.github.io/selects1.html"

    browser.get(LINK)
    num1 = browser.find_element(By.CSS_SELECTOR, "span#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "span#num2").text
    selector = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")

    logger.debug(num1, num2)
    result = int(num1) + int(num2)
    selector.select_by_value(str(result))
    submit.click()




except Exception as e:
    logger.debug(e)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
