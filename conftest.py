import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope='session')
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(testdata['implicitly_wait'])
    yield driver
    driver.quit()


# API
@pytest.fixture()
def login():
    response = requests.post(url=testdata['address'],
                             data={'username': testdata['username'], 'password': testdata['passwd']})
    return response.json()['token']


@pytest.fixture()
def not_my_post():
    return 'Test post'


@pytest.fixture()
def my_post():
    return 'Test post'
