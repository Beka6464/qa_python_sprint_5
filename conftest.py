import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service('/Users/a1/PycharmProject/qa_pythton_sprint_5/chromedriver')
    chrome = webdriver.Chrome(service=service)
    yield chrome
    chrome.quit()
