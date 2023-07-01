from selenium import webdriver
import pytest
from pageObject.LoginPage import LoginPage
from utilities.readProperties import RawConfig
from utilities.commonLogger import logGen
from time import sleep

class Test_001_Login:
    baseUrl = RawConfig.getApplicationUrl()
    email = RawConfig.getUsername()
    password = RawConfig.getPassword()

    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("************ Test_001_Login **************")
        self.logger.info("************ test_login **************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("************ test_login case passed **************")
        else:
            self.driver.save_screenshots(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("************ test_login case failed **************")
            assert False

    @pytest.mark.regression
    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        sleep(3)
        self.lp.clickLogout()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close() 
            self.logger.info("************ test_login case passed **************")

        else:
            self.driver.save_screenshots(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("************ test_logout case failed **************")
            assert False

            
        