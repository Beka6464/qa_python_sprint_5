from data.all_data import URLs
from data.locators import Locators
from utils.helpers import generate_data, validate_email, wait_for_element, click_button, check_page
from conftest import driver


def test_registration(driver):
    driver.get(URLs.REGISTRATION_PAGE)
    name, email, password, wrong_password = generate_data()

    assert name != '', 'Поле "Имя" не может быть пустым'
    assert validate_email(email), f'Ввели Email: {email} не в корректном формате'
    assert len(password) > 6

    name_field = wait_for_element(driver, Locators.NAME_FIELD)
    name_field.send_keys(name)

    email_field = wait_for_element(driver, Locators.EMAIL_FIELD)
    email_field.send_keys(email)

    password_field = wait_for_element(driver, Locators.PASSWORD_FIELD)
    password_field.send_keys(wrong_password)

    click_button(driver, Locators.REGISTRATION_BUTTON)

    error_message = wait_for_element(driver, Locators.PASSWORD_ERROR)
    assert error_message.is_displayed(), 'Сообщение о неверном пароле не отобразилось'

    driver.execute_script("arguments[0].value = '';", password_field)

    assert password_field.get_attribute("value") == '', 'Password field is not empty!'

    password_field.send_keys(password)
    click_button(driver, Locators.REGISTRATION_BUTTON)
    check_page(driver, URLs.LOGIN_PAGE, Locators.LOGIN_TITLE)
