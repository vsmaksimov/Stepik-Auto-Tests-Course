from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(y)
robot_cb = browser.find_element_by_id('robotCheckbox')
robot_cb.click()
robot_rb = browser.find_element_by_id('robotsRule')
robot_rb.click()
button = browser.find_element_by_tag_name('button')
button.click()
