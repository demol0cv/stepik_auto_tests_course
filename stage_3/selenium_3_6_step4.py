import math
import os
import time

import pytest
from dotenv import load_dotenv
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_user(descr: str = None):  # noqa: ARG001, RUF013
    pass #input(f"{descr if descr is not None else ""}Для продолжения нажми Enter...")

def setup_module()->None:
    logger.debug("Инициализация .env")
    load_dotenv()

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()

LINK = "https://stepik.org/lesson/236895/step/1"
LINKS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

@pytest.mark.parametrize("link", LINKS)
def test_stepik_login(browser, link):
    browser.get(link)

    # кликаем по ссылке Войти
    login_link = WebDriverWait(browser, timeout=10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button"),
            ),
        )
    login_link.click()

    # Вводим логин и пароль
    WebDriverWait(browser, timeout=3).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,"input#id_login_email"),
            ),
    )
    login_field = browser.find_element(By.CSS_SELECTOR, "input#id_login_email")
    pwd_field = browser.find_element(By.CSS_SELECTOR, "input#id_login_password")
    login_field.send_keys(os.getenv("STEPIK_LOGIN"))
    pwd_field.send_keys(os.getenv("STEPIK_PASSWORD"))

    # Авторизуемся
    btn_login = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader")
    btn_login.click()
    answer = math.log(int(time.time()))

    # Ждём появления кнопки отправки решения
    WebDriverWait(browser, timeout=15).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,"button.submit-submission"),
            ),
        )

    textarea = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area.ember-view.textarea")
    textarea.send_keys(str(answer))

    # Ждём, когда кнопка отправки решения потеряет атрибут disabled
    WebDriverWait(browser, timeout=5).until_not(
        EC.element_attribute_to_include((By.CSS_SELECTOR, "button.submit-submission"), "disabled"),
    )

    button_send = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    if button_send is bool:
        pytest.fail("Ошибка при поиске кнопки")

    # Отправляем решение
    button_send.click()

    # Ждём появления элемента с результатом решения
    WebDriverWait(browser, timeout=20, poll_frequency=.3).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.smart-hints.ember-view.lesson__hint>p.smart-hints__hint"),
            ),
    )

    result = browser.find_element(By.CSS_SELECTOR, "div.smart-hints.ember-view.lesson__hint>p.smart-hints__hint")
    result = result.text

    logger.debug(result)
    assert result == "Correct!"


if __name__ == "__main__":
    pass #test_stepik_login('aasd',"https://stepik.org/lesson/236895/step/1")
