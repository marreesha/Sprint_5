import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.locators import LoginPageLocators, RegistrationPageLocators, MainPageLocators
from helpers.generators import generate_login, generate_password
from helpers.urls import URLs


@pytest.fixture
def driver():
    """Фикстура для запуска и завершения работы браузера"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def generated_user():
    """Фикстура для генерации уникального логина и пароля"""
    email = generate_login()
    password = generate_password()
    return email, password

@pytest.fixture
def register_user(driver, generated_user):
    """Фикстура для регистрации пользователя"""
    email, password = generated_user
    print(f"Регистрация нового пользователя:\n  Email: {email}, Пароль: {password}")

    driver.get(URLs.REGISTER_PAGE)
    driver.find_element(*RegistrationPageLocators.REGISTRATION_NAME_INPUT).send_keys("Тестовый пользователь")
    driver.find_element(*RegistrationPageLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTRATION_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(URLs.LOGIN_PAGE))
    return email, password

@pytest.fixture
def login_user(driver, register_user):
    """Фикстура для логина пользователя после регистрации"""
    email, password = register_user
    driver.get(URLs.LOGIN_PAGE)
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(URLs.BASE_URL))
    return email, password

@pytest.fixture
def personal_account(driver, login_user):
    """Фикстура для перехода в личный кабинет"""
    email, password = login_user
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(URLs.PROFILE_PAGE))
    return email, password
