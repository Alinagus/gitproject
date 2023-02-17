from selenium import webdriver
driver = webdriver.Chrome()
import time

driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(10)
shop_3 = driver.find_element_by_id('menu-item-40').click()
driver.execute_script('window.scrollBy(0, 300)')
add_to_busket = driver.find_element_by_css_selector('.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
time.sleep(5)
busket = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0').click()
remove = driver.find_element_by_css_selector('.product-remove>.remove').click()
undo = driver.find_element_by_css_selector('.woocommerce-message>a').click()
count = driver.find_element_by_css_selector('.input-text.qty')
count.clear()
count.send_keys('3')
update = driver.find_element_by_name('update_cart').click()
Quantity = driver.find_element_by_css_selector('.input-text.qty')
Quantity_check = Quantity.get_attribute('value')
if Quantity_check == '3':
    print("количество добавленнных книг:", Quantity_check)
else: print('Ошибка', Quantity_check)
time.sleep(4)
Apply = driver.find_element_by_css_selector('.coupon>.button').click()
text = driver.find_element_by_class_name('woocommerce-error')
element_get_text = text.text
assert element_get_text == "Please enter a coupon code."




