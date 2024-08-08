"""
Задание: поиск элемента по XPath

https://stepik.org/lesson/138920/step/8?unit=196194
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


import time 

LINK = "http://suninjuly.github.io/find_xpath_form"

try:
   
    browser = webdriver.Firefox()
    browser.get(LINK)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")

    
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