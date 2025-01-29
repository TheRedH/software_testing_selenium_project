import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


CHROME_DRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"
CHROME_BINARY_PATH = "C:\\Program Files (x86)\\chrome-win64\\chrome.exe"


class CarSearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(CHROME_DRIVER_PATH)
        options = Options()
        options.binary_location = CHROME_BINARY_PATH
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get("http://127.0.0.1:8000/cars")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def wait_for_results(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "breadcrumb-areas"))
        )

    def test_search_car_asd(self):
        self.driver.get("http://127.0.0.1:8000/cars")

        search_box = self.driver.find_element(By.NAME, "keyword")
        search_box.send_keys("asd")
        search_box.submit()
        self.wait_for_results()

        results = self.driver.find_elements(By.CLASS_NAME, "car-box-3")
        self.assertEqual(
            len(results), 1, "One car has already been added with keyword 'asd'"
        )

    def test_search_car_lamborgini(self):
        self.driver.get("http://127.0.0.1:8000/cars")

        search_box = self.driver.find_element(By.NAME, "keyword")
        search_box.send_keys("lamborgini")
        search_box.submit()
        self.wait_for_results()

        results = self.driver.find_elements(By.CLASS_NAME, "car-box-3")
        self.assertEqual(
            len(results), 1, "One car has already been added with keyword 'lamborgini'"
        )

    def test_search_car_by_model(self):
        self.driver.get("http://127.0.0.1:8000/cars")
        model_dropdown = Select(self.driver.find_element(By.NAME, "model"))
        model_dropdown.select_by_visible_text("r8")
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-md")
        search_button.click()
        self.wait_for_results()

        results = self.driver.find_elements(By.CLASS_NAME, "car-box-3")
        self.assertEqual(len(results), 0, "No cars found with the model 'r8'")

    def test_search_car_by_price(self):

        min_price_slider = self.driver.find_elements(By.CLASS_NAME, "ui-slider-handle")[
            0
        ]
        max_price_slider = self.driver.find_elements(By.CLASS_NAME, "ui-slider-handle")[
            1
        ]

        # min_price_slider = self.driver.find_element(
        #     By.CLASS_NAME, "ui-slider-handle:nth-child(2)"
        # )
        # max_price_slider = self.driver.find_element(
        #     By.CLASS_NAME, "ui-slider-handle:nth-child(3)"
        # )

        # Move the sliders
        ActionChains(self.driver).drag_and_drop_by_offset(
            min_price_slider, 50, 0
        ).perform()
        ActionChains(self.driver).drag_and_drop_by_offset(
            max_price_slider, -50, 0
        ).perform()

        search_button = self.driver.find_element(By.CLASS_NAME, "btn-md")
        search_button.click()
        self.wait_for_results()

        results = self.driver.find_elements(By.CLASS_NAME, "car-box-3")
        self.assertEqual(
            len(results), 0, "No cars found within the specified price range"
        )

    def test_price_slider_lower_boundary(self):
        self.driver.get("http://127.0.0.1:8000/cars")
        min_price_slider = self.driver.find_elements(By.CLASS_NAME, "ui-slider-handle")[
            0
        ]
        min_val = self.driver.find_element(By.NAME, "min_price").get_attribute("value")
        ActionChains(self.driver).drag_and_drop_by_offset(
            min_price_slider, 10, 0
        ).perform()

        curr_val = self.driver.find_element(By.NAME, "min_price").get_attribute("value")

        self.assertGreater(curr_val, min_val, "max val decreases")

    def test_price_slider_upper_boundary(self):
        self.driver.get("http://127.0.0.1:8000/cars")
        max_val = self.driver.find_element(By.NAME, "max_price").get_attribute("value")
        max_price_slider = self.driver.find_elements(By.CLASS_NAME, "ui-slider-handle")[
            1
        ]

        ActionChains(self.driver).drag_and_drop_by_offset(
            max_price_slider, -10, 0
        ).perform()

        curr_val = self.driver.find_element(By.NAME, "max_price").get_attribute("value")

        self.assertLess(curr_val, max_val, "max val decreases")

    def test_search_car_by_city(self):

        city_dropdown = Select(self.driver.find_element(By.NAME, "city"))
        city_dropdown.select_by_visible_text("Mashhad")
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-md")
        search_button.click()
        self.wait_for_results()

        results = self.driver.find_elements(By.CLASS_NAME, "car-box-3")
        self.assertEqual(len(results), 0, "No cars found in the city 'Mashhad'")

    def test_price_slider_lower_not_exceed_upper(self):
        self.driver.get("http://127.0.0.1:8000/cars")
        min_price_slider = self.driver.find_elements(By.CLASS_NAME, "ui-slider-handle")[
            0
        ]
        max_price_slider = self.driver.find_elements(By.CLASS_NAME, "ui-slider-handle")[
            1
        ]

        ActionChains(self.driver).drag_and_drop_by_offset(
            min_price_slider, 200, 0
        ).perform()
        ActionChains(self.driver).drag_and_drop_by_offset(
            max_price_slider, -200, 0
        ).perform()

        min_price_value = self.driver.find_element(By.NAME, "min_price").get_attribute(
            "value"
        )
        max_price_value = self.driver.find_element(By.NAME, "max_price").get_attribute(
            "value"
        )

        # Assert that the lower boundary does not exceed the upper boundary
        self.assertEqual(
            min_price_value, max_price_value, "Lower boundary exceeds upper boundary"
        )

    def test_search_car_by_year(self):

        year_dropdown = Select(self.driver.find_element(By.NAME, "year"))
        year_dropdown.select_by_visible_text("2020")
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-md")
        search_button.click()
        self.wait_for_results()

        results = self.driver.find_elements(By.CLASS_NAME, "car-box-3")
        self.assertEqual(len(results), 0, "No cars found from the year '2020'")

    def test_search_car_by_body_style(self):

        body_style_dropdown = Select(self.driver.find_element(By.NAME, "body_style"))
        body_style_dropdown.select_by_visible_text("racing")
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-md")
        search_button.click()
        self.wait_for_results()

        results = self.driver.find_elements(By.CLASS_NAME, "car-box-3")
        self.assertEqual(len(results), 0, "No cars found with the body style 'racing'")


if __name__ == "__main__":
    unittest.main()
