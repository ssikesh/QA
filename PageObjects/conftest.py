import pytest
from selenium import webdriver

def pytest_addoption(parser):
    """Add browser command-line option for pytest"""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture
def browser(request):
    """Get the browser from command-line option"""
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    """Setup WebDriver based on the selected browser"""
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver  # Ensures the browser quits after tests
    driver.quit()


# Hook to get the browser option from the command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


############## GENERATION OF HTML REPORT ###########

@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "Selenium Mangsir Group Test Report"


######## Hook to add environment info and custom metadata to the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        extras.html("<p><strong>Project Name:</strong> Automation Testing </p>"),
        extras.html("<p><strong>Module Name:</strong> LoginTest</p>"),
        extras.html("<p><strong>QA:</strong> Bikesh</p>")
    ])


# Hook to add custom metadata
def pytest_configure(config):
    config._metadata['Project Name'] = 'Automation Testing'
    config._metadata['Module Name'] = 'Login Test'
    config._metadata['QA'] = 'Bikesh'
