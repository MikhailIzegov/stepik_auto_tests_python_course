from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    attr_value = x_element.get_attribute("valuex")
    y = calc(attr_value)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input_checkbox.click()
    inputRB = browser.find_element(By.ID, "robotsRule")
    inputRB.click()
    submit_btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()