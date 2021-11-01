from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:/Users/Andrius/Desktop/filmai_in/Filmai.in-Bot/chromedriver.exe')
url = ('https://filmai.in/')
driver.get(url)
driver.maximize_window()


driver.find_element_by_xpath('//*[@id="navbarsExampleContainer"]/div/button[2]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="login_append"]').send_keys('####')
driver.find_element_by_xpath('//*[@id="password_append"]').send_keys('####')
driver.find_element_by_xpath('//*[@id="rememberThis"]').click()
driver.find_element_by_xpath('//*[@id="submit_button"]').click()

driver.implicitly_wait(3)

try:
    driver.find_element_by_xpath('//*[@id="navCollapseB"]/div/div/div/div[2]/div[1]/div[1]/div/div[2]').click()
    driver.close()
except NoSuchElementException:
    driver.close()   

  