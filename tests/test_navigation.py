from selenium.webdriver.common.by import By
from conftest import driver
from data.all_data import URLs
from data.locators import Locators
from utils.helpers import wait_for_element, click_button, check_page


def test_navigation(driver):
    driver.get(URLs.LOGIN_PAGE)

    email_field = wait_for_element(driver, Locators.EMAIL_FIELD)
    email_field.send_keys('ulugbeksharipov20123@gmail.com')

    password_field = wait_for_element(driver, Locators.PASSWORD_FIELD)
    password_field.send_keys('ulugbeksharipov20123@gmail.com')

    click_button(driver, Locators.LOGIN_BUTTON)
    check_page(driver, URLs.MAIN_PAGE, Locators.MAIN_PAGE_TITLE)

    click_button(driver, Locators.PERSONAL_ACCOUNT_BUTTON)
    check_page(driver, URLs.PROFILE_PAGE, Locators.PROFILE_SECTION_TEXT)

    click_button(driver, Locators.CONSTRUCTOR_BUTTON)
    check_page(driver, URLs.MAIN_PAGE, Locators.MAIN_PAGE_TITLE)

    click_button(driver, Locators.TOPPINGS_BUTTON)
    assert driver.find_element(By.XPATH,
                               Locators.TOPPINGS_TITLE).is_displayed(), "Элемент не найден, прокрутка не произошла"

    click_button(driver, Locators.SAUCES_BUTTON)
    assert driver.find_element(By.XPATH,
                               Locators.SAUCES_TITLE).is_displayed(), "Элемент не найден, прокрутка не произошла"

    click_button(driver, Locators.BUNS_BUTTON)
    assert driver.find_element(By.XPATH,
                               Locators.BUNS_TITLE).is_displayed(), "Элемент не найден, прокрутка не произошла"

    click_button(driver, Locators.PERSONAL_ACCOUNT_BUTTON)

    click_button(driver, Locators.EXIT_BUTTON)
    check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)
