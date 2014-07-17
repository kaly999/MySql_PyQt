
from PyQt4.QtGui import *     # Contiene los Widgets
from PyQt4.QtSql import *
from PyQt4.QtCore import *

import sys

#class Ventana(QWidget):
#
#    def __init__(self):
#        super(Ventana, self).__init__()
#
#        # Cambiar el titulo de la ventana
#        self.setWindowTitle("Ejercicio uno")
#
#        # Redimensionar ventana
#        self.resize(800, 600)
#
#        # Mover posicion de inicio de la ventana
#        self.move(200, 100)
#
#        # Cambiar icono
#        self.setWindowIcon(QIcon("environment.png"))

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Connect to database
        db 		= QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("127.0.0.1")
        db.setDatabaseName("dbpyqt4")
        db.setUserName("root")
        db.setPassword("root123")
        
        if (db.open()==False):     
            QMessageBox.critical(None, "Database Error", db.lastError().text())   

        # Create QComboBox to show tables
        combo = QComboBox(self)
        

        # Create QTableView to show table's data
        tabla = QTableView(self)
        tabla.move(100, 0)

        # Create table model 
        TableModel = QSqlTableModel(self, db)
        tabla.setModel(TableModel)

        # Connect combobox signal to update model
        combo.currentIndexChanged[str].connect(TableModel.setTable)
        combo.currentIndexChanged[str].connect(TableModel.select)

        # Set the list of the tables to combobox
        combo.addItems(db.tables())
        
        
        btnInsert = QPushButton('Insert', self)
        btnInsert.clicked.connect(TableModel.insertRow)
        btnInsert.move(0, 100)
#        btnDelete = QPushButton('Delete', self)
#        btnDelete.clicked.connect(TableModel.deleteRow)
#        btnDelete.move(0, 200)

#    def deleteRow(self):
#        index = self.__tableGrid__.currentIndex()
#        self.__tableModel__.removeRows(index.row(), 1)

    def insertRow(self):
        TableModel.insertRows(0, 1)



app = QApplication(sys.argv)

ventana = MainWindow()
ventana.show()

# MainLoop que me mantiene viva a la aplicacion
sys.exit(app.exec_())
