import unittest
from DataProcessor import SqlLiteProcessor as dataProvider

class TestSqlLiteProcessor(unittest.TestCase):
    def Test_InitialTable(self):
        data = dataProvider.SqlLiteProcessor()
        result = data.InitialDb()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()