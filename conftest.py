import pytest
from selenium import webdriver
from data import generate_unique_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    email = generate_unique_email()
    password = generate_password(6)
    name = "TestUser"
    return {
        "name": name,
        "email": email,
        "password": password
    }

@pytest.fixture
def created_user():
    email = generate_unique_email()
    password = generate_password(6)
    name = "TestUser"
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

@pytest.fixture
def registered_user_via_ui(driver, user_data):
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
    )
    return user_data