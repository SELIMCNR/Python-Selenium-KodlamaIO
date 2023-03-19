#alias as takma isim
import ucuncuhaftamatematikmodül as mat
import random as rastgele #built in modül 
#ucuncuhaftamatematikmodül içinde topla metotunu ekle import et toplamislemi adında kullan
from ucuncuhaftamatematikmodül import topla as toplamaislemi
#ucuncuhafta içinden Human classı ekle import et
from ucuncuhafta import Human 
from human import Human

#selenium paketinden webdriverı ekle 
from selenium import webdriver



human1 = Human("Mirza")
human1.talk("Hello")

#ctrl tuşuna basılı tutup üzerine tıklarsan ilgili modülün detaylarını gösterir.
print(toplamaislemi(50,60))
print(mat.bol(10,20))
print(rastgele.randint(0,100)) #0ile 100 arasında rastgele sayı yazdırır.

#package paketler için pip install pip yazıp paket yöneticiyi ekle sonra 
#istediğin paketi indir örnek :pip install selenium
chromeDriver=webdriver.Chrome()