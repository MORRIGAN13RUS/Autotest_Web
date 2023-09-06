import logging
import time
import yaml
from testpage import OperationsHelper
from os import getcwd

with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test1 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'test1 failed'


def test_step2(browser):
    logging.info('Test2 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site
    testpage.enter_login(data['username'])
    testpage.enter_pass(data['password'])
    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {data["username"]}', 'test2 failed'


def test_step3(browser):
    logging.info('Test3 Starting')
    testpage = OperationsHelper(browser)
    testpage.click_create_post_btn()
    time.sleep(data['sleep_time'])
    testpage.enter_post_title(data['test_title'])
    testpage.enter_post_description(data['test_description'])
    testpage.enter_post_content(data['test_content'])
    testpage.enter_img_path(getcwd() + data['test_img'])
    testpage.click_save_btn()
    time.sleep(data['sleep_time'])
    assert testpage.get_added_post_title() == data['test_title'], 'test3 failed'


def test_step4(browser):
    logging.info('Test4 Starting')
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    testpage.enter_contact_name(data['contact_name'])
    testpage.enter_contact_email(data['contact_email'])
    testpage.enter_contact_content(data['contact_content'])
    testpage.click_contact_us_btn()
    time.sleep(1)
    assert testpage.get_alert_text() == 'Form successfully submitted', 'test4 failed'
