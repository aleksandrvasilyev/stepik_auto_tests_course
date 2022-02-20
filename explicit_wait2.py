from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    # name = browser.find_element_by_xpath('//input[@name="firstname"]')
    # name.send_keys('Alex')
    #
    # lname = browser.find_element_by_xpath('//input[@name="lastname"]')
    # lname.send_keys('Johnson')
    #
    # email = browser.find_element_by_xpath('//input[@name="email"]')
    # email.send_keys('email@gmail.com')
    #
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    # file = browser.find_element_by_id('file')
    # file.send_keys(file_path)
    # time.sleep(2)
    # button = browser.find_element_by_id("verify")
    # button.click()
    # message = browser.find_element_by_id("verify_message")
    #
    # assert "Verification was successful!" in message.text

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element_by_tag_name('button')
    button.click()

    #
    # button = browser.find_element_by_tag_name('button')
    # button.click()
    #
    # browser.switch_to.window(browser.window_handles[1])
    #
    x = browser.find_element_by_id('input_value').text
    x = calc(x)

    a = browser.find_element_by_id('answer')
    a.send_keys(x)

    button2 = browser.find_element_by_id('solve')
    button2.click()


finally:
    time.sleep(15)
    browser.quit()
