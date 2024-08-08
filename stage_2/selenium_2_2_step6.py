"""Задание: работа с выпадающим списком https://stepik.org/lesson/228249/step/3?unit=200781."""  # noqa: RUF002

import time

from loguru import logger
from selenium.webdriver.common.by import By

from common import browser, calc

try:
    LINK = "http://suninjuly.github.io/execute_script.html"

    browser.get(LINK)
    value_x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    text_field = browser.find_element(By.CSS_SELECTOR, "input#answer")
    robot_check = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    robot_radio = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(calc(value_x))
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)
    robot_check.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()




except Exception as e:
    logger.debug(e)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
