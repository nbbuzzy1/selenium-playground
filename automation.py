from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')


show_msg_button = chrome_browser.find_element_by_class_name('btn-default')
assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am extra cool')

# new_el = chrome_browser.find_element_by_css_selector('.btn')

# show_msg_button.click()

chrome_browser.close()
chrome_browser.close()  # or quit()
