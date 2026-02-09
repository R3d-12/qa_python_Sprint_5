from selenium.webdriver.common.by import By

class Locators:
    """
    Класс с локаторами для автотестов Stellar Burgers.
    Каждый блок соответствует функциональному разделу приложения.
    """

    # === РЕГИСТРАЦИЯ ===
    REGISTRATION_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Ссылка для перехода к форме регистрации
    NAME_INPUT_REG = (By.XPATH, "//input[@name='name' and ./parent::div[contains(@class, 'input')]]")  # Поле «Имя» в форме регистрации
    EMAIL_INPUT_REG = (By.XPATH, "//div[contains(@class, 'input') and .//label[text()='Email']]//input[@name='name']")  # Поле «Email» в форме регистрации
    PASSWORD_INPUT_REG = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password' and ./parent::div[contains(@class, 'input')]]")  # Поле «Пароль» в форме регистрации
    SUBMIT_REG_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")  # Кнопка отправки формы регистрации
    ERROR_PASSWORD_MESSAGE = (By.CSS_SELECTOR, ".input__error.text_type_main-default")  # Сообщение об ошибке для некорректного пароля


    # === ВХОД / АВТОРИЗАЦИЯ ===
    LOGIN_TO_ACCOUNT_BTN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    ACCOUNT_LINK = (By.LINK_TEXT, "Личный Кабинет")  # Ссылка «Личный кабинет» на главной
    LOGIN_LINK_IN_FORM = (By.XPATH, "//a[normalize-space()='Войти']")  # Ссылка «Войти» в форме регистрации
    RECOVERY_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Ссылка «Войти» в форме восстановления пароля
    AUTHORIZATION_SUBMIT_BTN = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")  # Кнопка «Войти» в форме авторизации
    EMAIL_INPUT_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_text') and .//label[normalize-space()='Email']]//input")  # Поле «Email» в форме входа
    PASSWORD_INPUT_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_password')]//input[@type='password']")  # Поле «Пароль» в форме входа


    # === ЛИЧНЫЙ КАБИНЕТ И НАВИГАЦИЯ ===
    CONSTRUCTOR_LINK = (By.CSS_SELECTOR,"p.AppHeader_header__linkText__3q_va.ml-2")  # Ссылка «Конструктор» в шапке
    LOGO_LINK = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers
    PROFILE_LOGOUT_BTN = (By.CLASS_NAME, "Account_button__14Yp3")  # Кнопка «Выйти» в профиле


    # === КОНСТРУКТОР БУРГЕРА ===
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")  # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")  # Вкладка «Начинки»
