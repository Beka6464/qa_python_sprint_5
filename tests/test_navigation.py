from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from data.all_data import URLs, Data
from data.locators import Locators
from utils.helpers import click_button


class TestNavigation:

    def test_navigation(self, driver):
        driver.get(URLs.LOGIN_PAGE)

        email_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.EMAIL_FIELD))
        email_field.send_keys(Data.login)

        password_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PASSWORD_FIELD))
        password_field.send_keys(Data.password)

        click_button(driver, Locators.LOGIN_BUTTON)

        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_TITLE))
        assert driver.current_url == URLs.BASE_URL, f'Неправильный URL после перехода, ожидался {URLs.BASE_URL}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Соберите бургер" не найден на странице'

        click_button(driver, Locators.PERSONAL_ACCOUNT_BUTTON)
        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PROFILE_SECTION_TEXT))
        assert driver.current_url == URLs.PROFILE_PAGE, f'Неправильный URL после перехода, ожидался {URLs.PROFILE_PAGE}, но был {driver.current_url}'
        assert title.is_displayed(), 'Искомый текст с описанием раздела не найден на странице'

        click_button(driver, Locators.CONSTRUCTOR_BUTTON)
        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAIN_PAGE_TITLE))
        assert driver.current_url == URLs.BASE_URL, f'Неправильный URL после перехода, ожидался {URLs.BASE_URL}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Соберите бургер" не найден на странице'

        click_button(driver, Locators.PERSONAL_ACCOUNT_BUTTON)

        click_button(driver, Locators.EXIT_BUTTON)
        title = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_TITLE))
        assert driver.current_url == URLs.LOGIN_PAGE, f'Неправильный URL после перехода, ожидался {URLs.LOGIN_PAGE}, но был {driver.current_url}'
        assert title.is_displayed(), 'Заголовок "Вход" не найден на странице'

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

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TOPPINGS_ELEMENT))

        assert driver.find_element(By.XPATH,
                                   Locators.TOPPINGS_ELEMENT).is_displayed(), "Элемент не найден, прокрутка не произошла"

