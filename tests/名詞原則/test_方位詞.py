from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 連字符檢查.名詞原則.方位詞 import 方位詞原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(方位詞原則(句物件), self.預期,
                         (self.漢字, self.臺羅))
    # 名詞原則三：名詞和單音節方位詞連寫，和多音節方位詞分寫
    # 山-頂、門 後-壁

    def test_山頂_正確(self):
        self.漢字 = '山頂'
        self.臺羅 = 'suann-tíng'
        self.預期 = []

    def test_山頂_單音節方位詞連寫(self):
        self.漢字 = '山頂'
        self.臺羅 = 'suann tíng'
        self.預期 = [('E名詞（三）', 2, '前')]
    
    def test_山後壁_正確(self):
        self.漢字 = '山後壁'
        self.臺羅 = 'suann āu-piah'
        self.預期 = []
        
    def test_山後壁_多音節方位詞分寫(self):
        self.漢字 = '山後壁'
        self.臺羅 = 'suann-āu-piah'
        self.預期 = [('E名詞（三）', 2, '前')]