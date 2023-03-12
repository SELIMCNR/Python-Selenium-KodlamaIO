print("Kodlamaio")

#değişken tanımlama
baslik="Taşıt Kredisi"

print(baslik)

#string => metinsel ifade 
baslik = "İhtiyac kredisi"
print(baslik)

#int , integer => tam sayi 
vade = 36 
ekVade=6
vade2 = "36"

#float ,decimal,double
aylikOdeme = 200.50

# bool,boolean => True veya False
yukselisteMi=True

#Matematiksel Operatörler
#+
print(5+5)
print(vade +12)
print(vade + ekVade)
print(36+6)
#-
print(5-5)
print(vade-12)
print(vade-ekVade)
print(36-6)
#*
print(5*5)
print(vade *2)
print(vade * ekVade)
print(10 *10)
#/
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)

yeniVade = vade / 2
fiyat = 100 
indirimliFiyat= fiyat -20 
print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü
print(10%2)
print(vade %5)
print(vade % ekVade)
print(30 % 10)

#Mantıksal operatörler
print(1 == 1)
print( 1==2)

print(1>2)
print(3>1)
print(1>1)
print(1>=1)
#control k + ctrl c yapılabilir.

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print( 1!=1 )
print( 1!=2 )

#or and 
print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)

print(1>2 and 5>2 and 3>2)

#karar yapıları
#if else 
sayi1=10
sayi2=15
# sayi1 sayi2 'den büyükse ekrana sayi 1 daha büyük yazdır.
#condition 

#indent
if sayi1 > sayi2:
    print("Sayi 1 Sayi 2'den büyüktür.")
#eğer if bloğu çalışmaz ise 
elif sayi1 == sayi2:
    print("İki sayı eşittir")
else:
    print("Sayi sayi 2 'den büyüktür") 
print("Burası if bloğunun dışındadır.")       

print("*************")
