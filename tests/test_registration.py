import pytest
from conftest import driver
from helpers.locators import RegistrationPageLocators
from helpers.generators import generate_login, generate_password
from helpers.urls import URLs
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def register_user(driver, password_length):
    """Функция для регистрации нового пользователя"""
    email = generate_login()
    password = generate_password(password_length)
    print(f"Регистрация нового пользователя:\n  Email: {email}, Пароль: {password}")

    driver.get(URLs.REGISTER_PAGE)
    driver.find_element(*RegistrationPageLocators.REGISTRATION_NAME_INPUT).send_keys("Тестовый пользователь")
    driver.find_element(*RegistrationPageLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTRATION_SUBMIT_BUTTON).click()

    return email, password


class TestRegistration:

    @pytest.mark.parametrize("password_length", [6, 7, 10, 20])
    def test_registration_new_user_correct_data_success(self, driver, password_length):
        """Тест регистрации со сгенерированными логином и паролем"""
        # Регистрируем пользователя
        register_user(driver, password_length)
        # Ожидаем сигнала успешной регистрации
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.LOGIN_PAGE))
        # Проверка успешной регистрации
        assert driver.current_url == URLs.LOGIN_PAGE, "Регистрация не удалась"

    @pytest.mark.parametrize("password_length", [1, 3, 5])
    def test_registration_new_user_short_pass_fail(self, driver, password_length):
        """Тест ошибки регистрации с коротким паролем"""
        # Регистрируем пользователя с коротким паролем
        register_user(driver, password_length)
        # Ожидаем сигнала ошибки регистрации
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_ERROR_MESSAGE)
        )
        # Проверяем текст ошибки
        error_message = driver.find_element(*RegistrationPageLocators.REGISTRATION_ERROR_MESSAGE).text
        assert error_message == "Некорректный пароль"
