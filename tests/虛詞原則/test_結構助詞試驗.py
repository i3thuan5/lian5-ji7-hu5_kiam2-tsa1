from unittest.case import TestCase, skip
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from src.連字符檢查.虛詞原則.虛詞 import 是否符合結構助詞原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合結構助詞原則(句物件), self.預期)

    # 虛詞原則三：結構助詞與前後詞分寫
    # 的、甲

    def test_結構助詞_的_正確(self):
        self.漢字 = '你的物件'
        self.臺羅 = 'Lí ê mi̍h-kiānn'
        self.預期 = []

    def test_結構助詞_的_前面不連寫(self):
        self.漢字 = '朋友的物件'
        self.臺羅 = 'pîng-iú-ê mi̍h-kiānn'
        self.預期 = [('E虛詞（三）', 3, '前')]

    def test_結構助詞_的_後面不連寫(self):
        self.漢字 = '朋友的物件'
        self.臺羅 = 'pîng-iú ê-mi̍h-kiānn'
        self.預期 = [('E虛詞（三）', 3, '後')]

    def test_結構助詞_的_前後不連寫(self):
        self.漢字 = '朋友的物件'
        self.臺羅 = 'pîng-iú-ê-mi̍h-kiānn'
        self.預期 = [('E虛詞（三）', 3, '前'), ('E虛詞（三）', 3, '後')]
    
    @skip('拆文分析器這馬閣有bug')
    def test_的_是詞綴_不是結構助詞(self):
        self.漢字 = '老的'
        self.臺羅 = 'lāu--ê'
        self.預期 = []
    