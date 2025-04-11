from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time
import pytest


class Test001Login:
    baseUrl = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_homepagetitle(self, setup):
        self.logger.info("***** Test001Login *****")
        self.logger.info("***** HomePage Title Testing *****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)

        try:
            act_title = self.driver.title
            if act_title == "OrangeHRM":
                self.logger.info("*** Home page title passed *****")
                assert True
            else:
                screenshot_path = ".//Screenshots/test_homepage_title.png"
                self.driver.save_screenshot(screenshot_path)
                self.logger.error(f"**** Homepage test failed. Screenshot saved at {screenshot_path} ****")
                assert False
        finally:
            self.driver.quit()

    def test_login(self, setup):
        self.logger.info("***** Test001Login - Login Test *****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_on_login_button()

        try:
            actual_title = self.driver.title
            if actual_title == "OrangeHRM":
                self.logger.info("*** Login successful, test passed *****")
                assert True
            else:
                time.sleep(2)  # Reduced sleep time
                screenshot_path = ".//Screenshots/test_login.png"
                self.driver.save_screenshot(screenshot_path)
                self.logger.error(f"**** Login test failed. Screenshot saved at {screenshot_path} ****")
                assert False
        finally:
            self.driver.quit()
