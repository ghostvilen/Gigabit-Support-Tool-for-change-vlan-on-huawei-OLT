from PyQt6 import QtCore, QtGui, QtWidgets
import re
import csv
import telnetlib
import time
import sys
import os
import platform
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


# загрузка логина и пароля на оборудование 
load_dotenv('SupportTool\DB.env')


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog.resize(404, 292)
        Dialog.setMouseTracking(False)
        Dialog.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet("border-top-color: rgb(160, 248, 255);")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        flags = Dialog.windowFlags()
        Dialog.setWindowFlags(flags | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
           # Добавление значка окна
        icon = QtGui.QIcon("SupportTool\gigabit_logo.png")
        Dialog.setWindowIcon(icon)
        
        
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 10, 170, 30))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet("selection-color: rgb(172, 247, 255);\n"
"")
        self.pushButton.setShortcut("")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox.setGeometry(QtCore.QRect(250, 150, 200, 17))
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 130, 200, 30))
        self.comboBox.setObjectName("comboBox")
        # Открытие списка олтов
        with open('SupportTool\olt.csv', encoding='utf-8') as tsv_file:
                reader = csv.reader(tsv_file, delimiter=',')
                self.data = {row[0]: {'host': row[1], 'vlan': row[2]} for row in reader}
        #Заполнить выпадающий список
        self.comboBox.addItems(self.data.keys())
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 40, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 70, 170, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 170, 170, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 210, 170, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(225, 110, 170, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.text = self.lineEdit.text()
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 30))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(211, 255, 208);")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 200, 30))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(211, 255, 208);")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 200, 30))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(211, 255, 208);")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 200, 30))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(211, 255, 208);")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 200, 30))
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(211, 255, 208);")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 245, 200, 30))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(211, 255, 208);")
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def test_select_data(self):
            selected_item = self.comboBox.currentText()  # Получение выбранного элемента из QComboBox
        #if selected_item in self.data:
            host = self.data[selected_item]['host']
            vlan = self.data[selected_item]['vlan']
            print(f"Host: {host}, VLAN: {vlan}")    
            cb=self.lineEdit.text()
            fcb =re.sub(r'[^a-fA-F0-9]', '', cb.upper())
            print(fcb)
            DB_USERNAME = os.getenv("DB_USERNAME")
            DB_PASSWORD = os.getenv("DB_PASSWORD")
            connect = telnetlib.Telnet(host)
            connect.read_until(b'>>User name:')
            connect.write(f'{DB_USERNAME}\n'.encode())
            connect.read_until(b'>>User password:')
            connect.write(f'{DB_PASSWORD}\n'.encode())
            connect.read_until(b'>')
            connect.write(b'ena\n')
            connect.write(b'con\n')
            connect.write(b'undo alarm output all\n')           
                        
                        
                        
                        
        
            
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gigabit Support Tool"))
        self.pushButton.setText(_translate("Dialog", "Конвертировать для UTM"))
        self.checkBox.setText(_translate("Dialog", "Перезагрузка ONT"))
        self.pushButton_2.setText(_translate("Dialog", "Конвертировать для bdcom"))
        self.pushButton_3.setText(_translate("Dialog", "Последнее"))
        self.pushButton_4.setText(_translate("Dialog", "сменить VLAN"))
        self.pushButton_5.setText(_translate("Dialog", "МAC за терминалом"))
        self.label.setText(_translate("Dialog", "MAC для ютм"))
        self.label_2.setText(_translate("Dialog", "MAC для bdcom"))
        self.label_3.setText(_translate("Dialog", "Последнее"))
        self.label_4.setText(_translate("Dialog", "F/S/P ont ID"))
        self.label_5.setText(_translate("Dialog", "МAC за терминалом"))
        self.label_6.setText(_translate("Dialog", "Производитель роутера"))

    # Привязка сигнала "clicked" к слоту (convert_and_update_label_utm)
        self.pushButton.clicked.connect(convert_and_update_label_utm)
        # Привязка сигнала "clicked" к слоту (convert_and_update_label_bdcom)
        self.pushButton_2.clicked.connect(convert_and_update_label_bdcom)
        # Привязка сигнала "clicked" к слоту (convert_and_update_label_bdcom)
        self.pushButton_3.clicked.connect(copy_last_convert)
        # Привязка сигнала "clicked" к слоту (test_select_data)
        self.pushButton_4.clicked.connect(self.test_select_data)
        
        
        
def convert_and_update_label_utm():
                clipboard = app.clipboard()
                # Получение данных из буфера обмена
                clipboard_text = clipboard.text()
                
                # Конвертирование данных
                converted_text =re.sub(r'[^a-fA-F0-9]', '', clipboard_text.lower())
                #find_manufacturer
                find_manufacturer=converted_text[:6].upper()
                oui_database = load_oui_database()
                if find_manufacturer in oui_database:
                        find_manufacturer=oui_database[find_manufacturer]
                        ui.label_6.setText(find_manufacturer)
                else:
                        ui.label_6.setText('Manufacturer not found')
                converted_text = ':'.join([converted_text[i:i+2] for i in range(0, 12, 2)])
                # Запись в буфер обмена
                clipboard.setText(converted_text)
                print(converted_text)
                ui.label.setText(converted_text)
                ui.label_3.setText(converted_text)
                
def convert_and_update_label_bdcom():
                clipboard = app.clipboard()
                
                # Получение данных из буфера обмена
                clipboard_text = clipboard.text()
                
                # Конвертирование данных
                converted_text =re.sub(r'[^a-fA-F0-9]', '', clipboard_text.lower())
                converted_text = '.'.join([converted_text[i:i+4] for i in range(0, 12, 4)])
                
                # Запись в буфер обмена
                clipboard.setText(converted_text)
                print(converted_text)
                ui.label_2.setText(converted_text)
                ui.label_3.setText(converted_text)
                
def copy_last_convert():
        clipboard = app.clipboard()
        last_text=ui.label_3.text()
        clipboard.setText(last_text)

def load_oui_database():
    database = {}
    with open('my scripts\oui.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "MA-L":
                mac_address = row[1].replace(':', '').replace('-', '').upper()
                manufacturer = row[2].strip('"')
                database[mac_address] = manufacturer
    return database







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    global ui
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    load_dotenv('SupportTool\pyqt_test\DB.env')
    Dialog.show()
    sys.exit(app.exec())
