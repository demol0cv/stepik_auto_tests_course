import time
import unittest
from venv import logger

from selenium import webdriver
from selenium.webdriver.common.by import By




class TestRegistrations(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Firefox()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        email = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")

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

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Не удалось зарегистрироваться",
            )
        browser.close()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Firefox()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        email = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")

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
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Не удалось зарегистрироваться",
            )
        browser.close()

if __name__ == "__main__":
    unittest.main()
