from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.all_data import URLs
from data.locators import Locators
from utils.helpers import generate_data, click_button
from conftest import driver


class TestRegistration():

    def test_registration(self, driver):
        driver.get(URLs.REGISTRATION_PAGE)
        name, email, password, _ = generate_data()

        name_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.NAME_FIELD))
        name_field.send_keys(name)

        email_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.EMAIL_FIELD))
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PASSWORD_FIELD))
        password_field.send_keys(password)

        click_button(driver, Locators.REGISTRATION_BUTTON)
        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.current_url == URLs.LOGIN_PAGE, f'Неправильный URL после перехода, ожидался {URLs.LOGIN_PAGE}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Вход" не найден на странице'

    def test_registration_with_wrong_password(self, driver):
        driver.get(URLs.REGISTRATION_PAGE)
        name, email, password, wrong_password = generate_data()

        name_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.NAME_FIELD))
        name_field.send_keys(name)

        email_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.EMAIL_FIELD))
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PASSWORD_FIELD))
        password_field.send_keys(wrong_password)

        click_button(driver, Locators.REGISTRATION_BUTTON)

        error_message = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PASSWORD_ERROR))
        assert error_message.is_displayed(), 'Сообщение о неверном пароле не отобразилось'
