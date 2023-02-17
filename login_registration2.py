from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://practice.automationtesting.in/')
account = driver.find_element_by_id('menu-item-50').click()
username = driver.find_element_by_id('username')
username.send_keys('guseinovaalina02@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('AlinaGus2023!')
login = driver.find_element_by_name('login').click()
check = driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation>ul>li:nth-child(6)>a')
check_text =check.text
assert check_text == "Logout"
driver.quit()