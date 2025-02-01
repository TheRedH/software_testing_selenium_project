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

class TestHorizontalScrollTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_horizontalScrollTest(self):
    self.driver.get("https://www.truecar.com/")
    self.driver.set_window_size(320, 568)
    self.driver.execute_script("window.scrollTo(100,0)")
    self.driver.execute_script("window.scrollTo(200,0)")
    self.driver.close()