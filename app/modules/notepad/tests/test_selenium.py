import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCreatenotepad():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createnotepad(self):
    self.driver.get("http://localhost:5000/login")
    time.sleep(2)
    self.driver.set_window_size(912, 1011)
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    self.driver.get("http://localhost:5000/notepad/create")
    time.sleep(2)
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("n1")
    self.driver.find_element(By.ID, "body").click()
    self.driver.find_element(By.ID, "body").send_keys("n1")
    self.driver.find_element(By.ID, "submit").click()
