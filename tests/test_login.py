from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from data.all_data import URLs
from data.locators import Locators
from utils.helpers import check_page


class TestLogin:

    def wait_for_element(self, driver, locator, timeout=3):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    def test_login_from_main_page(self, driver):
        driver.get(URLs.BASE_URL)

        login_button = self.wait_for_element(driver, Locators.LOGIN_ACCOUNT_BUTTON)
        login_button.click()

        check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)

    def test_login_from_personal_account_button(self, driver):
        driver.get(URLs.BASE_URL)

        personal_account_button = self.wait_for_element(driver, Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)

    def test_login_from_registration_form(self, driver):
        driver.get(URLs.REGISTRATION_PAGE)

        login_button_on_registration_page = self.wait_for_element(driver, Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE)
        login_button_on_registration_page.click()

        check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)

    def test_login_from_password_reset(self, driver):
        driver.get(URLs.LOGIN_PAGE)

        reset_password_button = self.wait_for_element(driver, Locators.RESET_PASSWORD_BUTTON)
        reset_password_button.click()

        check_page(driver, URLs.FORGOT_PASSWORD_PAGE, Locators.RESET_PASSWORD_TITLE)
