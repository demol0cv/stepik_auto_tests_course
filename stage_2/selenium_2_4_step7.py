"""Переход на новую вкладку браузера https://stepik.org/lesson/184253/step/5?unit=158843."""

import time

from loguru import logger
from selenium.webdriver.common.by import By

from common import browser

try:
    LINK = "http://suninjuly.github.io/wait1.html"
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait2.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

except Exception as e:
    logger.debug(e)
    browser.quit()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
