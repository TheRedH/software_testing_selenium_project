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

    # test home page link
    link_text = 'ماشینها'
    expected_url = '/cars/'

    # grabbing the link element
    links = driver.find_elements(By.CSS_SELECTOR, '#navbar ul li a')
    target_link = None
    found_target_link = False
    for link in links:
        if link.text.strip() == link_text:
            found_target_link = True
            target_link = link
            break
            
    if not found_target_link:
        print(f"Test failed for {link_text}")

    else:
        try:
            # start the test
            print(f"Testing link: {link_text}")

            # click on the link
            target_link.click()

            # wait for the page to load
            time.sleep(2)

            # grab the result page url
            current_url = driver.current_url

            # check if the result url is correct
            assert current_url == f"{url}{expected_url}", f"Failed for {link_text}. Expected: {url}{expected_url}, Got: {current_url}"
            print(f"Link {link_text} passed!")
        except Exception as e:
            print(f"Test failed for {link_text}: {e}")

    # close the browser after testing
    driver.quit()


# Run the test function
if __name__ == "__main__":
    test_navbar_links()
