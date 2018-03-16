from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase, skip
from src.連字符檢查.虛詞原則.虛詞 import 是否符合語尾助詞原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合語尾助詞原則(句物件), self.預期)

    # 虛詞原則五：語尾助詞
    # 否、未、無、啥
   
    def test_語尾助詞無_正確(self):
        self.漢字 = '有錢無'
        self.臺羅 = 'Ū tsînn bô'
        self.預期 = []
    
    @skip('拆文分析器猶閣無法度處理好輕聲調符號')
    def test_語尾助詞無_正確2(self):
        self.漢字 = '有錢無'
        self.臺羅 = 'Ū tsînn--bô'
        self.預期 = []
    
    def test_語尾助詞無_前面不連寫(self):
        self.漢字 = '有錢無'
        self.臺羅 = 'Ū tsînn-bô'
        self.預期 = [('E虛詞（五）', 3, '前')]
    
    def test_多個語尾助詞_皆前面不連寫(self):
        self.漢字 = '有錢啊乎'
        self.臺羅 = 'Ū tsînn ah-honnh'
        self.預期 = [('E虛詞（五）', 4, '前')]
    
    def test_逐家攏足無閒_正確(self):
        self.漢字 = '逐家攏足無閒，'
        self.臺羅 = 'ta̍k-ke lóng tsiok bô-îng,'
        self.預期 = []
        
