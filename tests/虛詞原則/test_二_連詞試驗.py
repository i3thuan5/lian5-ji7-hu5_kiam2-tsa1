from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.虛詞原則.虛詞 import 是否符合原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合原則(句物件), self.預期)

    # 虛詞原則二：連詞語前後詞分寫
    # 佮、閣、抑、愈

    def test_連詞_佮_正確(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke kah sin-lô'
        self.預期 = []

    def test_連詞_佮_前面不連寫(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke-kah sin-lô'
        self.預期 = [('E虛詞（二）', 3, '前', 'Thâu-ke kah')]

    def test_連詞_佮_後面不連寫(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke kah-sin-lô'
        self.預期 = [('E虛詞（二）', 3, '後', 'kah sin-lô')]

    def test_連詞_佮_前後皆不連寫(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke-kah-sin-lô'
        self.預期 = [('E虛詞（二）', 3, '前', 'Thâu-ke kah'),
                   ('E虛詞（二）', 3, '後', 'kah sin-lô')]

    def test_連詞_第一個愈_後面不連寫(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú-lâi jú kuai'
        self.預期 = [('E虛詞（二）', 1, '後', 'Jú lâi')]

    def test_連詞_第二個愈_後面不連寫(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú lâi jú-kuai'
        self.預期 = [('E虛詞（二）', 3, '後', 'jú kuai')]
    
    def test_連詞_第二個愈_前面不連寫(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú lâi-jú kuai'
        self.預期 = [('E虛詞（二）', 3, '前', 'lâi jú')]

    def test_連詞_愈愈_不夾別詞(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú-lâi-jú kuai'
        self.預期 = [('E虛詞（二）', 1, '後', 'Jú lâi'), ('E虛詞（二）', 3, '前', 'lâi jú')]

    def test_連詞_愈愈_不當詞嵌(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú lâi-jú-kuai'
        self.預期 = [('E虛詞（二）', 3, '前', 'lâi jú'), ('E虛詞（二）', 3, '後', 'jú kuai')]
