from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationPageLocators, LoginPageLocators

class TestRegistration:

    def test_registration_success(self, driver, user_data):
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(user_data["name"])
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    def test_registration_fail_incorrect_password(self, driver, user_data):
        driver.get("https://stellarburgers.education-services.ru/register")
        short_password = user_data["password"][:5]
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(user_data["name"])
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        error_element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.INCORRECT_PASSWORD_ERROR)
        )
        assert error_element.is_displayed()
        assert driver.current_url == "https://stellarburgers.education-services.ru/register"