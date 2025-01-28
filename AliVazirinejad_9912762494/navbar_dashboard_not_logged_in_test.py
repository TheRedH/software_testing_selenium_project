from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up Firefox options
options = webdriver.FirefoxOptions()
options.headless = False  # Set to True to run Firefox in headless mode (no GUI)

# Initialize WebDriver
driver = webdriver.Firefox(options=options)

# Function to test the links in the navbar
def test_navbar_links():
    # Replace with the URL of your Django app's homepage
    url = 'http://localhost:8000'
    driver.get(url)

    # Wait for the page to load
    time.sleep(2)  # You can use WebDriverWait for more robust waiting

    expected_url = '/accounts/login'

    link = driver.find_element(By.CSS_SELECTOR, 'body > header.top-header.th-2.top-header-bg > div > div > div.col-lg-4.col-md-4.col-sm-5 > ul > li:nth-child(1) > a')

    try:
        # click on the link
        link.click()

        # wait for the page to load
        time.sleep(2)

        # grab the result page url
        current_url = driver.current_url

        # check if the result url is correct
        assert current_url == f"{url}{expected_url}", f"Failed. Expected: {url}{expected_url}, Got: {current_url}"
        print(f"Test Passed!")
    except Exception as e:
        print(f"Test failed for dashboard: {e}")

    # close the browser after testing
    driver.quit()


# Run the test function
if __name__ == "__main__":
    test_navbar_links()
