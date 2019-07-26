from global_vars import url
from proj_setup.generic_decorators import singleton
from replib.config import Config
from replib.status import Status
from selenium import webdriver


class Base:

    @singleton
    def browser_inst(self):
        driver = webdriver.Chrome(executable_path="./drivers_files/chromedriver")
        return driver

    @singleton
    def report_inst(self):
        report = Status(Config.Script_version)
        return report

    def navigate_to_url(self):
        self.browser_inst().get(url)


class Clear:

    def clear_session(self):
        Base().report_inst().report_end()
        Base().browser_inst().close()
        Base().browser_inst().quit()
