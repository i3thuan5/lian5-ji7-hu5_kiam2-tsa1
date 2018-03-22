from unittest.case import TestCase
from src.連字符檢查.檢查 import 連字符檢查物件


class 整合試驗(TestCase):
    def tearDown(self):
        一物件 = 連字符檢查物件(self.漢字, self.臺羅) 
        結果 = 一物件.檢查()
        self.assertEqual(結果, self.預期)

    def test檢查一句(self):
        self.漢字 = '阿公會記得初一買我的物件'
        self.臺羅 = 'A kong ē kì-tit tshe it bé guá-ê mi̍h-kiānn'
        self.預期 = [
            ('E名詞（一）', 2, '前', ),
            ('E動詞（一）', 3, '後', ),
            ('E名詞（二）', 7, '前', ),
            ('E虛詞（三）', 10, '前'),
        ]
        
    def test檢查一句含特殊符號(self):
        self.漢字 = '就是佇咧運動／散步／跳舞。'
        self.臺羅 = 'tō sī tī-leh ūn-tōng/ sàn-pōo/ thiàu-bú.'
        self.預期 = []
