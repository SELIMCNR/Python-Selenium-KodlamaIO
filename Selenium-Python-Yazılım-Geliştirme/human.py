class Human:
    #built-in python içerisindeki hazır python metotları
    #constructor  yapıcı bloğa benzer 
    #initialize
    def __init__(self,name) :
        print("Bir human instance'i üretildi")
        self.name=name
        #Her nesnede birşeyler yapmada kullanılır
    def __str__(self):
       return f"STR Fonksiyonundan dönen değer : {self.name}" 
    name="Selim"
    def talk(self,sentence): #illaki self yazmaya gerek yok ama bu alanda ençok self kullanılır
        print(f"{self.name} : {sentence}")
    def walk(selim): #selim de yazabilin self yazmana gerek yok
        print("Human is walking..") 
