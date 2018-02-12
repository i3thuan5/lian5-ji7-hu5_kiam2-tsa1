from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.虛詞原則.虛詞 import 是否符合介詞原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合介詞原則(句物件), self.預期)
    
    # 虛詞原則一：介詞與前後詞分寫
    def test_虛詞原則一_佇_正確(self):
        self.漢字 = '伊佇頭前'
        self.臺羅 = 'I tī thâu-tsîng'
        self.預期 = []
    
    def test_虛詞原則一_佇_前面不連寫(self):
        self.漢字 = '伊佇頭前'
        self.臺羅 = 'I-tī thâu-tsîng'
        self.預期 = [('E虛詞（一）', 2, '前', 'I tī')]
    
    def test_虛詞原則一_佇_後面不連寫(self):
        self.漢字 = '伊佇頭前'
        self.臺羅 = 'I tī-thâu-tsîng'
        self.預期 = [('E虛詞（一）', 2, '後', 'tī thâu-tsîng')]
    
    def test_虛詞原則一_佇_前後皆不連寫(self):
        self.漢字 = '伊佇頭前'
        self.臺羅 = 'I-tī-thâu-tsîng'
        self.預期 = [('E虛詞（一）', 2, '前', 'I tī'), ('E虛詞（一）', 2, '後', 'tī thâu-tsîng')]
    
    def test_虛詞原則一_佇_長詞(self):
        self.漢字 = '頭家佇頭前'
        self.臺羅 = 'Thâu-ke-tī-thâu-tsîng'
        self.預期 = [('E虛詞（一）', 3, '前', 'Thâu-ke tī'), ('E虛詞（一）', 3, '後', 'tī thâu-tsîng')]
    
    def test_虛詞原則一_佇_數字調_正確(self):
        self.漢字 = '伊佇頭前'
        self.臺羅 = 'I1 ti7 thau5-tsing5'
        self.預期 = []
        
    def test_虛詞原則一_予_正確(self):
        self.漢字 = '講予你知'
        self.臺羅 = 'kóng hōo lí tsai'
        self.預期 = []
    
    def test_虛詞原則一_予_後面不連寫(self):
        self.漢字 = '講予你知'
        self.臺羅 = 'kóng hōo-lí tsai'
        self.預期 = [('E虛詞（一）', 2, '後', 'hōo lí')]