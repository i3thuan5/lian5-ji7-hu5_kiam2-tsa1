from unittest.case import TestCase, skip
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from src.連字符檢查.名詞原則.序列詞頭 import 序列詞頭原則


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
        self.預期 = [('E名詞（一）', 3, '前')]

    def test_第一_應和後面數詞連寫(self):  
        self.漢字 = '恁第一工去佗位'
        self.臺羅 = 'Lín tshe it kang uī khì tó-uī'
        self.預期 = [('E名詞（一）', 3, '前')] 