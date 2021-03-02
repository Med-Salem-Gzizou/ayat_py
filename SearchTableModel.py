from PySide2.QtCore import QAbstractTableModel, Qt



class SearchTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.__data = []
        self.__header = ["sura", "sura name", "aya", "aya text"]
    
    def rowCount( self, parent ):
        return len(self.__data)

    def columnCount( self , parent ):
        return 4

    def data ( self , index , role ):
        if role == Qt.DisplayRole:
            i_row = index.row()
            i_column = index.column()
            value = self.__data[i_row][i_column]
            #print("model data():", value)
            return value

    def setData(self, index, value):
        self.__data[index.row()][index.column()] = value
        return True
    
    def headerData(self, col, orientation, role):
        #print(f"[headerData] col: {col} orientation: {orientation} role: {role}")
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.__header[col]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return col
        return None
    
    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
    
    def new_data(self, data):
        self.beginResetModel()
        self.__data = data
        self.endResetModel()
        return True
    
    def get_row(self, row_index:int) -> tuple:
        return self.__data[row_index]