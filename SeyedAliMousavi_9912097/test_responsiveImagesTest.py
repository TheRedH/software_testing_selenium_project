import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestResponsiveImagesTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_responsiveImagesTest(self):
    self.driver.get("https://www.truecar.com/")
    self.driver.set_window_size(375, 667)
    self.driver.execute_script("window.scrollTo(0,50)")
    self.driver.set_window_size(375, 1150)
    self.driver.execute_script("window.scrollTo(0,50)")
    self.driver.set_window_size(800, 667)
    self.driver.execute_script("window.scrollTo(0,50)")
    self.driver.close()