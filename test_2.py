import logging
import yaml
from BaseApp import BaseAPI

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    username = testdata['username']
    password = testdata['password']
    address = testdata['address']
    address_posts = testdata['address_posts']
    title = testdata['test_title']
    description = testdata['test_description']
    content = testdata['test_content']
    my_post_title = testdata['my_post_title']
    not_my_post_title = testdata['not_my_post_title']


def test_api_step1():
    # Test my title
    logging.info('Test1 API starting')
    session = BaseAPI(address, username, password)
    posts = session.get_my_posts(address_posts)
    assert my_post_title in posts, 'Test1 API failed'


def test_api_step2():
    # Test not my title
    logging.info('Test2 API starting')
    session = BaseAPI(address, username, password)
    posts = session.get_other_posts(address_posts)
    assert not_my_post_title in posts, 'Test2 API failed'


def test_api_step3():
    # Test create new post
    logging.info('Test3 API starting')
    session = BaseAPI(address, username, password)
    new_post = session.new_post(address_posts, title, description, content)
    assert description in new_post, 'Test3 API failed'