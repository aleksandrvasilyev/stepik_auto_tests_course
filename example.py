from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()

    input3 = browser.find_element_by_id('robotsRule')
    input3.click()

    input4 = browser.find_element_by_tag_name('button')
    input4.click()


finally:
    time.sleep(5)
    browser.quit()
