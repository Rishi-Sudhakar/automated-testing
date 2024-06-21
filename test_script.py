from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver (make sure ChromeDriver is in your PATH)
driver = webdriver.Chrome()

try:
    # Navigate to the deployed webpage URL
    driver.get("https://automated-testing.vercel.app/")

    # Perform actions
    name_input = driver.find_element_by_id("name")
    name_input.send_keys("John Doe")

    email_input = driver.find_element_by_id("email")
    email_input.send_keys("john.doe@example.com")

    submit_button = driver.find_element_by_xpath("//input[@type='submit']")
    submit_button.click()

    time.sleep(2)  # Add a delay to see the result

    # Assert expected results
    assert "Submitted" in driver.page_source

    print("Test passed!")

finally:
    # Close the browser
    driver.quit()
