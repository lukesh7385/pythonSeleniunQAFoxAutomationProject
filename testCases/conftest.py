import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        serv_obj = Service("C:\\Program Files\\Drivers\\chromedriver-win64\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=serv_obj, options=options)
        driver.implicitly_wait(10)
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        serv_obj = Service("C:\\Program Files\\Drivers\\geckodriver-v0.34.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
        driver.implicitly_wait(10)
        print("Launching Firefox Browser")
    elif browser == 'edge':
        serv_obj = Service("C:\\Program Files\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=serv_obj, options=options)
        driver.implicitly_wait(10)
        print("Launching Edge Browser")
    else:
        serv_obj = Service("C:\\Program Files\\Drivers\\chromedriver-win64\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options, service=serv_obj)
        driver.implicitly_wait(10)
        print("Headless mode")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(params=[
    ("test101@credence.in", "Test@111", "Pass"),
    ("test1010@credence.in", "Test@111", "Fail"),
    ("test101@credence.in", "Test@1111", "Fail"),
    ("test1010@credence.in", "Test@1111", "Fail")
])
def data_for_login(request):
    return request.param


# # ########################### pyTest HTML Report ############################
#
# # Tt is a hook for Adding Environmental info to HTML Report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'QaFox.com'
#     config.metadata['Module Name'] = 'Customer'
#     config.metadata['tester'] = 'Lukesh Ade'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
