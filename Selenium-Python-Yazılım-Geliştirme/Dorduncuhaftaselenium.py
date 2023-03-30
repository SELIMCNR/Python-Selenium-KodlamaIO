# pip install selenium yaz ve paketi indir 
#selenium modülü içerisinden webdriverı ekle import et
from selenium import webdriver     #selenium internetteki işlemleri otomatize eder.
#webdriver_manager.chrome içinden  ChromeDriverManager ekle
from webdriver_manager.chrome import ChromeDriverManager
#time içinden sleep uykuyu import et ekle
from time import sleep
#
from selenium.webdriver.common.by import By
#chromedriver yaz internetetten chrome sürümüne göre chromedriveri winşeklini indir klasöre at.
#klasöre içinde değilse parametreye ekle bilgileri  driver = webdriver.Chrome("C:\Dersler\Yazılım geliştirme\Görsel-Programlama-Python\Selenium-Python-Yazılım-Geliştirme")
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(ChromeDriverManager().install()) #seleniumun kullanacağı tarayıcıyı ekle
driver.maximize_window() #Pencereyi tam ekran yap
driver.get("https://www.google.com/") #parametre içinde yazılan websiteye giden kod
input = driver.find_element(By.NAME,"q") #site üzerinde name si q olanı bul
input.send_keys("Fenerbahçe") #arama yerine fenerbahçe yazar
searchButton=driver.find_element(By.NAME,"btnK")   #namesi btnK olan buttonu bul 
sleep(2)     #2 saniye bekle script kodlarını
searchButton.click() #ve bulduğun arama buttonuna tıkla
sleep(5)
firstResult=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/a") #xpathedeki adresi bul ve 
firstResult.click() #xpathdeki adrese websitesine git.
listOfClasses=driver.find_elements(By.CLASS_NAME,"content")
print(f"Şuanda şu kadar haber var {listOfClasses}")
while(True):
    continue


#Html Locators 
"""
    xpath: Bulunacak elemana dair yol çizer elementi seç copy full xpath dersen örnek :/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/a
     
     xpath://*[@id='rso']/div[3]/div/div/div/div[1]/div/a


     web scrapting  : sitelerden veri kazıma
     data scrapting

"""