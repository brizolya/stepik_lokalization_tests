import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = str(request.config.getoption("--language"))

    print(f"\nstart browser at {language}-language for test..")
    
    options = Options()
    #options.add_argument("-lang="+ language)
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    #print(options.arguments)
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()