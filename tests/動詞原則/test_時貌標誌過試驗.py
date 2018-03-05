from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase, skip
from src.連字符檢查.動詞原則.動詞 import 是否符合著原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合著原則(句物件), self.預期,
                         (self.漢字, self.臺羅))

    # 動詞原則二：動詞和後接時貌標誌連寫
    # 參考著的作法

    def test_我看過錢_錯誤_前面動詞應連寫(self):
        self.漢字 = '我看過錢'
        self.臺羅 = 'Guá khuànn kuè tsînn'
        self.預期 = [('E動詞（二）', 3, '前')]

    def test_我看過錢_錯誤_前面動詞應連寫_又音(self):
        self.漢字 = '我看過錢'
        self.臺羅 = 'Guá khuànn kè tsînn'
        self.預期 = [('E動詞（二）', 3, '前')]

    def test_過開頭詞組_正確(self):
        self.漢字 = '過分'
        self.臺羅 = 'kuè-hun'
        self.預期 = []

    def test_過結尾詞組_正確(self):
        self.漢字 = '透過'
        self.臺羅 = 'thàu-kuè'
        self.預期 = []
