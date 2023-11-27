from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
import time
import unittest

import test

class DailyActivityTest(test.YourWebsiteTestSuite):

    def setUp(self):
        # Set up the WebDriver
#         self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def test_daily_activity_successful(self):
        # Open the login page

        self.test_login_successful()
        self.driver.get("http://localhost:3000/DailyActivity")
        # Find the email and password input fields and enter valid credentials
        big_text_box_input = self.driver.find_element(By.ID, "big-textbox")
        small_text_box_input = self.driver.find_element(By.ID, "small-textbox")

        big_text_box_input.send_keys("600gm")
        small_text_box_input.send_keys("300")

        # Find and click the login button
        login_button = self.driver.find_element(By.ID,"daily_activity_button")
        login_button.click()

        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
        # Assert that the user is redirected to the UserHome page after successful login
        # self.assertEqual(self.driver.current_url, "http://localhost:3000/UserHome")

    def test_daily_activity_invalid_credentials_1(self):
        # Open the login page
        self.test_login_successful()
        self.driver.get("http://localhost:3000/DailyActivity")

        # Find the email and password input fields and enter invalid credentials
        big_text_box_input = self.driver.find_element(By.ID, "big-textbox")
        small_text_box_input = self.driver.find_element(By.ID, "small-textbox")

        big_text_box_input.send_keys("")
        small_text_box_input.send_keys("300")

        # Find and click the login button
        login_button = self.driver.find_element(By.ID,"daily_activity_button")
        login_button.click()
        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)

        try:
            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains the expected message for invalid credentials
            self.assertTrue("Please enter all fields!" in alert_text)

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            self.assertEqual(error_message.text, "Please enter all fields!")

        finally:
            # Dismiss the alert
            self.driver.switch_to.alert.dismiss()

    def test_daily_activity_invalid_credentials_2(self):
        # Open the login page
        self.test_login_successful()
        self.driver.get("http://localhost:3000/DailyActivity")

        # Find the email and password input fields and enter invalid credentials
        big_text_box_input = self.driver.find_element(By.ID, "big-textbox")
        small_text_box_input = self.driver.find_element(By.ID, "small-textbox")

        big_text_box_input.send_keys("400")
        small_text_box_input.send_keys("")

        # Find and click the login button
        login_button = self.driver.find_element(By.ID,"daily_activity_button")
        login_button.click()
        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)

        try:
            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains the expected message for invalid credentials
            self.assertTrue("Please enter all fields!" in alert_text)

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            self.assertEqual(error_message.text, "Please enter all fields!")

        finally:
            # Dismiss the alert
            self.driver.switch_to.alert.dismiss()    

    def test_daily_activity_invalid_credentials_3(self):
        # Open the login page
        self.test_login_successful()
        self.driver.get("http://localhost:3000/DailyActivity")

        # Find the email and password input fields and enter invalid credentials
        big_text_box_input = self.driver.find_element(By.ID, "big-textbox")
        small_text_box_input = self.driver.find_element(By.ID, "small-textbox")

        big_text_box_input.send_keys("")
        small_text_box_input.send_keys("")

        # Find and click the login button
        login_button = self.driver.find_element(By.ID,"daily_activity_button")
        login_button.click()
        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)

        try:
            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains the expected message for invalid credentials
            self.assertTrue("Please enter all fields!" in alert_text)

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            self.assertEqual(error_message.text, "Please enter all fields!")

        finally:
            # Dismiss the alert
            self.driver.switch_to.alert.dismiss()    


    def tearDown(self):
        # Close the browser window
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main()
