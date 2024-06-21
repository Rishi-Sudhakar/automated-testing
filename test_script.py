from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Path to chromedriver may vary based on your environment setup
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver-linux64', options=chrome_options)

# Example usage: navigate to a website and print title
driver.get("https://automated-testing.vercel.app/")
print("Page title:", driver.title)

# Remember to quit the browser session to release resources
driver.quit()
