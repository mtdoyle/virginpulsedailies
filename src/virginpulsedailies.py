import os
import time

from selenium import webdriver


def virginpulsedailies():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    chromedriver_path = os.getenv("CHROMEDRIVERPATH")
    driver = webdriver.Chrome(chromedriver_path)
    driver.get('http://member.virginpulse.com/login.aspx')
    time.sleep(10)
    username_box = driver.find_element_by_id('username')
    username_box.click()
    username_box.send_keys(username)
    time.sleep(2)
    while not username_box.get_attribute('value') == username:
        username_box.clear()
        username_box.send_keys(username)
        time.sleep(2)

    password_box = driver.find_element_by_id('password')
    password_box.click()
    password_box.send_keys(password)
    time.sleep(2)
    while not password_box.get_attribute('value') == password:
        password_box.clear()
        password_box.send_keys(password)
        time.sleep(2)

    driver.find_element_by_id('kc-login').click()
    time.sleep(20)
    trophy_box = driver.find_elements_by_id('trophy-modal-close-btn')
    if trophy_box:
        trophy_box[0].click()
        time.sleep(3)
    daily_tips_done = driver.find_elements_by_class_name('daily-tips-all-done')
    cycle = 0
    while cycle < 5 and not daily_tips_done:
        got_it_card = driver.find_elements_by_id('triggerCloseCurtain')
        if got_it_card:
            if got_it_card[0].text == 'GOT IT!':
                got_it_card[0].click()
        true_false_card = driver.find_elements_by_class_name('quiz-true-false-buttons')
        if true_false_card:
            true_false_card[0].click()
            time.sleep(5)
            driver.find_element_by_class_name('got-it-core-button').click()
        cycle = cycle + 1
        time.sleep(3)
        daily_tips_done = driver.find_elements_by_class_name('daily-tips-all-done')
    hh_button = driver.find_element_by_class_name('hh-wrapper')
    hh_button.click()
    time.sleep(1)
    driver.execute_script('document.querySelector(\'#page-wrapper > div > div > div > basic-home > div > div > div:nth-child(4) > home-healthy-habits > div > div > div:nth-child(1) > home-healthy-habit-tile > div > div.home-healthy-habit-yesno.ng-scope > button.btn-primary-inverse.vp-button-primary-inverse.yesNo-btn.yes-btn.ng-scope\').click()')
    driver.execute_script('document.querySelector(\'#page-wrapper > div > div > div > basic-home > div > div > div:nth-child(4) > home-healthy-habits > div > div > div:nth-child(2) > home-healthy-habit-tile > div > div.home-healthy-habit-yesno.ng-scope > button.btn-primary-inverse.vp-button-primary-inverse.yesNo-btn.yes-btn.ng-scope\').click()')
    driver.execute_script('document.querySelector(\'#page-wrapper > div > div > div > basic-home > div > div > div:nth-child(4) > home-healthy-habits > div > div > div:nth-child(3) > home-healthy-habit-tile > div > div.home-healthy-habit-yesno.ng-scope > button.btn-primary-inverse.vp-button-primary-inverse.yesNo-btn.yes-btn.ng-scope\').click()')
    driver.execute_script('document.querySelector(\'#page-wrapper > div > div > div > basic-home > div > div > div:nth-child(4) > home-healthy-habits > div > div > div:nth-child(4) > home-healthy-habit-tile > div > div.home-healthy-habit-yesno.ng-scope > button.btn-primary-inverse.vp-button-primary-inverse.yesNo-btn.yes-btn.ng-scope\')')
    driver.quit()

if __name__ == '__main__':
    virginpulsedailies()