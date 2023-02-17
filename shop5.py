from selenium import webdriver
driver = webdriver.Chrome()
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.get('http://practice.automationtesting.in/')
shop_3 = driver.find_element_by_id('menu-item-40').click()
add_to_busket = driver.find_element_by_css_selector('.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
time.sleep(3)
check_price = driver.find_element_by_css_selector('.wpmenucart-contents>.amount')
element_get_text = check_price.text
assert element_get_text == '₹350.00'
item = driver.find_element_by_class_name('cartcontents')
element_get_text = item.text
assert element_get_text == '1 Item'
busket = driver.find_element_by_class_name('cartcontents').click()
Subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal>td>.woocommerce-Price-amount.amount'), '₹'))
total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'strong>.woocommerce-Price-amount.amount'), '₹'))
