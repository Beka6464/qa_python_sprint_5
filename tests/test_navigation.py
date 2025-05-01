from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from data.all_data import URLs, Data
from data.locators import Locators
from utils.helpers import click_button, check_page


class TestNavigation:
    def wait_for_element(self, driver, locator, timeout=3):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    def test_navigation(self, driver):
        driver.get(URLs.LOGIN_PAGE)

        email_field = self.wait_for_element(driver, Locators.EMAIL_FIELD)
        email_field.send_keys(Data.login)

        password_field = self.wait_for_element(driver, Locators.PASSWORD_FIELD)
        password_field.send_keys(Data.password)

        click_button(driver, Locators.LOGIN_BUTTON)
        check_page(driver, URLs.BASE_URL, Locators.MAIN_PAGE_TITLE)

        click_button(driver, Locators.PERSONAL_ACCOUNT_BUTTON)
        check_page(driver, URLs.PROFILE_PAGE, Locators.PROFILE_SECTION_TEXT)

        click_button(driver, Locators.CONSTRUCTOR_BUTTON)
        check_page(driver, URLs.BASE_URL, Locators.MAIN_PAGE_TITLE)

        click_button(driver, Locators.PERSONAL_ACCOUNT_BUTTON)

        click_button(driver, Locators.EXIT_BUTTON)
        check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)

    def test_constructor_navigation_to_buns(self, driver):
        driver.get(URLs.BASE_URL)
        # Пришлось инициировать клик на другой раздел, прежде чем нажимать на переход в раздел "Булок",
        # потому что я в этом разделе нахожусь по дефолту у меня не работает клик по нему
        click_button(driver, Locators.TOPPINGS_BUTTON)
        click_button(driver, Locators.BUNS_BUTTON)
        assert driver.find_element(By.XPATH,
                                   Locators.BUNS_ELEMENT).is_displayed(), "Элемент не найден, прокрутка не произошла"

    def test_constructor_navigation_to_sauces(self, driver):
        driver.get(URLs.BASE_URL)

        click_button(driver, Locators.SAUCES_BUTTON)
        assert driver.find_element(By.XPATH,
                                   Locators.SAUCES_ELEMENT).is_displayed(), "Элемент не найден, прокрутка не произошла"

    def test_constructor_navigation_to_toppings(self, driver):
        driver.get(URLs.BASE_URL)

        click_button(driver, Locators.TOPPINGS_BUTTON)
        assert driver.find_element(By.XPATH,
                                   Locators.TOPPINGS_ELEMENT).is_displayed(), "Элемент не найден, прокрутка не произошла"
