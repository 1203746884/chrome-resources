# coding =utf-8
from selenium import webdriver
from time import sleep


def access_code():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://mail.qq.com/cgi-bin/frame_html?sid=X8TXPdLKi6bWUyB7&r=56ca1d8478e5e4903be3ecab133915c6")
    sleep(4)
    cookie_log = driver.get_cookies()
    print(cookie_log)
    driver.add_cookie({'name': 'u', 'value': '1393232463'})
    """ add username cookie"""
    driver.add_cookie({'name':'p','value': 'icebitch8586'})
    """add  password cookie"""
    driver.get("https://mail.qq.com/cgi-bin/frame_html?sid=X8TXPdLKi6bWUyB7&r=56ca1d8478e5e4903be3ecab133915c6")
    driver.switch_to.frame("login_frame")
    driver.find_element_by_id("u").send_keys("1393232463")
    driver.find_element_by_id("p").send_keys("icebitch8586")
    driver.find_element_by_id("login_button").click()
    sleep(5)
    driver.close()
if __name__ == "__main__":
    access_code()