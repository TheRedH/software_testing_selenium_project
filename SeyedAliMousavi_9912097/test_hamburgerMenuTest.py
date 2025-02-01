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

class TestHamburgerMenuTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_hamburgerMenuTest(self):
    self.driver.get("https://www.truecar.com/")
    self.driver.set_window_size(375, 667)
    self.driver.find_element(By.CSS_SELECTOR, ".h-5 > svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".border-b > .expandable-list-item:nth-child(1) .icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".border-b > .expandable-list-item:nth-child(2) .icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".border-b > .expandable-list-item:nth-child(3) .icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".border-b > .expandable-list-item:nth-child(3) .icon")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".border-b > .expandable-list-item:nth-child(4) .icon").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"modalCloseButton\"]").click()
    self.driver.close()