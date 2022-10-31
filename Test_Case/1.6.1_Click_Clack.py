from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/find_link_text')

    var = math.ceil(math.pow(math.pi, math.e)*10000)

    browser.find_element(By.XPATH, f'//a[text()="{var}"]').click()
    browser.find_element(By.XPATH, '//input[@name="first_name"]').send_keys('Sergo')
    browser.find_element(By.XPATH, '//input[@name="last_name"]').send_keys('Dem')
    browser.find_element(By.XPATH, '//input[@class="form-control city"]').send_keys('Moscow')
    browser.find_element(By.XPATH, '//input[@id="country"]').send_keys('Russia')
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

    txt = list(browser.switch_to.alert.text)[-17:]
    browser.switch_to.alert.accept()
    browser.quit()

    var = txt[0]
    for i in range(1, len(txt)):
        var += txt[i]

finally:
    time.sleep(5)
    browser.quit()

print(var)