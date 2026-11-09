from pages.empty_register_page import RegisterPage


def test_empty_first_name_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_FIRST_NAME) == "First name is required"

def test_empty_last_name_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_LAST_NAME) == "Last name is required"

def test_empty_dob_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_DOB) == "Please enter a valid date in YYYY-MM-DD format.\nDate of Birth is required"

def test_empty_postal_code_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_POSTAL_CODE) == "Postcode is required"

def test_empty_house_number_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_HOUSE_NUMBER).strip() == "House number is required"

def test_empty_street_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_STREET).strip() ==  "Street is required"

def test_empty_city_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_CITY).strip() ==  "City is required"

def test_empty_state_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_STATE).strip() ==  "State is required"

def test_empty_phone_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_PHONE).strip() ==  "Phone is required."

def test_empty_email_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_EMAIL).strip() ==  "Email is required"

def test_empty_password_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_PASSWORD).strip() ==  "Password is required\nPassword must be minimal 6 characters long.\nPassword can not include invalid characters."

def test_empty_country_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    
    assert page.get_text(page.ERROR_COUNTRY).strip() ==  "Country is required"


            