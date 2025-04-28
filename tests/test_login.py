from conftest import driver
from data.all_data import URLs
from data.locators import Locators
from utils.helpers import wait_for_element, check_page


def test_login_from_main_page(driver):
    driver.get(URLs.MAIN_PAGE)

    login_button = wait_for_element(driver, Locators.LOGIN_ACCOUNT_BUTTON)
    login_button.click()

    check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)


def test_login_from_personal_account_button(driver):
    driver.get(URLs.MAIN_PAGE)

    personal_account_button = wait_for_element(driver, Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account_button.click()

    check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)


def test_login_from_registration_form(driver):
    driver.get(URLs.REGISTRATION_PAGE)

    login_button_on_registration_page = wait_for_element(driver, Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE)
    login_button_on_registration_page.click()

    check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)


def test_login_from_password_reset(driver):
    driver.get(URLs.LOGIN_PAGE)

    reset_password_button = wait_for_element(driver, Locators.RESET_PASSWORD_BUTTON)
    reset_password_button.click()

    check_page(driver, URLs.FORGOT_PASSWORD_PAGE, Locators.RESET_PASSWORD_TITLE)
