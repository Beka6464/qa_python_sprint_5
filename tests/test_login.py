from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from data.all_data import URLs
from data.locators import Locators


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(URLs.BASE_URL)

        login_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        login_button.click()

        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.current_url == URLs.LOGIN_PAGE, f'Неправильный URL после перехода, ожидался {URLs.LOGIN_PAGE}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Вход" не найден на странице'

    def test_login_from_personal_account_button(self, driver):
        driver.get(URLs.BASE_URL)

        personal_account_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()

        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.current_url == URLs.LOGIN_PAGE, f'Неправильный URL после перехода, ожидался {URLs.LOGIN_PAGE}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Вход" не найден на странице'

    def test_login_from_registration_form(self, driver):
        driver.get(URLs.REGISTRATION_PAGE)

        login_button_on_registration_page = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE))
        login_button_on_registration_page.click()

        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.current_url == URLs.LOGIN_PAGE, f'Неправильный URL после перехода, ожидался {URLs.LOGIN_PAGE}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Вход" не найден на странице'

    def test_login_from_password_reset(self, driver):
        driver.get(URLs.LOGIN_PAGE)

        reset_password_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.RESET_PASSWORD_BUTTON))
        reset_password_button.click()

        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.RESET_PASSWORD_TITLE))
        assert driver.current_url == URLs.FORGOT_PASSWORD_PAGE, f'Неправильный URL после перехода, ожидался {URLs.FORGOT_PASSWORD_PAGE}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Восстановление пароля" не найден на странице'
