import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    d = webdriver.Chrome(options=options)
    d.implicitly_wait(3)
    yield d
    d.quit()


def login(d, username=VALID_USER, password=VALID_PASSWORD):
    d.get(BASE_URL)
    d.find_element(By.ID, "user-name").send_keys(username)
    d.find_element(By.ID, "password").send_keys(password)
    d.find_element(By.ID, "login-button").click()


def test_01_valid_login(driver):
    login(driver)
    assert driver.current_url.endswith("/inventory.html")


def test_02_invalid_login(driver):
    login(driver, "standard_user", "wrong_password")
    error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert "Username and password do not match" in error.text


def test_03_locked_user(driver):
    login(driver, "locked_out_user", VALID_PASSWORD)
    error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert "locked out" in error.text.lower()


def test_04_product_catalog(driver):
    login(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0


def test_05_sort_price_low_to_high(driver):
    login(driver)
    select = driver.find_element(By.CLASS_NAME, "product_sort_container")
    from selenium.webdriver.support.ui import Select
    Select(select).select_by_value("lohi")
    prices = [float(e.text.replace("$", "")) for e in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert prices == sorted(prices)


def test_06_add_product_to_cart(driver):
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"


def test_07_add_multiple_products(driver):
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']").click()
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2"


def test_08_remove_product(driver):
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']").click()
    assert not driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")


def test_09_checkout_validation(driver):
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
    error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert "First Name is required" in error.text


def test_10_complete_checkout(driver):
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("Tester")
    driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("700001")
    driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='finish']").click()
    assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"
