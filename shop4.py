from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://practice.automationtesting.in/')
account = driver.find_element_by_id('menu-item-50').click()
username = driver.find_element_by_id('username')
username.send_keys('guseinovaalina02@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('AlinaGus2023!')
login = driver.find_element_by_name('login').click()
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