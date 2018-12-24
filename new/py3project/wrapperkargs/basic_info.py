# coding =utf-8
import time


class PageObject(object):
    def __init__(self, driver):
        self.driver = driver

    def test(self):
        ele = self.driver.find_element_by_id("menu-user")
        return ele

    def login(self):
        self.driver.find_element_by_id("userAccount").send_keys("admin")
        self.driver.find_element_by_id("loginPwd").send_keys(123456)
        time.sleep(2)
        self.driver.find_element_by_id("loginBtn").click()
