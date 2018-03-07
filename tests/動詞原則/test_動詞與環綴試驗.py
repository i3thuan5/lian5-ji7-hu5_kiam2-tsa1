from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.動詞原則.動詞 import 是否符合環綴原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合環綴原則(句物件), self.預期)

    # 動詞原則一：動詞與環綴連寫
    # 會...得，袂...得

    def test_會記得_正確(self):
        self.漢字 = '我會記得你'
        self.臺羅 = 'Guá ē-kì-tit lí'
        self.預期 = []
    
    def test_會記得_錯誤_首字應連寫(self):
        self.漢字 = '姑娘會記得你'
        self.臺羅 = 'Koo-niû ē kì-tit lí'
        self.預期 = [('E動詞（一）', 3, '後')]

    def test_會記得_錯誤_尾字應連寫(self):
        self.漢字 = '姑娘會記得你'
        self.臺羅 = 'Koo-niû ē-kì tit lí'
        self.預期 = [('E動詞（一）', 5, '前')]
    
    def test_袂記得_正確(self):
        self.漢字 = '我袂記得你'
        self.臺羅 = 'Guá bē-kì--tit lí'
        self.預期 = []

    def test_才會得人疼_正確(self):
        self.漢字 = '才會得人疼'
        self.臺羅 = 'Tsiah-ē tit-lâng-thiànn'
        self.預期 = []