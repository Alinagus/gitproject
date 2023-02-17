from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver.get('http://practice.automationtesting.in/')
my_account = driver.find_element_by_id('menu-item-50').click()
login = driver.find_element_by_css_selector('#reg_email:nth-child(2)')
login.send_keys('guseinovaalina02@gmail.com')
password = driver.find_element_by_css_selector('#reg_password:nth-child(2)')
password.send_keys('AlinaGus2023!')
register = driver.find_element_by_css_selector('.woocomerce-FormRow.form-row>.button').click()
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



