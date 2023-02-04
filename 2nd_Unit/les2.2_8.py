import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Пися")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Попкин")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("pisya@popka.com")
    for_files = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test_file for sending on a web page.txt"
    file_path = os.path.join(current_dir, file_name)
    for_files.send_keys(file_path)
    submt = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submt.click()
finally:
    time.sleep(5)
    browser.quit()