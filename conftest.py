import pytest

import undetected_chromedriver as uc
from selenium import webdriver as wd


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://rozetka.com.ua", help="select your required URL")
    # parser.addoption("--user-data-dir", action="store", default="C:\\chromedriver\\localhost\\Default\\",
    #                  help="Path to user data directory")
    # parser.addoption("--profile-directory", action="store", default="C:\\Users\\Evgeny\\AppData\\Local\\Google\\Chrome"
    #                                                                 "\\User", help="Path to user data directory")
    # parser.addoption("--headless", action="store", default=True, help="Headless mode if supplied.")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def browser(request):
    options = uc.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument('--user-data-dir=C:\\Users\\Evgeny\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    # options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    print("\nStart work browser")
    if browser == "chrome":
        driver = uc.Chrome(options=options)
        driver.maximize_window()
    elif browser == "firefox":
        driver = wd.Firefox()
    elif browser == "safari":
        driver = wd.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.get(url)
    yield driver
    print("\nEnd work browser")
    driver.close()


@pytest.fixture(scope="function")
def browser_chrome(request):
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    print("\nStart work browser")
    if browser == "chrome":
        driver = wd.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver = wd.Firefox()
    elif browser == "safari":
        driver = wd.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.get(url)
    yield driver
    print("\nEnd work browser")
    driver.close()
