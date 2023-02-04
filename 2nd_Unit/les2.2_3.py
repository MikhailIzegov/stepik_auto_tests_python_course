from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    n1_element = browser.find_element(By.ID, "num1")
    n1 = n1_element.text
    n2_element = browser.find_element(By.ID, "num2")
    n2 = n2_element.text
    outcome = str(int(n1) + int(n2))
    openDropDown = Select(browser.find_element(By.TAG_NAME, "select"))
    openDropDown.select_by_visible_text(outcome)
    submitBT = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submitBT.click()
finally:
    time.sleep(10)
    browser.quit()
