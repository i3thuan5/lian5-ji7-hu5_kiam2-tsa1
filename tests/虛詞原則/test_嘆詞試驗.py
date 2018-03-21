from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from src.連字符檢查.虛詞原則.虛詞 import 是否符合嘆詞原則
from unittest.case import TestCase, skip


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合嘆詞原則(句物件), self.預期)

    # 虛詞原則四：嘆詞與後面語詞分寫
    # 喔、Hngh8

    def test_嘆詞_喔_正確(self):
        self.漢字 = '喔！是你！'
        self.臺羅 = 'Ooh!Sī lí!'
        self.預期 = []

    def test_嘆詞_喔_正確_沒標點符號(self):
        self.漢字 = '喔是你'
        self.臺羅 = 'Ooh Sī lí'
        self.預期 = []
    
    def test_嘆詞_喔_正確_詞尾(self):
        self.漢字 = '是你喔'
        self.臺羅 = 'Sī lí--ooh'
        self.預期 = []

    def test_嘆詞_喔_後面不連寫(self):
        self.漢字 = '喔是你'
        self.臺羅 = 'Ooh-sī lí'
        self.預期 = [('E虛詞（四）', 1, '後')]
