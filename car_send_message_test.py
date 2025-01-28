from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Firefox options
options = webdriver.FirefoxOptions()
options.headless = False  # Set to True to run Firefox in headless mode (no GUI)

# Initialize WebDriver
driver = webdriver.Firefox(options=options)

# Function to test the links in the navbar
def test_navbar_links():
    # Replace with the URL of your Django app's homepage
    url = 'http://localhost:8000/cars/1'
    
    driver.get(url)

    # Wait for the page to load
    time.sleep(2)  # You can use WebDriverWait for more robust waiting

    # grabbing the link element
    button = driver.find_element(By.CSS_SELECTOR, 'body > div.car-details-page.content-area-6 > div > div > div.col-lg-4.col-md-12 > div > div.widget.advanced-search.d-none-992 > button')

    try:
        # click on the link
        button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#inquiryModal > div > div'))
        )
        print("Test Passed: modal works")
    except Exception as e:
        print(f"Test failed")


    # close the browser after testing
    driver.quit()


# Run the test function
if __name__ == "__main__":
    test_navbar_links()
