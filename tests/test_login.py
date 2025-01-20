from conftest import driver, generated_user, register_user
from helpers.locators import LoginPageLocators, MainPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from helpers.urls import URLs
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def perform_login(driver, email, password):
    """Функция для выполнения входа"""
    # Ввод email и пароля
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем, что URL будет изменен
    WebDriverWait(driver, 3).until(EC.url_to_be(URLs.BASE_URL))

    # Возвращаем текущий URL для проверки
    return driver.current_url


class TestLogin:

    def test_login_with_login_account_btn_success(self, driver, register_user):
        """Тест входа в аккаунт по кнопке «Войти в аккаунт» на главной"""
        email, password = register_user
        # Переход на главную страницу
        driver.get(URLs.BASE_URL)
        # Клик на кнопку для входа
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        assert perform_login(driver, email, password) == URLs.BASE_URL, "Не удалось войти в аккаунт"

    def test_login_with_personal_account_btn_success(self, driver, register_user):
        """Тест входа в аккаунт через кнопку «Личный кабинет»"""
        email, password = register_user
        # Клик на кнопку для входа
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert perform_login(driver, email, password) == URLs.BASE_URL, "Не удалось войти в аккаунт"

    def test_login_with_btn_in_registration_form_success(self, driver, register_user):
        """Тест входа в аккаунт через кнопку в форме регистрации"""
        email, password = register_user
        # Переход на главную страницу
        driver.get(URLs.REGISTER_PAGE)
        # Клик на кнопку для входа
        driver.find_element(*RegistrationPageLocators.REGISTRATION_LOGIN_BUTTON).click()
        assert perform_login(driver, email, password) == URLs.BASE_URL, "Не удалось войти в аккаунт"

    def test_login_in_password_recovery_form_success(self, driver, register_user):
        """Тест входа в аккаунт через кнопку в форме восстановления пароля"""
        email, password = register_user
        # Переход на главную страницу
        driver.get(URLs.FORGOT_PASSWORD_PAGE)
        # Клик на кнопку для входа
        driver.find_element(*ForgotPasswordPageLocators.FORGOT_PASSWORD_LOGIN_BUTTON).click()
        assert perform_login(driver, email, password) == URLs.BASE_URL, "Не удалось войти в аккаунт"
