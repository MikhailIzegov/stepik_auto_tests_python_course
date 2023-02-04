from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()

    def my_function(url):
        browser.get(url)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("37236@mail.ru")
        input4 = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone"]')
        input4.send_keys("385674326")
        input5 = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
        input5.send_keys("krochmalna 55")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    my_function(link1)
    my_function(link2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()