from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://practice.automationtesting.in/')
account = driver.find_element_by_id('menu-item-50').click()
username = driver.find_element_by_id('username')
username.send_keys('guseinovaalina02@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('AlinaGus2023!')
login = driver.find_element_by_name('login').click()
shop_2 = driver.find_element_by_id('menu-item-40').click()
HTML = driver.find_element_by_css_selector('.cat-item.cat-item-19>a').click()
items_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
if len(items_count) !=3:
    print('Ошибка', len(items_count))
else: print('Отображается:', len(items_count))

