# coding=utf-8
from selenium import webdriver
driver =webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://www.duoceshi.com:8080/bbs/forum.php')
driver.find_element_by_id('ls_username').send_keys('chenquan')
driver.find_element_by_id('ls_password').send_keys('123456')
driver.find_element_by_css_selector('#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button').click()