from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators

class TestConstructor:

    def test_switch_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()

        sauces_header = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES_HEADER)
        )
        assert sauces_header.is_displayed()

    def test_switch_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()

        fillings_header = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.FILLINGS_HEADER)
        )
        assert fillings_header.is_displayed()

    def test_switch_to_buns_section_from_another(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES_HEADER)
        )
        driver.find_element(*MainPageLocators.BUNS_SECTION).click()

        buns_header = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
        )
        assert buns_header.is_displayed()



