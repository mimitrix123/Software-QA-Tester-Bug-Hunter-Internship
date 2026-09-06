import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://www.saucedemo.com/'
USER = 'standard_user'
PASSWORD = 'secret_sauce'

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1440,1000')
    d = webdriver.Chrome(options=options)
    d.implicitly_wait(3)
    yield d
    d.quit()

def login(d, username=USER, password=PASSWORD):
    d.get(BASE_URL)
    d.find_element(By.ID, 'user-name').send_keys(username)
    d.find_element(By.ID, 'password').send_keys(password)
    d.find_element(By.ID, 'login-button').click()

def add_backpack(d):
    d.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()

def test_01_valid_login(driver):
    login(driver); assert driver.current_url.endswith('/inventory.html')

def test_02_invalid_login(driver):
    login(driver, USER, 'bad-password')
    e = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='error']")))
    assert 'Username and password do not match' in e.text

def test_03_locked_user(driver):
    login(driver, 'locked_out_user', PASSWORD)
    e = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='error']")))
    assert 'locked out' in e.text.lower()

def test_04_inventory_products(driver):
    login(driver); assert len(driver.find_elements(By.CLASS_NAME,'inventory_item')) > 0

def test_05_sort_price_low_high(driver):
    login(driver); Select(driver.find_element(By.CLASS_NAME,'product_sort_container')).select_by_value('lohi')
    prices=[float(x.text.replace('$','')) for x in driver.find_elements(By.CLASS_NAME,'inventory_item_price')]
    assert prices == sorted(prices)

def test_06_add_backpack(driver):
    login(driver); add_backpack(driver); assert driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text == '1'

def test_07_add_multiple_items(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CSS_SELECTOR,"[data-test='add-to-cart-sauce-labs-bike-light']").click()
    assert driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text == '2'

def test_08_remove_item(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CSS_SELECTOR,"[data-test='remove-sauce-labs-backpack']").click()
    assert not driver.find_elements(By.CLASS_NAME,'shopping_cart_badge')

def test_09_open_cart(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert driver.current_url.endswith('/cart.html')

def test_10_checkout_required_validation(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    driver.find_element(By.CSS_SELECTOR,"[data-test='checkout']").click(); driver.find_element(By.CSS_SELECTOR,"[data-test='continue']").click()
    e=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='error']")))
    assert 'First Name is required' in e.text

def test_11_checkout_valid_information(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CLASS_NAME,'shopping_cart_link').click(); driver.find_element(By.CSS_SELECTOR,"[data-test='checkout']").click()
    driver.find_element(By.CSS_SELECTOR,"[data-test='firstName']").send_keys('QA'); driver.find_element(By.CSS_SELECTOR,"[data-test='lastName']").send_keys('Tester'); driver.find_element(By.CSS_SELECTOR,"[data-test='postalCode']").send_keys('700001'); driver.find_element(By.CSS_SELECTOR,"[data-test='continue']").click()
    assert driver.current_url.endswith('/checkout-step-two.html')

def test_12_checkout_overview_item(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CLASS_NAME,'shopping_cart_link').click(); driver.find_element(By.CSS_SELECTOR,"[data-test='checkout']").click()
    driver.find_element(By.CSS_SELECTOR,"[data-test='firstName']").send_keys('QA'); driver.find_element(By.CSS_SELECTOR,"[data-test='lastName']").send_keys('Tester'); driver.find_element(By.CSS_SELECTOR,"[data-test='postalCode']").send_keys('700001'); driver.find_element(By.CSS_SELECTOR,"[data-test='continue']").click()
    assert driver.find_element(By.CLASS_NAME,'inventory_item_name').text == 'Sauce Labs Backpack'

def test_13_checkout_total_visible(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CLASS_NAME,'shopping_cart_link').click(); driver.find_element(By.CSS_SELECTOR,"[data-test='checkout']").click()
    driver.find_element(By.CSS_SELECTOR,"[data-test='firstName']").send_keys('QA'); driver.find_element(By.CSS_SELECTOR,"[data-test='lastName']").send_keys('Tester'); driver.find_element(By.CSS_SELECTOR,"[data-test='postalCode']").send_keys('700001'); driver.find_element(By.CSS_SELECTOR,"[data-test='continue']").click()
    assert driver.find_element(By.CLASS_NAME,'summary_total').is_displayed()

def test_14_complete_order(driver):
    login(driver); add_backpack(driver); driver.find_element(By.CLASS_NAME,'shopping_cart_link').click(); driver.find_element(By.CSS_SELECTOR,"[data-test='checkout']").click()
    driver.find_element(By.CSS_SELECTOR,"[data-test='firstName']").send_keys('QA'); driver.find_element(By.CSS_SELECTOR,"[data-test='lastName']").send_keys('Tester'); driver.find_element(By.CSS_SELECTOR,"[data-test='postalCode']").send_keys('700001'); driver.find_element(By.CSS_SELECTOR,"[data-test='continue']").click(); driver.find_element(By.CSS_SELECTOR,"[data-test='finish']").click()
    assert driver.find_element(By.CLASS_NAME,'complete-header').text == 'Thank you for your order!'

def test_15_logout(driver):
    login(driver); driver.find_element(By.ID,'react-burger-menu-btn').click(); WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'logout_sidebar_link'))).click()
    assert driver.current_url == BASE_URL
