import random
import re
import string

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


def generate_data():
    name = f'ulugbek_sharipov{random.randint(1000, 9999)}'
    email = f'ulugbek_sharipov_20_{random.randint(1000, 9999)}@yandex.ru'
    password = f'password{random.randint(100, 999)}'
    wrong_password = f'{random.randint(10, 99)}{''.join(random.choices(string.ascii_lowercase, k=3))}'

    return name, email, password, wrong_password


def validate_email(email):
    pattern = r"^[a-zA-Z0-9_]+_[a-zA-Z0-9_]+_\d{2}_\d{4}@yandex\.ru$"
    return bool(re.match(pattern, email))


def wait_for_element(driver, locator, timeout=3):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


def click_button(driver, locator, timeout=3):
    return WebDriverWait(driver, timeout).until(element_to_be_clickable(locator)).click()


def check_page(driver, expected_url, title_locator, timeout=3):
    title = wait_for_element(driver, title_locator)

    assert driver.current_url == expected_url, f'Неправильный URL после перехода, ожидался {expected_url}, но был {driver.current_url}'
    assert title.is_displayed(), 'Заголовок "Вход" не найден на странице'
