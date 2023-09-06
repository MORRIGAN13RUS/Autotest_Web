import logging
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru/gateway'

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        except:
            logging.exception('Find element exception')
            element = None
        return element

    def get_element_property(self, locator, el_property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(el_property)
        logging.error(f'Property {el_property} not found in element with locator {locator}')
        return None

    @property
    def go_to_site(self):
        try:
            start_browser = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browser = None
        return start_browser

    def get_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None


class BaseAPI:
    def __init__(self, address, username, password):
        self.address = address
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        response = self.session.post(url=self.address, data={'username': self.username, 'password': self.password})
        return response.json()['token']

    def get_token(self):
        try:
            token = self.login()
        except:
            token = None
            logging.exception(f'Token for {self.username} auth not get')
        return token

    def get_my_posts(self, address_posts):
        logging.info('Getting titles of my posts')
        token = self.get_token()
        try:
            data = self.session.get(url=address_posts, headers={'X-Auth-Token': token}).json()['data']
            titles = [i['title'] for i in data]
        except:
            titles = []
            logging.exception('Log In error')
        return titles

    def get_other_posts(self, address_posts):
        logging.info('Getting titles of not my posts')
        token = self.get_token()
        try:
            data = self.session.get(url=address_posts,
                                    headers={'X-Auth-Token': token},
                                    params={'owner': 'notMe'}).json()['data']
            titles = [i['title'] for i in data]
        except KeyError:
            titles = []
            logging.exception('Auth error')
        return titles

    def new_post(self, address_posts, title, description, content):
        logging.info('Creating a new post')
        token = self.get_token()
        try:
            self.session.post(url=address_posts,
                              headers={'X-Auth-Token': token},
                              data={'title': title, 'description': description, 'content': content})
            posts_info = self.session.get(url=address_posts,
                                          headers={'X-Auth-Token': token}).json()['data']
            descriptions = [i['description'] for i in posts_info]
        except:
            descriptions = []
            logging.exception('Log In error')
        return descriptions
