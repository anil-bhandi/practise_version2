import pytest
from selenium import webdriver
from utilities.readProperties import RawConfig
from utilities.commonLogger import logGen
from pageObject.LoginPage import LoginPage
from utilities import XlUtilities
from time import sleep

class Test_002_LoginDDT:
    url = RawConfig.getApplicationUrl()
    xlPath = RawConfig.getXlPath()

    logger = logGen.loggen()

    def test_loginDTT(self, setup):
        self.logger.info("********************* Test_002_LoginDDT **********************")
        self.logger.info("********************* test_loginDTT **********************")
        
        self.driver = setup
        self.driver.get(self.url)

        self.lp = LoginPage(self.driver)

        self.rows = XlUtilities.getRowCount(self.xlPath, 'Sheet1')
        
        lst_status = []
        
        for r in range (2, self.rows):
            self.username = XlUtilities.readData(self.xlPath, 'Sheet1', rownum= self.rows, colnum= 1)
            self.password = XlUtilities.readData(self.xlPath, 'Sheet1', rownum= self.rows, colnum= 2)
            self.exp = XlUtilities.readData(self.xlPath, 'Sheet1', rownum= self.rows, colnum= 3)
            self.lp.enterUsername(self.username)
            self.lp.enterPassword(self.password)
            self.lp.clickLoginButton()
            sleep(3)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** passed *****************")
                    self.lp.clickLogout()
                    sleep(5)
                    lst_status.append("Pass")
                    
                elif self.exp == "Fail":
                    self.logger.info("*************** failed *****************")
                    
            
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** failed *****************")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("*************** Login DDT test passed *****************")   
                assert True
            else:
                self.logger.info("*************** Login DDT test failed *****************")   
                assert False
        self.driver.close()
        self.logger.info("*************** End of Login ddt test *****************")
        self.logger.info("*************** Completed Test_002_Login  *****************")
