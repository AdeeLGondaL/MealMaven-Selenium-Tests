from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
import time
import unittest

class YourWebsiteTestSuite(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
#         self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def test_login_successful(self):
        # Open the login page
        self.driver.get("http://localhost:3000/UserLogin")

        # Find the email and password input fields and enter valid credentials
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")

        email_input.send_keys("ahmedadeel783@gmail.com")
        password_input.send_keys("Adeel123")

        # Find and click the login button
        login_button = self.driver.find_element(By.ID,"signin")
        login_button.click()

        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
        # Assert that the user is redirected to the UserHome page after successful login
        self.assertEqual(self.driver.current_url, "http://localhost:3000/UserHome")

    # def test_login_invalid_credentials(self):
    #     # Open the login page
    #     self.driver.get("http://localhost:3000/UserLogin")

    #     # Find the email and password input fields and enter invalid credentials
    #     email_input = self.driver.find_element(By.ID, "email")
    #     password_input = self.driver.find_element(By.ID, "password")

    #     email_input.send_keys("invalid_email@example.com")
    #     password_input.send_keys("invalid_password")

    #     # Find and click the login button
    #     login_button = self.driver.find_element(By.ID,"signin")
    #     login_button.click()
    #     # Wait for the login process to complete (you may need to adjust the sleep duration)
    #     time.sleep(2)

    #     try:
    #         # Check if an alert is present
    #         alert = self.driver.switch_to.alert
    #         alert_text = alert.text

    #         # Assert that the alert contains the expected message for invalid credentials
    #         self.assertTrue("Invalid Credentials" in alert_text)

    #     except UnexpectedAlertPresentException:
    #         # If no alert is present, find and check for an error message on the page
    #         error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
    #         self.assertEqual(error_message.text, "Invalid Credentials")

    #     finally:
    #         # Dismiss the alert
    #         self.driver.switch_to.alert.dismiss()

    # def test_login_invalid_credentials123(self):
    #     # Open the login page
    #     self.driver.get("http://localhost:3000/UserLogin")

    #     # Find the email and password input fields and enter invalid credentials
    #     email_input = self.driver.find_element(By.ID, "email")
    #     password_input = self.driver.find_element(By.ID, "password")

    #     email_input.send_keys("")
    #     password_input.send_keys("")

    #     # Find and click the login button
    #     login_button = self.driver.find_element(By.ID,"signin")
    #     login_button.click()

    #     # Wait for the login process to complete (you may need to adjust the sleep duration)
    #     time.sleep(2)

    #     try:
    #         # Check if an alert is present
    #         alert = self.driver.switch_to.alert
    #         alert_text = alert.text

    #         # Assert that the alert contains the expected message for invalid credentials
    #         self.assertTrue('Please enter both Email and Password!' in alert_text)

    #     except UnexpectedAlertPresentException:
    #         # If no alert is present, find and check for an error message on the page
    #         error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
    #         self.assertEqual(error_message.text, 'Please enter both Email and Password!')

    #     finally:
    #         # Dismiss the alert
    #         self.driver.switch_to.alert.dismiss()


    def tearDown(self):
        # Close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()