from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element(By.XPATH, '//button[contains(text(), "I want to go")]').click()
    browser.switch_to.window(browser.window_handles[1])
    var = browser.find_element(By.XPATH, '//span[@id="input_value"]').text

    form = math.log(abs(12*math.sin(int(var))))

    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(f'{form}')
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(10)
    browser.quit()