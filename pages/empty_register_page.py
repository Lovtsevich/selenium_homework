from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "https://practicesoftwaretesting.com/auth/register"
    REG_BUTTON = (By.CSS_SELECTOR, "[data-test='register-submit']")
    # REG_BUTTON = (By.CLASS_NAME, "btnSubmit.mb-3")
    ERROR_FIRST_NAME = (By.CSS_SELECTOR, "[data-test='first-name-error']")
    ERROR_LAST_NAME = (By.CSS_SELECTOR, "[data-test='last-name-error']")
    ERROR_DOB = (By.CSS_SELECTOR, "[data-test='dob-error']")
    ERROR_POSTAL_CODE = (By.ID, "postal_code-error")
    ERROR_HOUSE_NUMBER = (By.CSS_SELECTOR, "[data-test='house_number-error']")
    ERROR_STREET = (By.ID, "street-error")
    ERROR_CITY = (By.ID, "city-error")
    ERROR_STATE = (By.ID, "state-error")
    ERROR_PHONE = (By.ID, "phone-error")
    ERROR_EMAIL = (By.ID, "email-error")
    ERROR_PASSWORD = (By.ID, "password-error")
    ERROR_COUNTRY = (By.ID, "country-error")

    def click_register(self):
        self.wait_clickable(self.REG_BUTTON)
        self.click(self.REG_BUTTON)

    def find_first_name_error(self, text):
        self.find(self.ERROR_FIRST_NAME)
        self.get_text(self.ERROR_FIRST_NAME, text)

    def find_last_name_error(self, text):
        self.find(self.ERROR_LAST_NAME)
        self.get_text(self.ERROR_LAST_NAME, text)

    def find_dob_error(self, text):
        self.find(self.ERROR_DOB)
        self.get_text(self.ERROR_DOB, text)

    def find_postal_code_error(self, text):
        self.find(self.ERROR_POSTAL_CODE)
        self.get_text(self.ERROR_POSTAL_CODE, text)

    def find_house_number_error(self, text):
        self.find(self.ERROR_HOUSE_NUMBER)
        self.get_text(self.ERROR_HOUSE_NUMBER, text)

    def find_street_error(self, text):
        self.find(self.ERROR_STREET)
        self.get_text(self.ERROR_STREET, text)

    def find_city_error(self, text):
        self.find(self.ERROR_CITY)
        self.get_text(self.ERROR_CITY, text)

    def find_state_error(self, text):
        self.find(self.ERROR_STATE)
        self.get_text(self.ERROR_STATE, text)

    def find_phone_error(self, text):
        self.find(self.ERROR_PHONE)
        self.get_text(self.ERROR_PHONE, text)

    def find_email_error(self, text):
        self.find(self.ERROR_EMAIL)
        self.get_text(self.ERROR_EMAIL, text)

    def find_password_error(self, text):
        self.find(self.ERROR_PASSWORD)
        self.get_text(self.ERROR_PASSWORD, text)

    def find_country_error(self, text):
        self.find(self.ERROR_COUNTRY)
        self.get_text(self.ERROR_COUNTRY, text)