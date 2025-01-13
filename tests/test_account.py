from conftest import driver, generated_user, register_user, login_user, personal_account
from helpers.locators import MainPageLocators, PersonalAccountLocators
from helpers.urls import URLs
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAccount:

    def test_go_to_personal_account_success(self, driver, login_user):
        """Тест перехода по клику на «Личный кабинет»"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # Ожидаем, что URL будет изменен
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.PROFILE_PAGE))
        # Проверка успешного входа в личный кабинет
        assert driver.current_url == URLs.PROFILE_PAGE, "Не удалось войти в личный кабинет"

    def test_go_to_constructor_by_constructor_btn_success(self, driver, personal_account):
        """Тест перехода по клику на «Конструктор»"""
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        # Ожидаем, что URL будет изменен
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.BASE_URL))
        # Проверка успешного входа в личный кабинет
        assert driver.current_url == URLs.BASE_URL, "Не удалось перейти в конструктор"

    def test_go_to_constructor_by_stellar_burgers_success(self, driver, personal_account):
        """Тест перехода по клику на логотип Stellar Burgers"""
        driver.find_element(*MainPageLocators.LOGO).click()
        # Ожидаем, что URL будет изменен
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.BASE_URL))
        # Проверка успешного входа в личный кабинет
        assert driver.current_url == URLs.BASE_URL, "Не удалось перейти в конструктор"

    def test_exit_personal_account_success(self, driver, personal_account):
        """Тест выхода из аккаунта по кнопке «Выйти» в личном кабинете"""
        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
        # Ожидаем, что URL будет изменен
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.LOGIN_PAGE))
        # Проверка успешного входа в личный кабинет
        assert driver.current_url == URLs.LOGIN_PAGE, "Не удалось выйти из аккаунта"
