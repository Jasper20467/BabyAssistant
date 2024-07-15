from DataProcessor import DataProcessor
import sqlite3
import logging

class SqlLiteProcessor():
    def __init__(self):
        # 連接到資料庫（如果資料庫不存在，則會自動建立）
        self.conn = sqlite3.connect('BabyAssistant.db')
        # 建立遊標物件
        self.cursor = self.conn.cursor()

        self.BasicTableName = "BasicInfo"
        self.BabyInfoTableName = "Info"
        self.MilkTableName = "Milk"
        self.DiaperTableName = "Diaper"

    def InitialDb(self):
        try:
            logging.debug(f'Initialing Table {self.BasicTableName}...')
            self.cursor.execute(f'''
                            CREATE TABLE IF NOT EXISTS {self.BasicTableName} (
                                id INTEGER PRIMARY KEY,
                                Name TEXT NOT NULL,
                                BirthDay DATETIME NOT NULL,
                                GA FLOAT NOT NULL,
                                Weight INTEGER NOT NULL,
                                Height FLOAT NOT NULL,
                                HC FLOAT NOT NULL
                            )
                            ''')
            logging.debug(f'Initialing Table {self.BabyInfoTableName}...')
            self.cursor.execute(f'''
                                CREATE TABLE IF NOT EXISTS {self.BabyInfoTableName} (
                                    id INTEGER PRIMARY KEY,
                                    Date DATETIME NOT NULL,
                                    Weight INTEGER NOT NULL,
                                    Height FLOAT NOT NULL,
                                    HC FLOAT NOT NULL
                                )
                                ''')
            logging.debug(f'Initialing Table {self.MilkTableName}...')
            self.cursor.execute(f'''
                            CREATE TABLE IF NOT EXISTS {self.MilkTableName} (
                                id INTEGER PRIMARY KEY,
                                Date DATETIME NOT NULL,
                                Brand TEXT NOT NULL,
                                Type TEXT NOT NULL,
                                Capacity INTEGER NOT NULL,
                                Price INTEGER NOT NULL,
                                Note Text NULL
                            )
                            ''')
            logging.debug(f'Initialing Table {self.DiaperTableName}...')
            self.cursor.execute(f'''
                            CREATE TABLE IF NOT EXISTS {self.DiaperTableName} (
                                id INTEGER PRIMARY KEY,
                                Date DATETIME NOT NULL,
                                Brand TEXT NOT NULL,
                                Type TEXT NOT NULL,
                                Price INTEGER NOT NULL,
                                Note Text NULL
                            )
                            ''')
            logging.debug(f'Initialized All tables.')
            self.conn.commit()
            return True
        except:
            logging.error('Initial DB/Table Failed')
            return False


    def DropAllTable(self):
        self.cursor.execute(f"DROP TABLE {self.BasicTableName}")
        self.cursor.execute(f"DROP TABLE {self.BabyInfoTableName}")
        self.cursor.execute(f"DROP TABLE {self.MilkTableName}")
        self.cursor.execute(f"DROP TABLE {self.DiaperTableName}")        
