import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
import time


class Test001Login:
    baseurl = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickloginbutton()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True

        else:
            assert False
