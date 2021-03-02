#!/usr/bin/python3

from PySide2.QtWidgets import QWidget, QMainWindow, QSpinBox
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QListWidgetItem, QTableView
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PySide2.QtCore import Qt, QUrl, QDir, QModelIndex, QSettings

from MainWindow import Ui_MainWindow
from SearchWindow import Ui_SearchWindow
from SearchTableModel import SearchTableModel

import qt_db_handler
from suwar import SUWAR_LIST

ORG_NAME = "GZIZOU_ORG"
APP_NAME = "AYAT_PY"

class AyatSearchWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AyatSearchWindow, self).__init__(parent=parent)

        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)

        self.ui.search_table_model = SearchTableModel()
        self.ui.search_tableView.setModel(self.ui.search_table_model)
        self.ui.search_tableView.setSelectionBehavior(QTableView.SelectRows)
        self.ui.search_tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.search_tableView.verticalHeader().setVisible(True)

        self.ui.search_lineEdit.textChanged.connect(self.on_search_lineEdit_change)

        self.restore_settings()
    
    def restore_settings(self):
        settings = QSettings(ORG_NAME, APP_NAME)
        print( "Settings file:", settings.fileName())
        self.restoreGeometry(settings.value('SW_geometry'))
        self.restoreState(settings.value('SW_state'))
        self.ui.search_lineEdit.setText(settings.value('SW_search_text'))
        self.columns_width = settings.value('SW_columns_width')
        if self.columns_width != None:
            for i in range(3):
                self.ui.search_tableView.setColumnWidth(i, int(self.columns_width[i]))

    def save_settings(self):
        settings = QSettings(ORG_NAME, APP_NAME)
        settings.setValue('SW_geometry', self.saveGeometry())
        settings.setValue('SW_state', self.saveState())
        settings.setValue('SW_search_text', self.search_text)
        self.columns_width = []
        for i in range(3):
            self.columns_width.append(self.ui.search_tableView.columnWidth(i))
        settings.setValue('SW_columns_width', self.columns_width)
    
    def on_search_lineEdit_change(self, text:str):
        self.search_text = text
        data = qt_db_handler.get_aya_search_result(text)
        # display data
        self.ui.search_table_model.new_data(data)
    
    def closeEvent(self, event):
        self.save_settings()


class AyatMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AyatMainWindow, self).__init__(parent)

        # Setup windows
        self.search_window = AyatSearchWindow(self)
        
        # Setup ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.restore_settings()

        self.audio_player = QMediaPlayer()
        self.load_ui_data()

        # connect main window
        self.ui.search_btn.clicked.connect(self.on_btn_search_click)
        self.ui.suwar_listWidget.itemClicked.connect(self.on_surah_name_click)
        self.ui.ayats_listWidget.itemClicked.connect(self.on_aya_click)
        self.ui.tafsir_comboBox.currentIndexChanged.connect(self.on_tafsir_selectionchange)
        self.ui.read_ayat_checkBox.stateChanged.connect(
            lambda:self.on_read_aya_btn_change(self.ui.read_ayat_checkBox)
        )
        self.ui.aya_number_spinBox.valueChanged.connect(self.on_aya_number_box_change)
        self.ui.sura_number_spinBox.valueChanged.connect(self.on_sura_number_box_change)

        # connect search window
        self.search_window.ui.search_tableView.clicked.connect(self.on_search_item_click)


    def restore_settings(self):
        settings = QSettings(ORG_NAME, APP_NAME)
        print("settings file:", settings.fileName())
        self.restoreGeometry(settings.value('MW_geometry'))
        self.restoreState(settings.value('MW_state'))
        if settings.value('sura_number') != None:
            self.selected_sura_number = int(settings.value('sura_number'))
        else:
            self.selected_sura_number = 1
        if settings.value('aya_number') != None:
            self.selected_aya_number = int(settings.value('aya_number'))
        else:
            self.selected_aya_number = 1
        if settings.value('tafsir_i') != None:
            self.selected_tafsir_index = int(settings.value('tafsir_i'))
        else:
            self.selected_tafsir_index = 0
        if settings.value('read_aya') != None:
            self.read_aya_on_click = int(settings.value('read_aya'))
        else:
            self.read_aya_on_click = 0
    
    def save_settings(self):
        settings = QSettings(ORG_NAME, APP_NAME)
        settings.setValue('MW_geometry', self.saveGeometry())
        settings.setValue('MW_state', self.saveState())
        settings.setValue('sura_number', self.selected_sura_number)
        settings.setValue('aya_number', self.selected_aya_number)
        settings.setValue('tafsir_i', self.selected_tafsir_index)
        settings.setValue('read_aya', self.read_aya_on_click)
    
    def load_ui_data(self):
        self.load_sura_list()
        self.load_tafasir_list()
        
        self.set_selected_sura(self.selected_sura_number)
        self.show_sura()
        self.set_selected_aya(self.selected_aya_number)
        self.set_selected_tafsir(self.selected_tafsir_index)
        self.show_tafsir()
        self.set_read_aya_on_click(self.read_aya_on_click)
    
    def set_selected_sura(self, sura_number:int):
        self.selected_sura_number = sura_number
        self.ui.suwar_listWidget.item(sura_number -1).setSelected(True)
        self.ui.suwar_listWidget.setCurrentRow(sura_number - 1)
        self.ui.sura_number_spinBox.setValue(sura_number)
    
    def set_selected_aya(self, aya_number:int):
        self.selected_aya_number = aya_number
        self.ui.aya_number_spinBox.setValue(self.selected_aya_number)
        self.ui.ayats_listWidget.item(self.selected_aya_number - 1).setSelected(True)
        self.ui.ayats_listWidget.setCurrentRow(self.selected_aya_number - 1)
    
    def set_selected_tafsir(self, tafsir_index:int):
        self.selected_tafsir_index = tafsir_index
        self.ui.tafsir_comboBox.setCurrentIndex(tafsir_index)
    
    def set_read_aya_on_click(self, state:bool):
        self.ui.read_ayat_checkBox.setChecked(state)
    
    def show_sura(self):
        self.ui.ayats_listWidget.clear()
        data = qt_db_handler.get_sura(self.selected_sura_number)
        for row in data:
            aya_number = row[0]
            aya_text = row[1]
            item_text = '(' + str(aya_number) + ') ' + aya_text
            item = QListWidgetItem(item_text, self.ui.ayats_listWidget)
            item.aya_number = aya_number
        ayat_count = len(data)
        self.ui.aya_number_spinBox.setMaximum(ayat_count)
        if self.selected_sura_number == 1 or self.selected_sura_number == 9:
            self.ui.basmala_label.hide()
        else:
            self.ui.basmala_label.show()
    
    def show_tafsir(self):
        surah_number = self.selected_sura_number
        aya_number = self.selected_aya_number
        trans_key = self.tafasir_list[self.selected_tafsir_index][0]
        trans_dir = self.tafasir_list[self.selected_tafsir_index][2]
        text = qt_db_handler.get_aya_tafsir(surah_number, aya_number, trans_key, trans_dir)
        TAFSIR_STYLE_HTML = "<style> p {font-size: 15px;} </style>"
        self.ui.tafsir_textBrowser.setHtml(TAFSIR_STYLE_HTML + text)
    
    def play_aya(self):
        sura_number = self.selected_sura_number
        aya_number = self.selected_aya_number
        file_name = ""
        if sura_number < 10:
            file_name += "00" + str(sura_number)
        elif sura_number < 100:
            file_name += "0" + str(sura_number)
        else:
            file_name += str(sura_number)
        if aya_number < 10:
            file_name += "00" + str(aya_number)
        elif aya_number < 100:
            file_name += "0" + str(aya_number)
        else:
            file_name += str(aya_number)
        file_name += ".mp3"
        file_path = QDir.current().absoluteFilePath("resources/mp3/"+file_name)
        media = QMediaContent(QUrl.fromLocalFile(file_path))
        self.audio_player.setMedia(media)
        self.audio_player.play()
    
    def load_sura_list(self):
        self.ui.suwar_listWidget.clear()
        for surah in  SUWAR_LIST:
            if surah["number"] < 10:
                name = str(surah["number"]) + " " * 4 + surah["name"]
            elif surah["number"] < 100:
                name = str(surah["number"]) + " " * 3 + surah["name"]
            else :
                name = str(surah["number"]) + " " * 2 + surah["name"]
            item = QListWidgetItem(name, self.ui.suwar_listWidget)
            item.surah_number = surah["number"]
    
    def load_tafasir_list(self):
        self.ui.tafsir_comboBox.clear()
        self.tafasir_list = qt_db_handler.get_tafasir_list()
        for t in self.tafasir_list:
            self.ui.tafsir_comboBox.addItem(t[1])
    
    def on_surah_name_click(self, item):
        self.set_selected_sura(item.surah_number)
        self.show_sura()
        self.set_selected_aya(1)
        self.show_tafsir()
    
    def on_btn_search_click(self):
        if self.search_window.isVisible(): return
        self.search_window.show()
    
    def on_read_aya_btn_change(self, btn):
        self.read_aya_on_click = int(btn.isChecked())
    
    def on_aya_number_box_change(self, value:int):
        #if self.ui.aya_number_spinBox.value() == self.selected_aya_number: return
        if self.selected_aya_number == value: return
        self.set_selected_aya(value)
    
    def on_sura_number_box_change(self, value:int):
        if self.selected_sura_number == value: return
        self.set_selected_sura(value)
        self.show_sura()
        self.set_selected_aya(1)
    
    def on_aya_click(self, item):
        self.set_selected_aya(item.aya_number)
        self.show_tafsir()
        if self.read_aya_on_click: self.play_aya()
    
    def on_tafsir_selectionchange(self, index:int):
        if index < 0: return
        self.selected_tafsir_index = index
        self.show_tafsir()
    
    def on_search_item_click(self, index:QModelIndex):
        item = self.search_window.ui.search_table_model.get_row(index.row())
        if len(item) <= 0: return
        sura_number = item[0]
        aya_number  = item[2]
        self.set_selected_sura(sura_number)
        self.show_sura()
        self.set_selected_aya(aya_number)
    
    def closeEvent(self, event):
        self.save_settings()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = AyatMainWindow()
    window.show()
    sys.exit(app.exec_())
