from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.get('http://practice.automationtesting.in/')
account = driver.find_element_by_id('menu-item-50').click()
username = driver.find_element_by_id('username')
username.send_keys('guseinovaalina02@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('AlinaGus2023!')
login = driver.find_element_by_name('login').click()
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


