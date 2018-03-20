from unittest.case import TestCase
from src.連字符檢查.教典.是教典詞組 import 是教典詞組


class 單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(是教典詞組(self.詞分詞), self.預期)

    def test_佮意_教典有收(self):
        self.詞分詞 = '佮-意｜kah4-i3'
        self.預期 = True
    
    def test_佮豬_教典不存在此詞組(self):
        self.詞分詞 = '佮-豬｜kah4-ti1'
        self.預期 = False    