"""Задание: кликаем по checkboxes и radiobuttons (капча для роботов) https://stepik.org/lesson/165493/step/5?unit=140087."""

import time
from selenium.webdriver.common.by import By
from common import browser, calc

try:
    LINK = "https://suninjuly.github.io/math.html"

    browser.get(LINK)
    value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    textinput = browser.find_element(By.CSS_SELECTOR, "#answer")
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    x = value.text
    Y = calc(x)

    textinput.send_keys(str(Y))
    checkbox.click()
    radio.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
