# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(479, 333)
        self.centralwidget = QWidget(SearchWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.search_lineEdit = QLineEdit(self.centralwidget)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.horizontalLayout_2.addWidget(self.search_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.search_tableView = QTableView(self.centralwidget)
        self.search_tableView.setObjectName(u"search_tableView")
        self.search_tableView.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.search_tableView.setEditTriggers(QAbstractItemView.EditKeyPressed)
        self.search_tableView.setShowGrid(True)
        self.search_tableView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.search_tableView)

        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)

        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("SearchWindow", u"Search:", None))
    # retranslateUi

