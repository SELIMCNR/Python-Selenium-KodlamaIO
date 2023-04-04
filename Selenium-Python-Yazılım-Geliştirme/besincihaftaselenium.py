# pip install selenium yaz ve paketi indir 
#selenium modülü içerisinden webdriverı ekle import et
from selenium import webdriver     #selenium internetteki işlemleri otomatize eder.
#webdriver_manager.chrome içinden  ChromeDriverManager ekle
from webdriver_manager.chrome import ChromeDriverManager
#time içinden sleep uykuyu import et ekle
from time import sleep
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from constants import globalConstants

class Test_Sauce:
    def __init__(self) :
         self.driver=webdriver.Chrome(ChromeDriverManager().install())
         self.driver.maximize_window()
         self.driver.get(globalConstants.Url)
    def test_invalid_login(self):
        #5saniye bekle ilgili elementin görünmesini user-name'nin
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) 
        usernameInput= self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput= self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn= self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        textResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"Test sonucu {textResult}")
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        #5saniye bekle ilgili elementin görünmesini user-name'nin
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) 
        usernameInput= self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn= self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(50)
        
        #Action Chains  aksiyonları bağlar birbirlerine.
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() #aksiyonları birbirine bağla ve çalıştır.
        loginBtn = self.driver.find_element(By.ID,"login-button") 
        loginBtn.click()       
        sleep(5)
        #javascript komutu çalıştırıldı
        self.driver.execute_script("window.scrollTo(0,500)") 
        sleep(20)
testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()
sleep(50)
while (True):
        continue
