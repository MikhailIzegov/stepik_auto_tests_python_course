from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_book = browser.find_element(By.CSS_SELECTOR, "#book").click()
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    answ = browser.find_element(By.ID, "answer")
    answ.send_keys(calc(x))
    sbmt2 = browser.find_element(By.XPATH, "//button[text()='Submit']").click()
finally:
    time.sleep(7)
    browser.quit()