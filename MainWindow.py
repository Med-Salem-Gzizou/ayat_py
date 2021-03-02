# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 380)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.sura_number_spinBox = QSpinBox(self.centralwidget)
        self.sura_number_spinBox.setObjectName(u"sura_number_spinBox")
        self.sura_number_spinBox.setMinimum(1)
        self.sura_number_spinBox.setMaximum(114)

        self.horizontalLayout.addWidget(self.sura_number_spinBox)

        self.search_btn = QPushButton(self.centralwidget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setEnabled(True)
        self.search_btn.setMaximumSize(QSize(160, 16777215))
        self.search_btn.setAutoDefault(False)
        self.search_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.search_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.suwar_listWidget = QListWidget(self.centralwidget)
        self.suwar_listWidget.setObjectName(u"suwar_listWidget")
        self.suwar_listWidget.setMaximumSize(QSize(140, 16777215))
        self.suwar_listWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.suwar_listWidget.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_3.addWidget(self.suwar_listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.read_ayat_checkBox = QCheckBox(self.centralwidget)
        self.read_ayat_checkBox.setObjectName(u"read_ayat_checkBox")

        self.horizontalLayout_4.addWidget(self.read_ayat_checkBox)

        self.aya_number_spinBox = QSpinBox(self.centralwidget)
        self.aya_number_spinBox.setObjectName(u"aya_number_spinBox")
        self.aya_number_spinBox.setMaximumSize(QSize(60, 16777215))
        self.aya_number_spinBox.setMinimum(1)
        self.aya_number_spinBox.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.aya_number_spinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.basmala_label = QLabel(self.centralwidget)
        self.basmala_label.setObjectName(u"basmala_label")
        font = QFont()
        font.setPointSize(15)
        self.basmala_label.setFont(font)
        self.basmala_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.basmala_label)

        self.ayats_listWidget = QListWidget(self.centralwidget)
        self.ayats_listWidget.setObjectName(u"ayats_listWidget")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setWeight(50)
        self.ayats_listWidget.setFont(font1)
        self.ayats_listWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.ayats_listWidget.setLayoutDirection(Qt.RightToLeft)
        self.ayats_listWidget.setSpacing(1)
        self.ayats_listWidget.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.ayats_listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tafsir_comboBox = QComboBox(self.centralwidget)
        self.tafsir_comboBox.setObjectName(u"tafsir_comboBox")

        self.verticalLayout.addWidget(self.tafsir_comboBox)

        self.tafsir_textBrowser = QTextBrowser(self.centralwidget)
        self.tafsir_textBrowser.setObjectName(u"tafsir_textBrowser")

        self.verticalLayout.addWidget(self.tafsir_textBrowser)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.search_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ayat_py", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.read_ayat_checkBox.setText(QCoreApplication.translate("MainWindow", u"Read Ayat On Click", None))
        self.basmala_label.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0650\u0633\u0652\u0645\u0650 \u0627\u0644\u0644\u064e\u0651\u0640\u0647\u0650 \u0627\u0644\u0631\u064e\u0651\u062d\u0652\u0645\u064e\u0640\u0670\u0646\u0650 \u0627\u0644\u0631\u064e\u0651\u062d\u0650\u064a\u0645\u0650", None))
        self.tafsir_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

