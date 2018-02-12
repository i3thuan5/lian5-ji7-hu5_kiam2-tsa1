from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.虛詞原則.虛詞 import 是否符合連詞原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合連詞原則(句物件), self.預期)

    # 虛詞原則二：連詞語前後詞分寫
    # 佮、閣、抑、愈

    def test_連詞_佮_正確(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke kah sin-lô'
        self.預期 = []

    def test_連詞_佮_前面不連寫(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke-kah sin-lô'
        self.預期 = [('E虛詞（二）', 3, '前')]

    def test_連詞_佮_後面不連寫(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke kah-sin-lô'
        self.預期 = [('E虛詞（二）', 3, '後')]

    def test_連詞_佮_前後皆不連寫(self):
        self.漢字 = '頭家佮辛勞'
        self.臺羅 = 'Thâu-ke-kah-sin-lô'
        self.預期 = [('E虛詞（二）', 3, '前'),
                   ('E虛詞（二）', 3, '後')]

    def test_連詞_多個佮(self):
        self.漢字 = '我佮伊佮爸爸佮恁老師'
        self.臺羅 = 'Guá-kah-i-kah-pah-pah-kah-Lín-lāu-su'
        self.預期 = [
            ('E虛詞（二）', 2, '前'),
            ('E虛詞（二）', 2, '後'),
            ('E虛詞（二）', 4, '前'),
            ('E虛詞（二）', 4, '後'),
            ('E虛詞（二）', 7, '前'),
            ('E虛詞（二）', 7, '後'), ]

    def test_連詞_我佮伊講好(self):
        self.漢字 = '我佮伊講好'
        self.臺羅 = 'Guá-kah-i kóng-hó'
        self.預期 = [
            ('E虛詞（二）', 2, '前'),
            ('E虛詞（二）', 2, '後'), ]

    def test_連詞_第一個愈_後面不連寫(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú-lâi jú kuai'
        self.預期 = [('E虛詞（二）', 1, '後')]

    def test_連詞_第二個愈_後面不連寫(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú lâi jú-kuai'
        self.預期 = [('E虛詞（二）', 3, '後')]

    def test_連詞_第二個愈_前面不連寫(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú lâi-jú kuai'
        self.預期 = [('E虛詞（二）', 3, '前')]

    def test_連詞_愈愈_不夾詞(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú-lâi-jú kuai'
        self.預期 = [('E虛詞（二）', 1, '後'), ('E虛詞（二）', 3, '前')]

    def test_連詞_愈愈_不夾詞_長詞(self):
        self.漢字 = '愈大漢愈乖'
        self.臺羅 = 'Jú-tuā-hàn-jú kuai'
        self.預期 = [('E虛詞（二）', 1, '後'),
                   ('E虛詞（二）', 3, '前')]

    def test_連詞_愈愈_不當詞嵌(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú lâi-jú-kuai'
        self.預期 = [('E虛詞（二）', 3, '前'), ('E虛詞（二）', 3, '後')]

    def test_連詞_愈愈_不當詞嵌_長詞(self):
        self.漢字 = '愈來愈大漢'
        self.臺羅 = 'Jú lâi-jú-tuā-hàn'
        self.預期 = [('E虛詞（二）', 3, '前'),
                   ('E虛詞（二）', 3, '後')]

    def test_連詞_愈愈_不串在一起(self):
        self.漢字 = '愈來愈乖'
        self.臺羅 = 'Jú-lâi-jú-kuai'
        self.預期 = [('E虛詞（二）', 1, '後'),
                   ('E虛詞（二）', 3, '前'),
                   ('E虛詞（二）', 3, '後')]
