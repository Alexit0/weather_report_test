import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="firefox",
        choices=("chrome", "firefox", "edge")
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()

    driver.get("https://www.accuweather.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()

