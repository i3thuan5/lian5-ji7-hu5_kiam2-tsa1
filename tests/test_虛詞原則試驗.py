import pytest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.虛詞原則.虛詞 import 是否符合原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合原則(句物件), self.預期)
    
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
#           
# @pytest.mark.parametrize('漢字, 臺羅, 預期', [
#    
#    
#     # 虛詞原則二：連詞語前後詞分寫 
#     # 佮、閣、抑、愈
#     ('頭家佮辛勞', 'Thâu-ke kah sin-lô', None),
#     ('頭家佮辛勞', 'Thâu-ke-kah sin-lô', [('E虛詞（二）', 3, '前', 'Thâu-ke kah')]),
#     ('頭家佮辛勞', 'Thâu-ke kah-sin-lô', [('E虛詞（二）', 3, 'kah sin-lô')]),
#     ('頭家佮辛勞', 'Thâu-ke-kah-sin-lô', [('E虛詞（二）', 3, 'Thâu-ke kah sin-lô')]),
#     ('愈來愈乖', 'Jú lâi-jú kuai', [('E虛詞（二）', 3, 'Jú lâi jú kuai')]),
#     ('愈來愈乖', 'Jú-lâi jú kuai', [('E虛詞（二）', 1, 'Jú lâi jú kuai')]),
#     ('愈來愈乖', 'Jú-lâi-jú kuai', [('E虛詞（二）', 1, 'Jú lâi jú kuai'), ('E虛詞（一）', 3, 'Jú lâi jú kuai')]),
#     ('愈來愈乖', 'Jú lâi jú-kuai', [('E虛詞（二）', 3, 'Jú lâi jú kuai')]),
#     ('愈來愈乖', 'Jú lâi-jú-kuai', [('E虛詞（二）', 3, 'Jú lâi jú kuai')]),
#     # 虛詞原則三：結構助詞
#     # 的
#     ('你的物件', 'Lí ê mi̍h-kiānn', None),
#     ('朋友的物件', 'pîng-iú-ê mi̍h-kiānn', [('E虛詞（二）', 3, '前', 'pîng-iú ê')]),
#     ('朋友的物件', 'pîng-iú ê-mi̍h-kiānn', [('E虛詞（二）', 3, 'ê mi̍h-kiānn')]),
#     ('朋友的物件', 'pîng-iú-ê-mi̍h-kiānn', [('E虛詞（二）', 3, 'pîng-iú ê mi̍h-kiānn')]),
#     # 虛詞原則四：嘆詞與後面語詞分寫
#     # 喔、Hngh8
#     ('喔！是你', 'Ooh! Sī lí!', None),
#     ('喔是你', 'Ooh Sī lí!', None),
#     ('是你喔', 'Sī lí--ooh', None),
#     ('喔是你', 'Ooh-Sī lí!', [('E虛詞（四）', 1, '後', 'Ooh Sī')]),
#     # 虛詞原則五：結構助詞
#     # 否、未、無、啥
#     ('有錢無', 'Ū tsînn bô', None),
#     ('有錢無', 'Ū tsînn-bô', [('E虛詞（五）', 3, '前', 'tsînn bô')]),
#     ('有錢無', 'Ū tsînn--bô', None),
# ])
# def test_虛詞原則(漢字, 臺羅, 預期):
#     句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
#     assert 是否符合原則(句物件) == 預期
