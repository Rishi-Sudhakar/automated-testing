from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Initialize ChromeDriver without specifying executable_path
driver = webdriver.Chrome(options=chrome_options)

# Example usage: navigate to a website and print title
driver.get("https://automated-testing.vercel.app/")
print("Page title:", driver.title)

# Remember to quit the browser session to release resources
driver.quit()
