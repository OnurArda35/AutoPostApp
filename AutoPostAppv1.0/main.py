from ast import Index
import enum
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from panel import *
import sqlite3
from datetime import datetime, timedelta
from PyQt5.QtCore import QDateTime, Qt
import threading
import time
from instagrapi import Client

def adapt_datetime(datetime_obj):
    return datetime_obj.isoformat()
sqlite3.register_adapter(datetime, adapt_datetime)

# Arayüz işlemleri

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


#Veritabanı işlemleri1

baglanti = sqlite3.connect("Records.db",check_same_thread=False)
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("Create Table if Not Exists UserRecords(Username text, Password text)")
baglanti.commit()

table2 = islem.execute("Create Table if Not Exists PostRecords(Username text, Password text, Caption text, File text, CreatedDate datetime, PostDate datetime)")
baglanti.commit()

ui.usernameTbl.setHorizontalHeaderLabels(["Users"])
ui.postTbl.setHorizontalHeaderLabels(["User","Caption","File","Created Date","Post Date"])

def setDateTimeToNow():
    ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
    threading.Timer(30,setDateTimeToNow).start()

def post():
    query = "select * from PostRecords where PostDate between ? and ?"

    try:
        islem.execute(query,(datetime.now().replace(second=0,microsecond=0),datetime.now().replace(second=0,microsecond=0) + timedelta(minutes=1)))
        results = islem.fetchall()
        baglanti.commit()
        if results:
            for row in results:
                client = Client()
                client.login(row[0], row[1])
                photo_path = row[3].replace('/','\\')
                photo_item = client.photo_upload(photo_path, row[2])
                client.logout()
                ui.statusbar.showMessage("Post Paylaşıldı", 10000)
        
    except Exception as e:
            ui.statusbar.showMessage("Post Paylaşılamadı."+ str(e), 10000)
    threading.Timer(60,post).start()
    


#User ekleme

def addUser():
    uName = ui.usernameLn.text()
    pword = ui.passwordLn.text()

    try:
        add = "insert into UserRecords(Username,Password) values (?,?)"
        islem.execute(add,(uName,pword))
        baglanti.commit()
        ui.statusbar.showMessage("Kayit Eklendi!", 10000)
        showUserList()
        ui.usernameLn.clear()
        ui.passwordLn.clear()
    except:
        ui.statusbar.showMessage("Kayit Eklenemedi!", 10000)
    setCombo()

def delUser():
    delmsg = QMessageBox.question(pencere,"Silme Onayı","Silmek istediğine Emin Misin?")
    QMessageBox.Yes | QMessageBox.No
    if delmsg == QMessageBox.Yes:
        selectedUser = ui.usernameTbl.selectedItems()
        userToDel = selectedUser[0].text()

        query = "delete from UserRecords where Username = ?"

        try:
            islem.execute(query,(userToDel,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayit Silindi.", 10000)
            showUserList()
        except Exception as e:
            ui.statusbar.showMessage("Kayit Silinemedi."+ str(e), 10000)

    else:
        ui.statusbar.showMessage("İslem İptal Edildi.", 10000)
    setCombo()
        
def delPost():
    delmsg = QMessageBox.question(pencere,"Post Silme Onayı","Postu Silmek İster Misin?")
    QMessageBox.Yes | QMessageBox.No
    if delmsg == QMessageBox.Yes:
        selectedPost = ui.postTbl.selectedItems()
        postToDel = selectedPost[0].text()
        
        query = "delete from PostRecords where CreatedDate = ?"

        try:
            islem.execute(query,(postToDel,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayit Silindi.", 10000)
            showPostList()
        except Exception as e:
            ui.statusbar.showMessage("Kayit Silinemedi", 10000)
        
    else:
        ui.statusbar.showMessage("İslem iptal Edildi", 10000)
        
                

#UserList Güncelleme
        
def showUserList():
    ui.usernameTbl.clear()
    ui.usernameTbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.usernameTbl.setHorizontalHeaderLabels(["Users"])
    query = "select Username from UserRecords"
    islem.execute(query)

    for indexRow, recNo in enumerate(islem):
        for indexCol, recCol in enumerate(recNo):
            ui.usernameTbl.setItem(indexRow,indexCol,QTableWidgetItem(str(recCol)))

def showPostList():
    ui.postTbl.clear()
    ui.postTbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.postTbl.setHorizontalHeaderLabels(["User","Caption","File","Created Date","Post Date"])
    query = "select Username, Caption, File, CreatedDate, PostDate from PostRecords"
    islem.execute(query)

    for indexRow, recNo in enumerate(islem):
        for indexCol, recCol in enumerate(recNo):
            ui.postTbl.setItem(indexRow,indexCol,QTableWidgetItem(str(recCol)))


#Post Ekleme

def addPost():
    selectedUser = ui.usernameTbl.selectedItems()
    if selectedUser:
        uName = selectedUser[0].text()
        #get the password
        query = "select Password From UserRecords where Username = ? "
        pword = islem.execute(query,(uName,))
        result = islem.fetchone()
        if result is not None:
            pword = result[0]
        else:
            ui.statusbar.showMessage("Kullanici Bulunamadi!", 10000)
            
        caption = ui.captionLn.text()
        file = ui.fileLn.text()
        createdDate = datetime.now()
        postDate = ui.dateTimeEdit.dateTime()
        
        
        

        try:
            add = "insert into PostRecords(Username,Password,Caption,File,CreatedDate,PostDate) values (?,?,?,?,?,?)"
            islem.execute(add,(uName,pword,caption,file,createdDate, postDate.toPyDateTime()))
            baglanti.commit()
            ui.statusbar.showMessage("Kayit Eklendi!", 10000)
            showPostList()
            ui.fileLn.clear()
            ui.captionLn.clear()
        except Exception as e:
            ui.statusbar.showMessage("Kayit Eklenemedi!" + str(e), 10000)
    else:
        ui.statusbar.showMessage("Lütfen Kullanici Seciniz!",10000)

def browse():
    fileName, _  = QFileDialog.getOpenFileName(None, 'Single File', 'C:\\', '*')
    ui.fileLn.setText(fileName)



def setCombo():
    ui.comboBox.clear()
    ui.comboBox.addItem('All')
    query = "select Username from UserRecords"
    islem.execute(query)
    results = islem.fetchall()
    baglanti.commit()
    for result in results:
        ui.comboBox.addItem(result[0])

def filterPost():
    filter_value = ui.comboBox.currentText()
    if filter_value != 'All':
        query = "select * from PostRecords where Username = ?"
        islem.execute(query,(filter_value,))
        ui.postTbl.clear()
        ui.postTbl.setHorizontalHeaderLabels(["User","Caption","File","Created Date","Post Date"])
        for indexRow, recNo in enumerate(islem):
            for indexCol, recCol in enumerate(recNo):
                ui.postTbl.setItem(indexRow,indexCol,QTableWidgetItem(str(recCol)))
    else:
        showPostList()


#Butonlar
ui.filterPostBtn.clicked.connect(filterPost)
ui.delPostBtn.clicked.connect(delPost)
ui.browseBtn.clicked.connect(browse)
ui.addBtn.clicked.connect(addUser)
ui.delBtn.clicked.connect(delUser)
ui.postBtn.clicked.connect(addPost)


setCombo()
post()
setDateTimeToNow()
showPostList()
showUserList()
sys.exit(uygulama.exec_())