import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KRIXT Browser")
        self.setWindowIcon(QIcon("C:/Users/kim/Desktop/coding/KRIXT-browser/kicon.png"))
        self.setGeometry(100,100,1920,1080)
        self.showMaximized()
        self.setStyleSheet("background-color : white;")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.bb = QPushButton()
        self.bb.setIconSize(QSize(26,26))
        self.bb.setIcon(QIcon("C:/Users/kim/Desktop/coding/KRIXT-browser/bb.png"))
        self.bb.setStyleSheet("border : none")
        toolbar.addWidget(self.bb)
        self.bb.clicked.connect(self.bbb)

        self.fb = QPushButton()
        self.fb.setIconSize(QSize(26,26))
        self.fb.setIcon(QIcon("C:/Users/kim/Desktop/coding/KRIXT-browser/fb.png"))
        toolbar.addWidget(self.fb)
        self.fb.setStyleSheet("border : none")
        self.fb.clicked.connect(self.fbb)

        self.rb = QPushButton()
        self.rb.setIconSize(QSize(26,26))
        self.rb.setIcon(QIcon("C:/Users/kim/Desktop/coding/KRIXT-browser/rb.png"))
        toolbar.addWidget(self.rb)
        self.rb.setStyleSheet("border : none")
        self.rb.clicked.connect(self.rbb)

        self.ale = QLineEdit("https://")
        self.ale.setFont(QFont("Arial",10))
        self.ale.returnPressed.connect(self.sbb)
        self.ale.setStyleSheet("border : none")
        toolbar.addWidget(self.ale)

        self.sb = QPushButton()
        self.sb.setIconSize(QSize(26,26))
        self.sb.setIcon(QIcon("C:/Users/kim/Desktop/coding/KRIXT-browser/sb.png"))
        toolbar.addWidget(self.sb)
        self.sb.setStyleSheet("border : none")
        self.sb.clicked.connect(self.sbb)

        self.web = QWebEngineView()
        self.setCentralWidget(self.web)
        iurl = 'https://www.google.com'
        self.ale.setText(iurl)
        self.web.load(QUrl(iurl))

    def sbb(self):
        myurl = self.ale.text()
        self.web.load(QUrl(myurl))

    def bbb(self):
        self.web.back()

    def fbb(self):
        self.web.forward()

    def rbb(self):
        self.web.reload()



app = QApplication(sys.argv)
window = Window()
app.setStyle(QStyleFactory.create('Cleanlooks'))
window.show()
sys.exit(app.exec_())

