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
book = driver.find_element_by_css_selector('.products.masonry-done>li:nth-child(3)>a:nth-child(1)').click()
test = driver.find_element_by_css_selector('#content>div>div>.product_title.entry-title')
element = driver.find_element_by_css_selector(".summary.entry-summary>h1")
element_get_text = element.text
assert element_get_text == "HTML5 Forms"






