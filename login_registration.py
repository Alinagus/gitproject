from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://practice.automationtesting.in/')
my_account = driver.find_element_by_id('menu-item-50').click()
login = driver.find_element_by_css_selector('#reg_email:nth-child(2)')
login.send_keys('guseinovaalina02@gmail.com')
password = driver.find_element_by_css_selector('#reg_password:nth-child(2)')
password.send_keys('AlinaGus2023!')
register = driver.find_element_by_css_selector('.woocomerce-FormRow.form-row>.button').click()




