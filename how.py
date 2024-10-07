from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Path to your WebDriver (replace with the actual path to your chromedriver)"

# Set up WebDriver
service = Service()
driver = webdriver.Chrome(service=service)

# URL of the Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfs8XnsT4X5C_Sp8B4wcDYpH5TjKR0ufAL3cMCYbY8rV_hJBA/viewform"

# Open the form
driver.get(form_url)

# Infinite loop to keep submitting the form
while True:
    try:
        # Wait for the form to load
        time.sleep(2)

        # Fill in the first question (Kurz, Zechariah)
        first_question = driver.find_element(By.XPATH, '//input[@aria-label="First Question Label"]')
        first_question.clear()
        first_question.send_keys("Kurz, Zechariah")

        # Fill in the second question (kurz_zechariah@student.mahoningctc.com)
        second_question = driver.find_element(By.XPATH, '//input[@aria-label="Second Question Label"]')
        second_question.clear()
        second_question.send_keys("kurz_zechariah@student.mahoningctc.com")

        # Select the option for "Panther - Kurz"
        option = driver.find_element(By.XPATH, '//div[@aria-label="Panther - Kurz"]')
        option.click()

        # Submit the form
        submit_button = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]')
        submit_button.click()

        # Wait for the form to submit
        time.sleep(2)

        # Click the "Submit another response" link
        another_response = driver.find_element(By.XPATH, '//a[contains(text(), "Submit another response")]')
        another_response.click()

    except Exception as e:
        print(f"Error occurred: {e}")
        break

# Close the browser when finished
driver.quit()
