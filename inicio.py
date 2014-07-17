# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtSql import *
from PyQt4.QtCore import *

import sys

def main():  
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    db 		= QSqlDatabase.addDatabase("QMYSQL")
    
    table.setWindowTitle("Connect to Mysql Database Example")   
    
    db.setHostName("127.0.0.1")
    # db.setDatabaseName("dbpyqt4")
    db.setDatabaseName("prueba1")
    db.setUserName("root")
   # db.setPassword("root123")
    
    if (db.open()==False):     
        QMessageBox.critical(None, "Database Error", db.lastError().text())   
  
    query = QSqlQuery ("SELECT * FROM person")   
    
    table.setColumnCount(query.record().count())
    table.setRowCount(query.size())
    
    index=0
    while (query.next()):
        table.setItem(index,0,QTableWidgetItem(query.value(0).toString()))
        table.setItem(index,1,QTableWidgetItem(query.value(1).toString()))	
        index = index+1
    
    table.show()
    
    return app.exec_()
    
if __name__ == '__main__':
  main()
    
