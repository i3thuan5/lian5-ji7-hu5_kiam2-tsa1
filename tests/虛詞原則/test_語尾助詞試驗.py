from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from src.連字符檢查.虛詞原則.虛詞 import 是否符合嘆詞原則
from unittest.case import TestCase, skip
from src.連字符檢查.虛詞原則.虛詞 import 是否符合語尾助詞原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合語尾助詞原則(句物件), self.預期)

    # 虛詞原則五：語尾助詞
    # 否、未、無、啥
   
    def test_語尾助詞_喔_正確(self):
        self.漢字 = '有錢無'
        self.臺羅 = 'Ū tsînn bô'
        self.預期 = []
    
    @skip('拆文分析器猶閣無法度處理好輕聲調符號')
    def test_語尾助詞_喔_正確2(self):
        self.漢字 = '有錢無'
        self.臺羅 = 'Ū tsînn--bô'
        self.預期 = []
    
    def test_語尾助詞_喔_前面不連寫(self):
        self.漢字 = '有錢無'
        self.臺羅 = 'Ū tsînn-bô'
        self.預期 = [('E虛詞（五）', 3, '前')]
