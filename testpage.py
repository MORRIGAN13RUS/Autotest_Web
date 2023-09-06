import logging
import yaml
import requests
from selenium.webdriver.common.by import By
from BaseApp import BasePage


class TestSearchLocators:
    ibs = {}
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['XPATH'].keys():
        ibs[locator] = (By.XPATH, locators['XPATH'][locator])
    for locator in locators['CSS_SELECTOR'].keys():
        ibs[locator] = (By.CSS_SELECTOR, locators['CSS_SELECTOR'][locator])
    for locator in locators['ID'].keys():
        ibs[locator] = (By.ID, locators['ID'][locator])


class OperationsHelper(BasePage):
    with open('testdata.yaml') as f:
        testdata = yaml.safe_load(f)

    # enter text
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element with locator {locator} not found')
            return False
        try:
            logging.debug(f'Send "{word}" in element {element_name}')
            field.clear()
            field.send_keys(word)

        except TypeError:
            logging.exception(f'Exception while operation with locator {locator}')
            return False
        return True

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_LOGIN_FIELD'], word, 'user login field')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_PASS_FIELD'], word, 'user password field')

    def enter_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_POST_TITLE'], word, 'post title')

    def enter_post_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_POST_DESCRIPTION'], word, 'post description')

    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_POST_CONTENT'], word, 'post content')

    def enter_img_path(self, path):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_POST_IMG'], path, 'post image')

    def enter_contact_name(self, contact_name):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_INPUT_YOUR_NAME'], contact_name, 'contact name field')

    def enter_contact_email(self, contact_email):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_INPUT_YOUR_EMAIL'], contact_email, 'contact email field')

    def enter_contact_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ibs['LOCATOR_INPUT_CONTENT'], content, 'content field')

    # click
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False
        logging.debug(f'Clicked {element_name}')
        return True

    def click_login_button(self):
        self.click_button(TestSearchLocators.ibs['LOCATOR_LOGIN_BTN'], 'Clicked login button')

    def click_create_post_btn(self):
        self.click_button(TestSearchLocators.ibs['LOCATOR_CREATE_POST_BTN'], 'Clicked create new post button')

    def click_save_btn(self):
        self.click_button(TestSearchLocators.ibs['LOCATOR_SAVE_BTN'], 'Clicked save post button')

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ibs['LOCATOR_CONTACT_LINK'], 'Clicked Contact link')

    def click_contact_us_btn(self):
        self.click_button(TestSearchLocators.ibs['LOCATOR_CONTACT_US_BTN'], 'Clicked contact us button')

    # get
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'Find text in {element_name}')
        return text

    def get_error_text(self):
        text = self.get_text_from_element(TestSearchLocators.ibs['LOCATOR_ERROR_FIELD'], 'Error')
        return text

    def get_login_text(self):
        text = self.get_text_from_element(TestSearchLocators.ibs['LOCATOR_HELLO_LOGIN'], 'Log In')
        return text

    def get_added_post_title(self):
        title = self.get_text_from_element(TestSearchLocators.ibs['LOCATOR_POST_ADDED'], 'Post added')
        return title

    def get_alert_text(self):
        logging.info('Get alert text')
        text = self.get_alert()
        logging.info(f'Got alert {text}')
        return text
