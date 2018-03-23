from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 連字符檢查.名詞原則.序列詞頭 import 序列詞頭原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(序列詞頭原則(句物件), self.預期,
                         (self.漢字, self.臺羅))
    # 名詞原則二：序列詞頭與後接數詞連寫
    # 初一、第五

    def test_初一_正確(self):
        self.漢字 = '恁初一去佗位'
        self.臺羅 = 'Lín tshe-it khì tó-uī'
        self.預期 = []

    def test_初一_應和後面數詞連寫(self):
        self.漢字 = '恁初一去佗位'
        self.臺羅 = 'Lín tshe it khì tó-uī'
        self.預期 = [('E名詞（二）', 3, '前')]

    def test_第十_應和後面數詞連寫(self):  
        self.漢字 = '恁第十工去佗位'
        self.臺羅 = 'Lín tē tsa̍p kang khì tó-uī'
        self.預期 = [('E名詞（二）', 3, '前')] 
    
    def test_頭一擺_正確_不是序列詞(self):  
        self.漢字 = '恁頭一擺去佗位'
        self.臺羅 = 'Lín thâu tsi̍t pái khì tó-uī'
        self.預期 = [] 