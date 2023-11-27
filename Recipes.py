from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
import time
import unittest

import test

class RecipesTest(test.YourWebsiteTestSuite):

    def setUp(self):
        # Set up the WebDriver
#         self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def test_Sugar_Free_valid(self):
        # Open the login page

        self.test_login_successful()
        self.driver.get("http://localhost:3000/SugarFreeRecipe")
        # Find the email and password input fields and enter valid credentials
        time.sleep(2)
        try:
            self.assertEqual(self.driver.current_url, "http://localhost:3000/SugarFreeRecipe")

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            print(error_message)


    def test_StarchFreeRecipe(self):
        # Open the login page
        self.test_login_successful()
        self.driver.get("http://localhost:3000/StarchFreeRecipe")

        # Find the email and password input fields and enter invalid credentials
  

        # Find and click the login button

        time.sleep(2)
        try:
            self.assertEqual(self.driver.current_url, "http://localhost:3000/StarchFreeRecipe")

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            print(error_message)

    def test_ProteinRecipe(self):
        # Open the login page
        self.test_login_successful()
        self.driver.get("http://localhost:3000/ProteinRecipe")

        # Find the email and password input fields and enter invalid credentials
  

        # Find and click the login button

        time.sleep(2)
        try:
            self.assertEqual(self.driver.current_url, "http://localhost:3000/ProteinRecipe")

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            print(error_message)

    def test_DairyRecipe(self):
        # Open the login page
        self.test_login_successful()
        self.driver.get("http://localhost:3000/DairyRecipe")

        # Find the email and password input fields and enter invalid credentials
  

        # Find and click the login button

        time.sleep(2)
        try:
            self.assertEqual(self.driver.current_url, "http://localhost:3000/DairyRecipe")

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            print(error_message)


    def test_CarbFreeRecipe(self):
        # Open the login page
        self.test_login_successful()
        self.driver.get("http://localhost:3000/CarbFreeRecipe")

        # Find the email and password input fields and enter invalid credentials
  

        # Find and click the login button

        time.sleep(2)
        try:
            self.assertEqual(self.driver.current_url, "http://localhost:3000/CarbFreeRecipe")

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            print(error_message)

  
  

    def tearDown(self):
        # Close the browser window
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main()
