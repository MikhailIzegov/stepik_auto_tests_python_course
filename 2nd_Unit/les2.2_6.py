from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = (browser.find_element(By.ID, "input_value")).text
# либо строчку выше можно заменить на (и ничего не изменится!): x = int((browser.find_element(By.ID, "input_value")).text)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    chb = browser.find_element(By.ID, "robotCheckbox")
    chb.click()
    rb = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    rb.click()
    sbmt = browser.find_element(By.XPATH, "//button[text()='Submit']")
    sbmt.click()
finally:
    time.sleep(5)
    browser.quit()
