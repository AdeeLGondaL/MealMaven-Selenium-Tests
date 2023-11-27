from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
import time
import unittest

import test

class UserDietPlanTest(test.YourWebsiteTestSuite):

    def setUp(self):
        # Set up the WebDriver
#         self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def test_daily_activity_successful(self):
        # Open the login page

        self.test_login_successful()
        self.driver.get("http://localhost:3000/UserDietPlan")
        # Find the email and password input fields and enter valid credentials
        email = self.driver.find_element(By.NAME, "email")
        height = self.driver.find_element(By.NAME, "height")
        weight = self.driver.find_element(By.NAME, "weight")
        age = self.driver.find_element(By.NAME, "age")
        prefer = self.driver.find_element(By.NAME, "prefer")
        avoid = self.driver.find_element(By.NAME, "avoid")
        goal = self.driver.find_element(By.NAME, "goal")

        email.send_keys("abc5@gmail.com")
        height.send_keys(50)
        weight.send_keys(50)
        age.send_keys(20)
        prefer.send_keys('eggs')
        avoid.send_keys('protein')
        goal.send_keys('Weight decrease')

        # Find and click the login button
        button = self.driver.find_element(By.ID,"submitDietButton")
        button.click()

        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
        # Assert that the user is redirected to the UserHome page after successful login
        self.assertEqual(self.driver.current_url, "http://localhost:3000/UserDietPlan")   

    # def test_daily_activity_Invalid_1(self):
    #     # Open the login page

    #     self.test_login_successful()
    #     self.driver.get("http://localhost:3000/UserDietPlan")
    #     # Find the email and password input fields and enter valid credentials
    #     email = self.driver.find_element(By.NAME, "email")
    #     height = self.driver.find_element(By.NAME, "height")
    #     weight = self.driver.find_element(By.NAME, "weight")
    #     age = self.driver.find_element(By.NAME, "age")
    #     prefer = self.driver.find_element(By.NAME, "prefer")
    #     avoid = self.driver.find_element(By.NAME, "avoid")
    #     goal = self.driver.find_element(By.NAME, "goal")

    #     email.send_keys("abc4gmail.com")
    #     height.send_keys(50)
    #     weight.send_keys(50)
    #     age.send_keys(20)
    #     prefer.send_keys('eggs')
    #     avoid.send_keys('protein')
    #     goal.send_keys('Weight decrease')

    #     # Find and click the login button
    #     button = self.driver.find_element(By.ID,"submitDietButton")
    #     button.click()

    #     # Wait for the login process to complete (you may need to adjust the sleep duration)
    #     time.sleep(2)

    #     try:
    #         # Check if an alert is present
    #         # alert = self.driver.switch_to.alert
    #         alert = self.driver.switch_to.active_element.find_elements(By.NAME,"email")
    #         # alert_text = alert.text

    #         # Assert that the alert contains the expected message for invalid credentials
    #         self.assertTrue("email" in alert)

    #     except UnexpectedAlertPresentException:
    #         # If no alert is present, find and check for an error message on the page
    #         error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
    #         self.assertEqual(error_message.text, "Please enter an email adress.")

    #     finally:
    #         # Dismiss the alert
    #         self.driver.switch_to.alert.dismiss()

    def test_daily_activity_Invalid_2(self):
        # Open the login page

        self.test_login_successful()
        self.driver.get("http://localhost:3000/UserDietPlan")
        # Find the email and password input fields and enter valid credentials
        email = self.driver.find_element(By.NAME, "email")
        height = self.driver.find_element(By.NAME, "height")
        weight = self.driver.find_element(By.NAME, "weight")
        age = self.driver.find_element(By.NAME, "age")
        prefer = self.driver.find_element(By.NAME, "prefer")
        avoid = self.driver.find_element(By.NAME, "avoid")
        goal = self.driver.find_element(By.NAME, "goal")

        email.send_keys("abc6@gmail.com")
        height.send_keys(0)
        weight.send_keys(50)
        age.send_keys(20)
        prefer.send_keys('eggs')
        avoid.send_keys('protein')
        goal.send_keys('Weight decrease')

        # Find and click the login button
        button = self.driver.find_element(By.ID,"submitDietButton")
        button.click()

        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)

        try:
            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains the expected message for invalid credentials
            self.assertTrue("Invalid BMI values!" in alert_text)

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            self.assertEqual(error_message.text, "Invalid BMI values!")

        finally:
            # Dismiss the alert
            self.driver.switch_to.alert.dismiss()

    def test_daily_activity_Invalid_3(self):
        # Open the login page

        self.test_login_successful()
        self.driver.get("http://localhost:3000/UserDietPlan")
        # Find the email and password input fields and enter valid credentials
        email = self.driver.find_element(By.NAME, "email")
        height = self.driver.find_element(By.NAME, "height")
        weight = self.driver.find_element(By.NAME, "weight")
        age = self.driver.find_element(By.NAME, "age")
        prefer = self.driver.find_element(By.NAME, "prefer")
        avoid = self.driver.find_element(By.NAME, "avoid")
        goal = self.driver.find_element(By.NAME, "goal")

        email.send_keys("abc6@gmail.com")
        height.send_keys(50)
        weight.send_keys(0)
        age.send_keys(20)
        prefer.send_keys('eggs')
        avoid.send_keys('protein')
        goal.send_keys('Weight decrease')

        # Find and click the login button
        button = self.driver.find_element(By.ID,"submitDietButton")
        button.click()

        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)

        try:
            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains the expected message for invalid credentials
            self.assertTrue("Invalid BMI values!" in alert_text)

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            self.assertEqual(error_message.text, "Invalid BMI values!")

        finally:
            # Dismiss the alert
            self.driver.switch_to.alert.dismiss()            

    def test_daily_activity_Invalid_4(self):
        # Open the login page

        self.test_login_successful()
        self.driver.get("http://localhost:3000/UserDietPlan")
        # Find the email and password input fields and enter valid credentials
        email = self.driver.find_element(By.NAME, "email")
        height = self.driver.find_element(By.NAME, "height")
        weight = self.driver.find_element(By.NAME, "weight")
        age = self.driver.find_element(By.NAME, "age")
        prefer = self.driver.find_element(By.NAME, "prefer")
        avoid = self.driver.find_element(By.NAME, "avoid")
        goal = self.driver.find_element(By.NAME, "goal")

        email.send_keys("abc6@gmail.com")
        height.send_keys(50)
        weight.send_keys(50)
        age.send_keys(0)
        prefer.send_keys('eggs')
        avoid.send_keys('protein')
        goal.send_keys('Weight decrease')

        # Find and click the login button
        button = self.driver.find_element(By.ID,"submitDietButton")
        button.click()

        # Wait for the login process to complete (you may need to adjust the sleep duration)
        time.sleep(2)

        try:
            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains the expected message for invalid credentials
            self.assertTrue("Invalid BMI values!" in alert_text)

        except UnexpectedAlertPresentException:
            # If no alert is present, find and check for an error message on the page
            error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
            self.assertEqual(error_message.text, "Invalid BMI values!")

        finally:
            # Dismiss the alert
            self.driver.switch_to.alert.dismiss()            

    # def test_daily_activity_Invalid_5(self):
    #     # Open the login page

    #     self.test_login_successful()
    #     self.driver.get("http://localhost:3000/UserDietPlan")
    #     # Find the email and password input fields and enter valid credentials
    #     email = self.driver.find_element(By.NAME, "email")
    #     height = self.driver.find_element(By.NAME, "height")
    #     weight = self.driver.find_element(By.NAME, "weight")
    #     age = self.driver.find_element(By.NAME, "age")
    #     prefer = self.driver.find_element(By.NAME, "prefer")
    #     avoid = self.driver.find_element(By.NAME, "avoid")
    #     goal = self.driver.find_element(By.NAME, "goal")

    #     email.send_keys("abc6@gmail.com")
    #     height.send_keys(50)
    #     weight.send_keys(50)
    #     age.send_keys(50)
    #     prefer.send_keys('eggs')
    #     avoid.send_keys('protein')
    #     goal.send_keys('')

    #     # Find and click the login button
    #     button = self.driver.find_element(By.ID,"submitDietButton")
    #     button.click()

    #     # Wait for the login process to complete (you may need to adjust the sleep duration)
    #     time.sleep(2)

    #     try:
    #         # Check if an alert is present
    #         alert = self.driver.switch_to.alert
    #         alert_text = alert.text

    #         # Assert that the alert contains the expected message for invalid credentials
    #         self.assertTrue("Please select an item in the list." in alert_text)

    #     except UnexpectedAlertPresentException:
    #         # If no alert is present, find and check for an error message on the page
    #         error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
    #         self.assertEqual(error_message.text, "Please select an item in the list.")

    #     finally:
    #         # Dismiss the alert
    #         self.driver.switch_to.alert.dismiss()   

    def tearDown(self):
        # Close the browser window
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main()
