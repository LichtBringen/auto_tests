from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    browser.implicitly_wait(5)

    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), '$100')
    )
    browser.find_element(By.XPATH, '//button[@id="book"]').click()
    var = browser.find_element(By.XPATH, '//span[@id="input_value"]').text

    form = math.log(abs(12 * math.sin(int(var))))

    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(f'{form}')
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(7)
    browser.quit()
