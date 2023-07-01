from selenium import webdriver
from selenium.webdriver.common.by import By


class   LoginPage:

    textBox_email_id = "Email"
    textBox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    checkBox_rememberMe_id = "RememberMe"
    link_logout_linkText = "Logout"

    def __init__(self,driver):
        self.driver = driver
    
    def enterUsername(self, username):
        self.driver.find_element(By.ID,self.textBox_email_id).clear()
        self.driver.find_element(By.ID,self.textBox_email_id).send_keys(username)
    
    def enterPassword(self,password):
        self.driver.find_element(By.ID,self.textBox_password_id).clear()
        self.driver.find_element(By.ID,self.textBox_password_id).send_keys(password)
    
    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickRememberMe(self):
        self.driver.find_element(By.ID,self.checkBox_rememberMe_id).click()
    
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linkText).click()

    
