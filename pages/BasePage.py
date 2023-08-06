import datetime

from common import common


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.delay = 15
        self.delimiter = 60  # delimiter = products on grid
        self.LOGIN_ENV, self.PASSWD_ENV = ' '.join(list(common.get_creds())).split()

    def open(self):
        self.browser.get(self.url)

