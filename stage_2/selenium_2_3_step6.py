"""Переход на новую вкладку браузера https://stepik.org/lesson/184253/step/5?unit=158843."""

import sys
import time

from loguru import logger
from selenium.webdriver.common.by import By

from common import browser, calc

try:
    LINK = "http://suninjuly.github.io/redirect_accept.html"

    browser.get(LINK)
    first_button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    first_button.click()

    browser.switch_to.window(browser.window_handles[1])

    time.sleep(.5)
    num_value = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    result = calc(num_value)

    field_result = browser.find_element(By.CSS_SELECTOR, "input#answer")
    field_result.send_keys(result)

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
