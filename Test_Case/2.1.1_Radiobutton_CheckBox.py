from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')


    var = browser.find_element(By.XPATH, '//img[@id="treasure"]').get_attribute('Valuex')

    form = math.log(abs(12*math.sin(int(var))))

    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(f'{form}')
    browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    browser.find_element(By.XPATH, '//input[@id="robotsRule"]').click()
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(10)
    browser.quit()

