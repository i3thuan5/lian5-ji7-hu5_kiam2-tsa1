from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase, skip
from src.連字符檢查.動詞原則.動詞 import 是否符合著原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合著原則(句物件), self.預期)

    # 動詞原則二：動詞和後接時貌標誌連寫
    
    # 動詞和時貌著連寫 我看著 => 我看-著
    # 著是動詞，跳過不處理 著你
    # 著是動詞一部份，跳過不處理 我著-病
    
    def test_我看著錢_正確(self):
        self.漢字 = '我看著錢'
        self.臺羅 = 'Guá khuànn-tio̍h tsînn'
        self.預期 = []

    def test_我看著錢_錯誤_前面連寫(self):
        self.漢字 = '我看著錢'
        self.臺羅 = 'Guá khuànn tio̍h tsînn'
        self.預期 = [('E動詞（二）', 3, '前'), ]

    def test_我看著錢_錯誤_不是結尾應正常變調(self):
        self.漢字 = '我看著錢'
        self.臺羅 = 'Guá khuànn--tio̍h tsînn'
        self.預期 = [('E動詞（二）', 3, '前'), ]

    def test_我看著錢_錯誤_後面分寫(self):
        self.漢字 = '我看著錢'
        self.臺羅 = 'Guá khuànn-tio̍h-tsînn'
        self.預期 = [('E動詞（二）', 3, '後'), ]

    def test_我看著的錢_正確(self):
        self.漢字 = '我看著的錢'
        self.臺羅 = 'Guá khuànn--tio̍h ê tsînn'
        self.預期 = []

    def test_我看著的錢_錯誤_結構助詞之前應輕聲調(self):
        self.漢字 = '我看著的錢'
        self.臺羅 = 'Guá khuànn-tio̍h ê tsînn'
        self.預期 = [('E動詞（二）', 3, '前'), ]

    def test_我看著矣_正確(self):
        self.漢字 = '我看著矣。'
        self.臺羅 = 'Guá khuànn--tio̍h--ah.'
        self.預期 = []

    def test_我有看著_正確(self):
        self.漢字 = '我有看著'
        self.臺羅 = 'Guá ū khuànn--tio̍h'
        self.預期 = []

    def test_我有看著_錯誤_結尾應輕聲調(self):
        self.漢字 = '我有看著。'
        self.臺羅 = 'Guá ū khuànn-tio̍h.'
        self.預期 = [('E動詞（二）', 3, '前'), ]

    def test_著是動詞_我著病(self):
        self.漢字 = '我著病。'
        self.臺羅 = 'Guá tio̍h-pīnn.'
        self.預期 = []
    
    