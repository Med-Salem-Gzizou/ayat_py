
from PySide2.QtSql import QSqlDatabase, QSqlQuery
from suwar import SUWAR_LIST

AYAT_DB = "resources/ayat.ayt"
TAFASIR_DB = "resources/tafasir.ayt"

AYAT_DB_CON = QSqlDatabase.addDatabase('QSQLITE', "AYAT_DB_CON")
AYAT_DB_CON.setDatabaseName(AYAT_DB)
AYAT_DB_CON.open()

DBS_CON = QSqlDatabase.addDatabase('QSQLITE')

# @return: arry of Tuple's (aya_number, aya_text)
def get_sura(sura_number:int) -> list:
    query = QSqlQuery(AYAT_DB_CON)
    query.exec_(f"SELECT * FROM ayat WHERE sura={sura_number} ORDER BY aya ASC")
    id, sura_n, aya_n, text, nass_safy, safha = range(6)

    data = []
    while query.next():
        item = (query.value(aya_n), query.value(text))
        data.append(item)
    
    query.finish()
    return data

# @return: tafsir text as string
def get_aya_tafsir(sura_number:int, aya_number:int, trans_key:str, trans_dir:str) -> str:
    db_path = f"resources/{trans_dir}/{trans_key}.ayt"
    DBS_CON.setDatabaseName(db_path)
    DBS_CON.open()
    query = QSqlQuery(f"SELECT * FROM {trans_key} WHERE sura={sura_number} AND aya={aya_number} LIMIT 1", DBS_CON)
    query.first()
    text = query.value(3)
    query.finish()
    DBS_CON.close()
    return text

# @return: array of tuple's (trans_key, trans_name, trans_dir)
def get_tafasir_list() -> list:
    DBS_CON.setDatabaseName(TAFASIR_DB)
    DBS_CON.open()
    query = QSqlQuery(f'SELECT * FROM trans ORDER BY trans_order ASC', DBS_CON)
    id, trans_key, trans_name, trans_desc, trans_tbl, trans_order, trans_dir = range(7)

    data = []
    while query.next():
        item = (query.value(trans_key), query.value(trans_name), query.value(trans_dir))
        data.append(item)
    
    query.finish()
    DBS_CON.close()
    return data

# @return: array of tuple's (sura_number:int, sura_name:str, aya_number:int, aya_text:str)
def get_aya_search_result(text:str) -> list:
    data = []
    if len(text) <= 0: return data
    query = QSqlQuery(f'SELECT * FROM ayat WHERE nass_safy LIKE "%{text}%"', AYAT_DB_CON)
    id, sura, aya, text, nass_safy, safha = range(6)

    while query.next():
        name = SUWAR_LIST[query.value(sura) - 1]["name"]
        item = (query.value(sura), name, query.value(aya), query.value(text))
        data.append(item)
    
    query.finish()
    return data