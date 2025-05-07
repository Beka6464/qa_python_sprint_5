import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    yield chrome
    chrome.quit()
