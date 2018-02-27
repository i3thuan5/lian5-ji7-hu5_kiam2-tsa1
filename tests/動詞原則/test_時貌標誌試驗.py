from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase, skip


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合時貌標誌原則(句物件), self.預期)

    # 動詞原則二：動詞和後接時貌標誌連寫
    # 咧、著、過
    # 徛-咧 講
    # 咧 看 冊  (動詞前面的時貌標誌分寫）

    def test_徛咧講_正確(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā-leh kóng'
        self.預期 = []
#
#     def test_徛咧講_錯誤_前面動詞必須連寫(self):
#         self.漢字 = '徛咧講'
#         self.臺羅 = 'Khiā leh kóng'
#         self.預期 = [('E動詞（二）', 2, '前')]
#
#     def test_徛咧講_錯誤_後面不連寫(self):
#         self.漢字 = '徛咧講'
#         self.臺羅 = 'Khiā-leh-kóng'
#         self.預期 = [('E動詞（二）', 2, '後')]

    def test_徛咧講_錯誤_前面動詞連寫後分寫(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā leh-kóng'
        self.預期 = [('E動詞（二）', 2, '前'), ('E動詞（二）', 2, '後')]

    def test_徛咧講_錯誤_後面有詞就不用輕聲調(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā--leh kóng'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_我咧講_錯誤_前面不是動詞(self):
        self.漢字 = '我咧講'
        self.臺羅 = 'Guá-leh kóng'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧_正確(self):
        self.漢字 = '徛咧'
        self.臺羅 = 'Khiā--leh'
        self.預期 = []

    def test_徛咧_錯誤_應是輕聲符(self):
        self.漢字 = '徛咧'
        self.臺羅 = 'Khiā-leh'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧_錯誤_應是輕聲符2(self):
        self.漢字 = '徛咧'
        self.臺羅 = 'Khiā leh'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧_錯誤_語氣完結_應是輕聲符_句尾嘆詞(self):
        self.漢字 = '徛咧矣'
        self.臺羅 = 'Khiā-leh--ah'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧_錯誤_語氣完結_應是輕聲符_語尾助詞(self):
        self.漢字 = '欲徛咧無？'
        self.臺羅 = 'Beh khiā-leh--bô?'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 3, '前')]

    def test_看過書_錯誤(self):
        self.漢字 = '看過書'
        self.臺羅 = 'Khuànn--kuè-tsu'
        # 正確 Khuànn-kuè tsu
        self.預期 = [('E動詞（二）', 2, '前'), ('E動詞（二）', 2, '後')]

    def test_我看著的_錯誤_語氣完結_應是輕聲符_結構助詞(self):
        self.漢字 = '我看著的'
        self.臺羅 = 'Guá khuànn-tio̍h--ê'
        # 正確 Guá khuànn--tio̍h ê
        self.預期 = [('E動詞（二）', 3, '前'), ('E動詞（二）', 3, '後')]
