from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
import time
import unittest

import test

class LogoutTest(test.YourWebsiteTestSuite):

    def setUp(self):
        # Set up the WebDriver
#         self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def test_Logout(self):
        # Open the login page

        self.test_login_successful()
        self.driver.get("http://localhost:3000/UserHome")
        # Find the email and password input fields and enter valid credentials

        button = self.driver.find_element(By.ID,"Logout")
        button.click()
        time.sleep(2)

        try:
            self.assertEqual(self.driver.current_url, "http://localhost:3000/UserLogin")

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            print(error_message)


    
  
  

    def tearDown(self):
        # Close the browser window
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main()
