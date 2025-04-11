from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig

class LoginPage:
    username_textbox_xpath = "//input[@placeholder='Username']"
    password_textbox_xpath = "//input[@placeholder='Password']"
    login_button_xpath = "//button[normalize-space()='Login']"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.username_textbox_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_textbox_xpath).send_keys(password)

    def click_on_login_button(self,):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()