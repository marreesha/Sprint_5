from conftest import driver, generated_user, register_user, login_user
from helpers.locators import ConstructorLocators


class TestConstructorNavigation:

    def test_constructor_default_buns_success(self, driver, login_user):
        parent_element = driver.find_element(*ConstructorLocators.BUNS_PARENT_SECTION)
        # Проверяем, что "Булки" - дефолтное значение
        assert "tab_tab_type_current" in parent_element.get_attribute("class")

    def test_transition_to_buns_success(self, driver, login_user):
        # Кликнуть на другую категорию, так как "Булки" уже выбран
        driver.find_element(*ConstructorLocators.SAUCES_SECTION).click()
        # Кликнуть по кнопке "Булки"
        driver.find_element(*ConstructorLocators.BUNS_SECTION).click()
        parent_element = driver.find_element(*ConstructorLocators.BUNS_PARENT_SECTION)
        # Проверяем, что страница проскроллилась до нужной позиции
        assert "tab_tab_type_current" in parent_element.get_attribute("class")

    def test_transition_to_sauces_success(self, driver, login_user):
        # Кликнуть по кнопке "Соусы"
        driver.find_element(*ConstructorLocators.SAUCES_SECTION).click()
        parent_element = driver.find_element(*ConstructorLocators.SAUCES_PARENT_SECTION)
        # Проверяем, что страница проскроллилась до нужной позиции
        assert "tab_tab_type_current" in parent_element.get_attribute("class")

    def test_transition_to_fillings_success(self, driver, login_user):
        # Кликнуть по кнопке "Начинки"
        driver.find_element(*ConstructorLocators.FILLINGS_SECTION).click()
        parent_element = driver.find_element(*ConstructorLocators.FILLINGS_PARENT_SECTION)
        # Проверяем, что страница проскроллилась до нужной позиции
        assert "tab_tab_type_current" in parent_element.get_attribute("class")
