class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        _ = self.driver.find_element(value=self.textbox_username_id).clear()
        self.driver.find_element(value=self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        _ = self.driver.find_element(value=self.textbox_password_id).clear()
        self.driver.find_element(value=self.textbox_password_id).send_keys(password)

    def clickloginbutton(self):
        _ = self.driver.find_element(by='xpath', value=self.button_login_xpath).click()

    def clicklogout(self):
        _ = self.driver.find_element(by='link text', value=self.link_logout_linktext).click()
