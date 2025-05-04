from selenium.webdriver.common.by import By


class Locators():
    # поле для ввода имени
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # поле для ввода email
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # поле для ввода пароля
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    # кнопка Войти
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")
    # кнопка Зарегистрироваться
    REGISTRATION_BUTTON = (By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]")
    # Текст Вход на странице логина
    LOGIN_TITLE = (By.XPATH, "//*[text()='Вход']")
    # Сообщение об ошибке неправильного пароля
    PASSWORD_ERROR = (By.XPATH, "//*[text()='Некорректный пароль']")
    # Кнопка "Войти в аккаунт"
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(@class, 'button_button__33qZ0 ') and text()='Войти в аккаунт']")
    # Кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "// *[contains( @class , 'AppHeader_header__link__3D_hX')] // p[text()='Личный Кабинет']")
    # Кнопка “Войти” на странице регистрации
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, "//*[@class='Auth_link__1fOlj' and text()='Войти']")
    # Кнопка "Восстановить пароль" на странице логин
    RESET_PASSWORD_BUTTON = (By.XPATH, "//*[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    # Заголовок "Восстановление пароля" на странице с end-point'ом "/forgot-password"
    RESET_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # Заголовок "Соберите бургер" на главной странице
    MAIN_PAGE_TITLE = (By.XPATH, "//*[contains(text(), 'Соберите бургер')]")
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "// *[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    # Информационный текст внизу на странице профиля
    PROFILE_SECTION_TEXT = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")
    # Кнопка "Булки" на главной странице
    BUNS_BUTTON = (By.XPATH, "//*[ @class ='text text_type_main-default' and text()='Булки']")
    # Кнопка "Соусы" на главной странице
    SAUCES_BUTTON = (By.XPATH, "//*[ @class ='text text_type_main-default' and text()='Соусы']")
    # Кнопка "Начинки" на главной странице
    TOPPINGS_BUTTON = (By.XPATH, "//*[ @class ='text text_type_main-default' and text()='Начинки']")
    # Первый элемент в категории "Булки"
    BUNS_ELEMENT = "//a[contains(@href, '61c0c5a71d1f82001bdaaa6d') and @draggable='true']"
    # Первый элемент в категории "Соусы"
    SAUCES_ELEMENT = "//a[contains(@href, '61c0c5a71d1f82001bdaaa72') and @draggable='true']"
    # Первый элемент в категории "Начинки"
    TOPPINGS_ELEMENT = "//a[contains(@href, '61c0c5a71d1f82001bdaaa6f') and @draggable='true']"
    # Кнопка "Выход" в профиле
    EXIT_BUTTON = (By.XPATH, "//*[@class='Account_listItem__35dAP']//button[text()='Выход']")
