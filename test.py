import mainWindow 
import setParameter as sp
import measure as ms
import waveform_plot as wp
import pyvisa as visa

from PyQt5.Qt import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import webbrowser
import sys


# Load the UI file
# form_class = uic.loadUiType("info.ui")[0]

class InfoWindow(QMainWindow):
    def __init__(self):
        # QMainWindow.__init__(self, parent)
        super().__init__()
        uic.loadUi('info.ui', self)
        # self.setupUi(self)

        # manual button
        self.dev_manual.clicked.connect(self.dev_btn_callback)
        self.user_manual.clicked.connect(self.usr_btn_callback)
        # contribution
        self.contri.clicked.connect(self.contribution_btn_callback)
        # source code
        self.source.clicked.connect(self.source_btn_callback)
        # self.test_btn.clicked.connect(self.test_btn_callback)

        # connection source input
        self.check.clicked.connect(self.check_btn_callback)
        self.address.returnPressed.connect(self.check_btn_callback)


        
    def usr_btn_callback(self):
        url = ''
        webbrowser.open(url)


    def dev_btn_callback(self):
        url = 'file:///V:/Jaeyong/Hardware%20setup/DSO9404A/Programmer_s+Guide+for+Infiniium+Oscilloscop.pdf'
        webbrowser.open(url)

    
    # def test_btn_callback(self):
    #     self.main_window = mainWindow.MyWindowClass()
    #     self.main_window.show()

    
    def contribution_btn_callback(self):
        url = ''
        webbrowser.open(url)

    def source_btn_callback(self):
        url = 'https://github.com/tiancheng-st/qt_practice'
        webbrowser.open(url)

    def check_btn_callback(self):
        addr = self.address.text()
        self.connection_test(addr)


    # "USB0::0x0957::0x9009::MY53120106::0::INSTR"
    def connection_test(self, addr=""):
        rm = visa.ResourceManager()
        # scope = rm.open_resource(addr)
        # sp.initialize(scope)
        # ms.initialize(scope)
        # wp.initialize(scope)
        try:
            rm = visa.ResourceManager()
            scope = rm.open_resource(addr)
            sp.initialize(scope)
            ms.initialize(scope)
            wp.initialize(scope)
            # scope.timeout = 20000
            self.sucess_msg()
        except:
            self.error_msg()
    
    def error_msg(self):
        self.error = Error()
        self.error.show()

    def sucess_msg(self):
        self.sucess = SucessConnect()
        self.sucess.show() 



class Error(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('error.ui', self)


class SucessConnect(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('sucess.ui', self)
        self.test_btn.clicked.connect(self.test_begin)
    
    def test_begin(self):
        self.main_window = mainWindow.MyWindowClass()
        self.main_window.show()
    



app = QApplication(sys.argv)

myWindow = InfoWindow()
myWindow.show()
# wd = window2()
# wd.show()

app.exec_()
