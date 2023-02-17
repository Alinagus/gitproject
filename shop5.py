from selenium import webdriver
driver = webdriver.Chrome()
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
wait =  WebDriverWait(driver, 10).until
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(10)
shop = driver.find_element_by_id('menu-item-40').click()
driver.execute_script('window.scrollBy(0, 300)')
add_to_busket = driver.find_element_by_css_selector('.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
time.sleep(5)
busket =  driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0').click()
waiting = wait(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button')))
checkout = driver.find_element_by_class_name('checkout-button').click()
first_name = driver.find_element_by_id('billing_first_name')
first_name.send_keys('Alex')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Bern')
email = driver.find_element_by_id('billing_email')
email.send_keys('auto@mail.ru')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys(89316224539)
country = driver.find_element_by_css_selector('#s2id_billing_country>a>span>b').click()
search = driver.find_element_by_id('s2id_autogen1_search')
search.send_keys('Russia')
russia = driver.find_element_by_id('select2-result-label-394').click()
street = driver.find_element_by_css_selector('#billing_address_1.input-text ')
street.send_keys('Nevsky Avenue, 22')
Town = driver.find_element_by_css_selector('#billing_city.input-text ')
Town.send_keys('Saint-Petersburg')
state = driver.find_element_by_css_selector('#billing_state.input-text')
state.send_keys('Saint-Petersburg')
Postcode = driver.find_element_by_css_selector('#billing_postcode.input-text')
Postcode.send_keys('1234')
place_order = driver.find_element_by_id('place_order').click()
text = wait(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
payment_method = wait(EC.text_to_be_present_in_element((By.CLASS_NAME, 'method'), 'Direct Bank Transfer'))



