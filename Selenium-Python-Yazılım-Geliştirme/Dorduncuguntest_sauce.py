# pip install selenium yaz ve paketi indir 
#selenium modülü içerisinden webdriverı ekle import et
from selenium import webdriver     #selenium internetteki işlemleri otomatize eder.
#webdriver_manager.chrome içinden  ChromeDriverManager ekle
from webdriver_manager.chrome import ChromeDriverManager
#time içinden sleep uykuyu import et ekle
from time import sleep
#
from selenium.webdriver.common.by import By
class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput= driver.find_element(By.ID,"user-name")
        passwordInput= driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(10)
        loginBtn= driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        textResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"Test sonucu {textResult}")
        sleep(10)
testClass = Test_Sauce()
testClass.test_invalid_login()
sleep(50)
while (True):
        continue
