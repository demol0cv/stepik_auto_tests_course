"""
https://stepik.org/lesson/138920/step/5?unit=196194
"""

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "http://suninjuly.github.io/find_link_text"

try:

    browser = webdriver.Firefox()

    browser.get(LINK)
    TEXT = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    url = browser.find_element(By.XPATH, f'//a[text()="{TEXT}"]')
    url.click()
    time.sleep(2)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
except Exception as e:
    print(e)
    exit(1)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
