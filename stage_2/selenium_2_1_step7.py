"""Задание: поиск сокровища с помощью get_attribute. https://stepik.org/lesson/165493/step/7?unit=140087."""  # noqa: RUF002

import time

from selenium.webdriver.common.by import By

from common import browser, calc

try:
    LINK = "http://suninjuly.github.io/get_attribute.html"

    browser.get(LINK)
    treasure_box = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    input_box = browser.find_element(By.CSS_SELECTOR, "input#answer")
    robot_check = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    robot_radio = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    treasure_value = treasure_box.get_attribute("valuex")
    RESULT = calc(treasure_value)
    input_box.send_keys(str(RESULT))
    robot_check.click()
    robot_radio.click()
    send_button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
