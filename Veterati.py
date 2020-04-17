from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = '/Users/josephtabalon/Desktop/chromedriver')

driver.get('https://enter.veterati.com/mentee/auth/login')
main_page = driver.current_window_handle

login = driver.find_element_by_xpath('//*[@id="signin_link"]/a')
login.click()

linkedin = driver.find_element_by_xpath('//*[@id="signin_content"]/div/p')
linkedin.click()

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

driver.switch_to.window(login_page)

email = 'joseph.tabalon.jr@gmail.com'
user = driver.find_element_by_xpath('//*[@id="username"]')
user.send_keys(email)

password = input('Enter password: ')
userPass = driver.find_element_by_xpath('//*[@id="password"]')
userPass.send_keys(password)

linkedinloginbutton = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
linkedinloginbutton.click()