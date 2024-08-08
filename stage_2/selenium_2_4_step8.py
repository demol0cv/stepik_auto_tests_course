"""Переход на новую вкладку браузера https://stepik.org/lesson/184253/step/5?unit=158843."""

import time  # noqa: I001

from loguru import logger

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common import browser, calc


try:
    LINK = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(LINK)

    cost_value = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"),
    )


    button = browser.find_element(By.ID, "book")
    button.click()

    text_value = WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.ID, "input_value")),
    ).text

    result = calc(text_value)
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(result)
    send_button = browser.find_element(By.ID, "solve")
    send_button.click()

except Exception as e:
    logger.debug(e)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
