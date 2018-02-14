from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from src.連字符檢查.虛詞原則.虛詞 import 是否符合嘆詞原則
from unittest.case import TestCase, skip


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合時貌標誌原則(句物件), self.預期)

    # 動詞原則二：動詞和後接時貌標誌連寫
    # 咧、著、過

    def test_徛咧講_正確(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā-leh kóng'
        self.預期 = []

    def test_徛咧講_錯誤_前面必須連寫(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā leh kóng'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧講_錯誤_後面動詞不連寫(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā-leh-kóng'
        self.預期 = [('E動詞（二）', 2, '後')]

    def test_徛咧講_錯誤_前連寫後分寫(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā leh-kóng'
        self.預期 = [('E動詞（二）', 2, '前'), ('E動詞（二）', 2, '後')]

    def test_徛咧講_錯誤_後面有詞就不用輕聲調(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā--leh kóng'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_看過書_錯誤_不用輕聲調且後面分寫(self):
        self.漢字 = '看過書'
        self.臺羅 = 'Khuànn--kuè-tsu'
        # 正確 Khuànn-kuè tsu
        self.預期 = [('E動詞（二）', 2, '前'), ('E動詞（二）', 2, '後')]

    def test_徛咧_正確(self):
        self.漢字 = '徛咧'
        self.臺羅 = 'Khiā--leh'
        self.預期 = []

    def test_徛咧_錯誤_應是輕聲符(self):
        self.漢字 = '徛咧'
        self.臺羅 = 'Khiā-leh'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧_錯誤_動詞和咧不斷開(self):
        self.漢字 = '徛咧矣'
        self.臺羅 = 'Khiā leh--ah'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧_錯誤_句尾嘆詞不影響輕聲符(self):
        self.漢字 = '徛咧矣'
        self.臺羅 = 'Khiā-leh--ah'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 2, '前')]
        
    def test_徛咧_錯誤_語尾助詞不影響輕聲符(self):
        self.漢字 = '欲徛咧無？'
        self.臺羅 = 'Beh khiā-leh--bô?'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 3, '前')]

    def test_我看著的_錯誤_結構助詞不影響輕聲符(self):
        self.漢字 = '我看著的'
        self.臺羅 = 'Guá khuànn-tio̍h--ê'
        # 正確 Guá khuànn--tio̍h--ê
        self.預期 = [('E動詞（二）', 3, '前')]
    
    def test_我看著的_錯誤_要和結構助詞分寫(self):
        self.漢字 = '我看著的'
        self.臺羅 = 'Guá khuànn-tio̍h-ê'
        # 正確 Guá khuànn--tio̍h--ê
        self.預期 = [('E動詞（二）', 3, '後')]
