# Generated by Selenium IDE
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
from webdriver_manager.chrome import ChromeDriverManager

class TestAlltest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_alltest(self):
    self.driver.get("https://www.google.com.tr/")
    self.driver.maximize_window()
    usernameInput= self.driver.find_element(By.NAME,"q")
    usernameInput.send_keys("kodlama.io")
    usernameInput.send_keys(Keys.ENTER)

    element = self.driver.find_element(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    WebDriverWait(self.driver, 0.5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb")))
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb").click()
    WebDriverWait(self.driver, 0.5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Giriş Yap")))
    self.driver.find_element(By.LINK_TEXT, "Giriş Yap").click()
  
