from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators

class TestLogin:

    def test_login_via_main_page_login_button(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    def test_login_via_personal_account_button(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_login_via_registration_form(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_login_via_forgot_password_form(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

