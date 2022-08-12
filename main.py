from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from network import *


class Network_Calc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        label_1  = QLabel('Adres IP:', self)
        label_2  = QLabel('Prefix maski:', self)
        self.output = QLabel(self)
        self.output.setStyleSheet('background-color: white; border: 1px solid black;')
        
        grid = QGridLayout()

        grid.addWidget(label_1, 0, 0)
        grid.addWidget(label_2, 0, 1)
        
        

        self.addres_input = QLineEdit()
        self.addres_mask = QLineEdit()
      
        button = QPushButton("&Przelicz", self)
        clear = QPushButton('Wyczyść', self)
        grid.addWidget(self.addres_input, 1, 0)
        grid.addWidget(self.addres_mask, 1, 1)
        
        
        button.clicked.connect(self.count)
        clear.clicked.connect(self.clear)
        H = QHBoxLayout()
        H.addWidget(button)
        H.addWidget(clear)
        grid.addLayout(H, 2, 0, 1, 2)
        grid.addWidget(self.output, 3 , 0, 4, 2)
        
        self.setLayout(grid)
        self.setGeometry(20, 20, 600, 220)
        self.setWindowTitle("Kalkulator adresów sieci")
        self.show()


    def clear(self):

        sender = self.sender()
        del sender
        self.output.setText('')
        self.addres_input.setText('')
        self.addres_mask.setText('')
    def count(self):
        sender = self.sender()
        try:
            address = self.addres_input.text()
            mask = int(self.addres_mask.text())
            assert mask in range(33)
            assert Network_Calc.isValidAddres(address)
            network = Network(address, mask)

            self.output.setText(str(network))
            
            
        except:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

    @staticmethod

    def isValidAddres(text):
        numbers = text.split('.')
        if len(numbers) != 4:
            return False
        for _ in numbers:
            if int(_) not in range(256):
                return False
        return True






if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Network_Calc()
    sys.exit(app.exec_())
