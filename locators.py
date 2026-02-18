from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка на "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']") # Ссылка на "Личный кабинет"
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div") # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div") # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div") # Раздел "Начинки"
    BUNS_HEADER = (By.XPATH, ".//h2[text()='Булки']") # Заголовок "Булки"
    SAUCES_HEADER = (By.XPATH, ".//h2[text()='Соусы']") # Заголовок "Соусы"
    FILLINGS_HEADER = (By.XPATH, ".//h2[text()='Начинки']") # Заголовок "Начинки"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']") # Ссылка "Конструктор"
    LOGO = (By.XPATH, ".//a[@href='/' and contains(@class, 'logo')]") # Логотип Stellar Burgers
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']") #Кнопка оформления заказа(после логина)

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']") # Поле Email на странице входа
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']") # Поле Пароль
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка Войти
    REGISTER_LINK = (By.XPATH, ".//a[@href='/register']") # Ссылка на страницу регистрации
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']") # Ссылка на страницу восстановления пароля

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, ".//fieldset[1]//input") # Поле Имя
    EMAIL_INPUT = (By.XPATH, ".//fieldset[2]//input") # Поле Email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']") # Поле Пароль
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']") # Ссылка "Войти" на странице регистрации
    INCORRECT_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']") # Сообщение об ошибке при неправильном пароле

class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']") # Ссылка "Войти" на странице восстановления

class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") # Кнопка выхода
    PROFILE_HEADER = (By.XPATH, ".//a[text()='Профиль']") # Заголовок профиля при авторизованном пользователе
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']")
    LOGO = (By.XPATH, ".//a[@href='/']")