from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Личный кабинет" в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка "Конструктор" в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers в шапке сайта
    LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")

class RegistrationPageLocators:
    # Поле ввода имени при регистрации
    REGISTRATION_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле ввода email при регистрации
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле ввода пароля при регистрации
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка подтверждения регистрации
    REGISTRATION_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке при неверных данных регистрации
    REGISTRATION_ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")
    # Кнопка "Войти" на странице регистрации
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")

class LoginPageLocators:
    # Поле ввода email на странице авторизации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле ввода пароля на странице авторизации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка подтверждения входа в аккаунт
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

class PersonalAccountLocators:
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class ConstructorLocators:
    # Кнопка перехода в секцию "Булки" в конструкторе
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    # Родительский элемент секции "Булки"
    BUNS_PARENT_SECTION = (By.XPATH, "//span[text()='Булки']/parent::*")
    # Кнопка перехода в секцию "Соусы" в конструкторе
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    # Родительский элемент секции "Соусы"
    SAUCES_PARENT_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::*")
    # Кнопка перехода в секцию "Начинки" в конструкторе
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    # Родительский элемент секции "Начинки"
    FILLINGS_PARENT_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::*")

class ForgotPasswordPageLocators:
    # Поле ввода email для восстановления пароля
    FORGOT_PASSWORD_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Кнопка "Восстановить" на странице восстановления пароля
    FORGOT_PASSWORD_RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Кнопка "Войти" на странице восстановления пароля
    FORGOT_PASSWORD_LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")

class ResetPasswordPageLocators:
    # Поле ввода нового пароля
    RESET_PASSWORD_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Поле ввода кода из письма
    RESET_PASSWORD_LETTER_CODE = (By.XPATH, "//label[text()='Введите код из письма']/following-sibling::input")
    # Кнопка подтверждения сохранения нового пароля
    RESET_PASSWORD_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    # Кнопка "Войти" на странице сброса пароля
    RESET_PASSWORD_LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")
