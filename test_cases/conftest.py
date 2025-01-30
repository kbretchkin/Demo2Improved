import pytest
from pytest_metadata.hooks import pytest_metadata
from selenium import webdriver

#  Importing metadata_key module
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser",action = "store",default="chrome",
        help="Specify the browser: chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError ("Unsupported browser")
    return driver

################################ Add/Remove some parameters to HTML report ###################
# hooks for adding environment info to HTML report ###################
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, Demo2Improved'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'KB'

# hooks for delete/modify environment info to HTML report ###################
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)