from unittest.case import TestCase, skip
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 連字符檢查.名詞原則.單音節詞綴 import 單音節詞綴原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(單音節詞綴原則(句物件), self.預期,
                         (self.漢字, self.臺羅))
    # 名詞原則一：名詞與單音節的前中後詞綴連寫
    # 名詞原則五：阿與後接人名連寫。
    # 程式無法分出後面是否為人名；所以將原則五合併到原則一。

    def test_阿公_正確(self):
        self.漢字 = '阿公'
        self.臺羅 = 'a-kong'
        self.預期 = []
    
    def test_阿公_名詞和前詞綴應連寫(self):
        self.漢字 = '恁阿公'
        self.臺羅 = 'Lín a kong'
        self.預期 = [('E名詞（一）', 3, '前')]
    
    def test_椅仔_正確(self):
        self.漢字 = '椅仔'
        self.臺羅 = 'Í-á'
        self.預期 = [] 
    
    def test_椅仔_名詞和後詞綴應連寫(self):
        self.漢字 = '椅仔'
        self.臺羅 = 'Í á'
        self.預期 = [('E名詞（一）', 2, '前')] 
    
    @skip('拆文分析器還分不出輕聲調')
    def test_林的_輕聲調的視為後詞綴(self):
        self.漢字 = '林的是啥人'
        self.臺羅 = 'Lîm--ê sī siánn-lâng'
        self.預期 = [('E名詞（一）', 2, '前')]