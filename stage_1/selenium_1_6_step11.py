"""
Уникальность селекторов: часть 2

https://stepik.org/lesson/138920/step/10?unit=196194
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Firefox()
    #time.sleep()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.form-group.first_class>input.form-control.first")
    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.form-group.second_class>input.form-control.second")
    email = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.form-group.third_class>input.form-control.third")

    first_name.send_keys("Mikhail")
    last_name.send_keys("Gogberashvili")
    email.send_keys("example@example.com")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
