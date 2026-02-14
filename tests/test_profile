from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators

class TestProfile:

    def test_go_to_personal_account(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_HEADER)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

    def test_logout(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_HEADER)
        )
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"
    def test_go_to_constructor_from_profile(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_HEADER)
        )
        driver.find_element(*ProfilePageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_go_to_main_via_logo_from_profile(self, driver, registered_user_via_ui):
        user = registered_user_via_ui
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_HEADER)
        )
        driver.find_element(*ProfilePageLocators.LOGO).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"


