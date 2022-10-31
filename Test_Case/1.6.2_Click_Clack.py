from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')

    var = browser.find_element(By.XPATH, '//span[@id="input_value"]').text

    form = math.log(abs(12*math.sin(int(var))))

    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(f'{form}')
    browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    browser.find_element(By.XPATH, '//label[text()="Robots rule"]').click()
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(10)
    browser.quit()
