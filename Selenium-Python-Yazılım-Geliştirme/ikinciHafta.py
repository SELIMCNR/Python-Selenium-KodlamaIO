faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

#type() -> verinin tipini verir.
print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12 )


#Tür dönüşümü
print(int(vade)+12)  #değer integer oldu

#print(int(krediAdi)) #stringden inte sayı olmayanlar çevrilmez
faiz = str(faiz) #İntegerden stringe dönüştü
print(type(faiz))


#Dışardan veri almak input
vade = input("Lütfen istediğiniz vade sayısını giriniz: ")
print(type(vade)) #inputdan gelen değer stringdir.
print(int(vade) + 12)

##String interpolation format yazdırma
print("Seçtiğiniz vade sonucu ortaya çıkan vade : "+str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi=vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade :{vade}")

isim = "Halit"
metin = "Merhaba {name}".format(name="Samet")
print(metin)

#F-String ile yazdırma
metin = f"Hoşgeldiniz {isim}"
metin2 = f"Hoşgeldiniz {1+1}"
print(metin)
print(metin2)


#listeler 
#döngüler
#fonksiyonlar


#Listeler
dizi = ["İhtiyaç Kredisi",10,5.2,True]
print(dizi)
krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
#liste yazdırma
print(krediler[0])
#Liste uzunluğu bulan fonksiyon
print(len(krediler))
#Listelere özel fonksiyonlar
krediler.append("Özel Kredi") #append son indise elemana ekler
print(krediler)

krediler.append("X Kredisi")
print(krediler)

#Liste silme işlemi
krediler.pop() #indeks vermezsen son elemanı sil
print(krediler)

krediler.remove("Konut Kredisi") # değere göre silme yapar ilk elemanı siler
krediler.remove("Taşıt Kredisi")


krediler.extend(["Y kredisi","Z kredisi"]) #listeye liste şeklinde eleman ekler extend
print(krediler)


#Döngüler

#For

for i in range(10): #0 dan 10 a kadar gider
    print("xx")
    print(i)
print("*****************")

for i in range(5,11): # 5 den 11'e kadar gider.
    print(i)
print("*****************")

for i in range(0,51,10): # 0'dan 51'e kadar 10 ar artarak gider
    print(i)

#Range fonksiyonu içinde integer döner double dönmez
#for i in range(0.1,0.5):
 #   print(i)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*************")
for i in range(len(krediler)):
    print(krediler[i])
print("********************") 


#While döngüsü 
#Sonsuz döngü
while True:
    print("x")
    break # döngü kırar

#While döngü
i=0
while True:
    print("x")    
    i+=1
    if i==10:
        break


while i<len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

#Fonskiyonlar
def calculate():
        print(100-20)

calculate() #Fonksiyon çalışır

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)


def sayHello(name):
    print(f"Merhaba {name}")



calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")

def calculateAndReturn(fiyat,indirim):
    return fiyat - indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat+10)

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("**********")
fonk1=calculatePrice(100,50)
fonk2=calculatePriceAndReturn(300,100)
print(f"159.satır : {fonk1+100}")
print(f"160.satır: {fonk2+100}")
print("************")

