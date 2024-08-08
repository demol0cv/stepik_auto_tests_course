"""
Задание: использование метода find_elements

https://stepik.org/lesson/138920/step/7?unit=196194
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "http://suninjuly.github.io/huge_form.html"

try:

    browser = webdriver.Firefox()
    browser.get(LINK)
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys("Мой ответ")

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
