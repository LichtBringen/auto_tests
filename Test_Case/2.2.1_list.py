from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')


    var1 = browser.find_element(By.XPATH, '//span[@id="num1"]').text
    var2 = browser.find_element(By.XPATH, '//span[@id="num2"]').text
    Select(browser.find_element(By.XPATH, '//select[@id="dropdown"]')).select_by_visible_text(f'{int(var1) + int(var2)}')
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(10)
    browser.quit()
