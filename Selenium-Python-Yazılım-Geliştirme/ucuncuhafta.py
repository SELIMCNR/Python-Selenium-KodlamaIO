#Human.py içinde ekle Human ekle
from human import Human

# sınıflar => classlar
# modules 
# paket yönetimi
#self => this self fonksiyonda nesnenin kendisini ifade eder.nesneyi ifade eder self,bu classtaki nesne der.
# instance => örnek obje oluşturma classtan


human1 = Human("Selim")
human1.name="Yusuf"
human1.talk("Merhaba")
human1.walk()
print(human1) #str built in fonksiyonu içerisindeki işlemler yapılır.

human2=Human("Altay")
human2.name="Cem"
human2.talk("Selam")
human2.walk()
print(human2) #str built in fonksiyonu içerisindeki işlemler yapılır.

#Tek satırda işlem
Human("Selim").talk("Merhaba")