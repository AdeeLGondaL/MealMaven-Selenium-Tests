import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from faker import Faker

class SignupTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver (Make sure the ChromeDriver executable is in your PATH)
        self.driver = webdriver.Chrome()
        self.fake = Faker()  # Initialize the Faker object

    def test_signup_successful(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys(fake_email)
        phone_input.send_keys("03094108357")
        password_input.send_keys(fake_password)
        cpassword_input.send_keys(fake_password)

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue("Registeration Successful" in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

        # Assert that the user is redirected to the UserLogin page after successful signup
        self.assertEqual(self.driver.current_url, "http://localhost:3000/UserLogin")

    def test_already_signedup(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys('ahmedadeel783@gmail.com')
        phone_input.send_keys("03094108357")
        password_input.send_keys(fake_password)
        cpassword_input.send_keys(fake_password)

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue("Registeration not successful" in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def test_empty_input_fields(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys('')
        phone_input.send_keys("03094108357")
        password_input.send_keys(fake_password)
        cpassword_input.send_keys(fake_password)

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue('Please fill all the fields!' in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def test_invalid_input_phoneNumber_length(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys(fake_email)
        phone_input.send_keys("0309410835")
        password_input.send_keys(fake_password)
        cpassword_input.send_keys(fake_password)

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue('Invalid Phone number lenght!' in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def test_invalid_input_name(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys("a")
        email_input.send_keys(fake_email)
        phone_input.send_keys("03094108357")
        password_input.send_keys(fake_password)
        cpassword_input.send_keys(fake_password)

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue('Name must have atleast 3 characters!' in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def test_invalid_input_password_length(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys(fake_email)
        phone_input.send_keys("03094108357")
        password_input.send_keys("abc")
        cpassword_input.send_keys("abc")

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue('Password must have atleast 8 characters!' in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def test_invalid_input_email(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@example.net'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys(fake_email)
        phone_input.send_keys("03094108357")
        password_input.send_keys(fake_password)
        cpassword_input.send_keys(fake_password)

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue('Invalid email address!' in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def test_invalid_input_password(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys(fake_email)
        phone_input.send_keys("03094108357")
        password_input.send_keys("testpassword123")
        cpassword_input.send_keys("testpassword123")

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue('Password must have atleast 1 uppercase letter!' in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def test_invalid_input_password_numeric_character(self):
        # Open the signup page
        self.driver.get("http://localhost:3000/UserSignup")

        # Generate random data using faker
        fake_name = self.fake.name()
        fake_email = self.fake.email().split('@')[0] + '@gmail.com'
        fake_phone = self.fake.phone_number()
        fake_password = self.fake.password()

        # Find the input fields and enter valid signup information
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        phone_input = self.driver.find_element(By.ID, "phone")
        password_input = self.driver.find_element(By.ID, "password")
        cpassword_input = self.driver.find_element(By.ID, "cpassword")

        name_input.send_keys(fake_name)
        email_input.send_keys(fake_email)
        phone_input.send_keys("03094108357")
        password_input.send_keys("TestPassword@")
        cpassword_input.send_keys("TestPassword@")

        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signup")
        signup_button.click()

        try:
            # Wait for the signup process to complete (you may need to adjust the sleep duration)
            time.sleep(2)

            # Check if an alert is present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Assert that the alert contains either the success or failure message
            self.assertTrue('Password must have atleast 1 numerical digit!' in alert_text)

            # Dismiss the alert
            alert.dismiss()

        except UnexpectedAlertPresentException:
            # If no alert is present, it means the redirect has occurred
            pass

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()