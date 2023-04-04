import sys

from PyQt6 import QtWidgets
import webbrowser,time


class pencere(QtWidgets.QWidget):
    
    def __init__(self):
        
        
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        
        self.iurl=QtWidgets.QLineEdit("url")
        self.iagain=QtWidgets.QLineEdit("tekrar")
        self.basla=QtWidgets.QPushButton("baslat")
        
        
        
        vbox=QtWidgets.QVBoxLayout()
         
        vbox.addWidget(self.iurl)
        vbox.addWidget(self.iagain)
        vbox.addWidget(self.basla)
        
        vbox.addStretch()
        
        
        self.basla.clicked.connect(self.fbasla)
        
         
        self.setLayout(vbox)
        
        self.show()
    def fbasla(self):
        url=self.iurl.text()
        tekrar =self.iagain.text()
        for i in range(int(tekrar)):
            webbrowser.open_new(url)
            webbrowser.open_new_tab(url)
            time.sleep(1)
    
        

    
    
app=QtWidgets.QApplication(sys.argv)

pencere=pencere()

sys.exit(app.exec())    
    