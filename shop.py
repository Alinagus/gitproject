from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.get('http://practice.automationtesting.in/')
account = driver.find_element_by_id('menu-item-50').click()
username = driver.find_element_by_id('username')
username.send_keys('guseinovaalina02@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('AlinaGus2023!')
login = driver.find_element_by_name('login').click()
shop = driver.find_element_by_id('menu-item-40').click()
book = driver.find_element_by_css_selector('.products.masonry-done>li:nth-child(3)>a:nth-child(1)').click()
test = driver.find_element_by_css_selector('#content>div>div>.product_title.entry-title')
element = driver.find_element_by_css_selector(".summary.entry-summary>h1")
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
shop_2 = driver.find_element_by_id('menu-item-40').click()
HTML = driver.find_element_by_css_selector('.cat-item.cat-item-19>a').click()
items_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
if len(items_count) !=3:
    print('Ошибка', len(items_count))
else: print('Отображается:', len(items_count))
shop = driver.find_element_by_id('menu-item-40').click()
select = driver.find_element_by_css_selector('.woocommerce-ordering>.orderby')
check = select.get_attribute("value")
print("value of check: ", check)
select = driver.find_element_by_class_name('orderby')
select_price = Select(select)
select_price.select_by_value('price-desc')
check2 = driver.find_element_by_css_selector('.orderby>option:nth-child(6)')
ab = check2.get_attribute('selected')
if ab == 'true':
    print('Прверка пройдена')
else: print(ab, 'что-то пошло не так')
shop = driver.find_element_by_id('menu-item-40').click()
book = driver.find_element_by_css_selector('.masonry-done>li:nth-child(1)>a>.attachment-shop_catalog').click()
price = driver.find_element_by_css_selector('del>.woocommerce-Price-amount.amount')
element_get_text = price.text
print(element_get_text)
assert element_get_text == "₹600.00"
price2 = driver.find_element_by_css_selector('ins>.woocommerce-Price-amount.amount')
element_get_text = price2.text
assert element_get_text == "₹450.00"
wait = driver.implicitly_wait(5)
pictures = driver.find_element_by_class_name('attachment-shop_single').click()
wait_2 = driver.implicitly_wait(5)
close = driver.find_element_by_class_name('pp_close').click()
driver.quit()

time.sleep(5)
driver.get('http://practice.automationtesting.in/')
shop_3 = driver.find_element_by_id('menu-item-40').click()
add_to_busket = driver.find_element_by_css_selector('.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
busket = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0').click()
check_price = driver.find_element_by_css_selector('.product-subtotal>.amount')
element_get_text = check_price.text
print(element_get_text)
assert element_get_text == '350.00'
items = driver.find_elements_by_class_name('cartcontents')
element_get_text = items.text
assert element_get_text == '1 item'



