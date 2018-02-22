from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合環綴原則(句物件), self.預期)

    # 動詞原則一：動詞與環綴連寫
    # 會...得，袂...得

    def test_會記得_正確(self):
        self.漢字 = '會記得'
        self.臺羅 = 'ē-kì-tit'
        self.預期 = []
    
    def test_會記得_錯誤(self):
        self.漢字 = '會記得'
        self.臺羅 = 'ē kì-tit'
        self.預期 = [('E動詞（一）', 1, '前')]

    def test_會記得_錯誤_前後應連寫(self):
        self.漢字 = '會記得'
        self.臺羅 = 'ē kì tit'
        self.預期 = [('E動詞（一）', 1, '前'), ('E動詞（一）', 1, '後')]
    
    def test_袂記得_正確(self):
        self.漢字 = '袂記得'
        self.臺羅 = 'bē-kì--tit'
        self.預期 = []
