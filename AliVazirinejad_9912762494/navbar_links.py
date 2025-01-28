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

    # Locate the navbar by a common selector (you may need to adjust this based on your HTML structure)
    links = driver.find_elements(By.CSS_SELECTOR, '#navbar ul li a')

    # Links text and expected URLs
    expected_links = {
        "خانه": '/',
        "ماشینها": '/cars/',
        "سرویسها": '/services/',
        "درباره": '/about/',
        "ارتباط با ما": '/contact/'
    }

    # Iterate through each link, click and validate the page URL
    for link in links:
        link_text = link.text.strip()  # Get link text and make it lowercase for comparison
        print(f"Testing link: {link_text}")
        
        if link_text in expected_links:
            expected_url = expected_links[link_text]
            try:
                link.click()
                time.sleep(2)  # Wait for page to load after click
                
                # Check if the current URL matches the expected URL
                current_url = driver.current_url
                assert current_url == f"{url}{expected_url}", f"Failed for {link_text}. Expected: {url}{expected_url}, Got: {current_url}"
                print(f"Link {link_text} passed!")
            except Exception as e:
                print(f"Test failed for {link_text}: {e}")
                continue

    # Close the browser after testing
    driver.quit()

# Run the test function
if __name__ == "__main__":
    test_navbar_links()
