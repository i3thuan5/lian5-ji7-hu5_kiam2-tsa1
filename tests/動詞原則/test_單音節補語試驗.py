from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.動詞原則.動詞 import 符合單音節補語原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(符合單音節補語原則(句物件), self.預期,
                         (self.漢字, self.臺羅))

    # 動詞原則三：單音節動詞或形容詞，和後接補語連寫。
    # 其餘情況分寫。

    def test_講煞_正確(self):
        self.漢字 = '我講煞'
        self.臺羅 = 'Guá kóng-suah'
        self.預期 = []

    def test_講煞_要連寫(self):
        self.漢字 = '我講煞'
        self.臺羅 = 'Guá kóng suah'
        self.預期 = [('E動詞（三）', 3, '前')]
    
    def test_我煞_前面不是動詞(self):
        self.漢字 = '我煞'
        self.臺羅 = 'Guá-suah'
        self.預期 = [('E動詞（三）', 2, '前')]
        
    def test_整理好_要分寫(self):
        self.漢字 = '整理好'
        self.臺羅 = 'Tsíng-lí-hó'
        self.預期 = [('E動詞（三）', 3, '前')]

    def test_排好勢_要分寫(self):
        self.漢字 = '排好勢'
        self.臺羅 = 'Pâi-hó-sè'
        self.預期 = [('E動詞（三）', 2, '前')]

    def test_整理好勢_要分寫(self):
        self.漢字 = '整理好勢'
        self.臺羅 = 'Tsíng-lí-hó-sè'
        self.預期 = [('E動詞（三）', 3, '前')]
