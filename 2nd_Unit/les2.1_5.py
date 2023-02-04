from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    #Следующая команда из всего элемента выделит только текст и присвоеит переменной x
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input_checkbox.click()
    inputRB = browser.find_element(By.XPATH, "//label[text()='Robots rule']")
    inputRB.click()
    submit_btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()