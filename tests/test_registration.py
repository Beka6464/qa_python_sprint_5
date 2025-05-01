from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.all_data import URLs
from data.locators import Locators
from utils.helpers import generate_data, click_button, check_page
from conftest import driver


class TestRegistration():

    def wait_for_element(self, driver, locator, timeout=3):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    def test_registration(self, driver):
        driver.get(URLs.REGISTRATION_PAGE)
        name, email, password, _ = generate_data()

        name_field = self.wait_for_element(driver, Locators.NAME_FIELD)
        name_field.send_keys(name)

        email_field = self.wait_for_element(driver, Locators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.wait_for_element(driver, Locators.PASSWORD_FIELD)

        password_field.send_keys(password)
        click_button(driver, Locators.REGISTRATION_BUTTON)
        check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)

    def test_registration_with_wrong_password(self, driver):
        driver.get(URLs.REGISTRATION_PAGE)
        name, email, password, wrong_password = generate_data()

        name_field = self.wait_for_element(driver, Locators.NAME_FIELD)
        name_field.send_keys(name)

        email_field = self.wait_for_element(driver, Locators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.wait_for_element(driver, Locators.PASSWORD_FIELD)
        password_field.send_keys(wrong_password)

        click_button(driver, Locators.REGISTRATION_BUTTON)

        error_message = self.wait_for_element(driver, Locators.PASSWORD_ERROR)
        assert error_message.is_displayed(), 'Сообщение о неверном пароле не отобразилось'
