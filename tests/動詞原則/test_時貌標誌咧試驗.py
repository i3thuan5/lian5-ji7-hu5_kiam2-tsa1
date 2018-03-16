from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase, skip
from src.連字符檢查.動詞原則.動詞 import 是否符合咧原則


class 單元試驗(TestCase):
    def tearDown(self):
        句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
        self.assertEqual(是否符合咧原則(句物件), self.預期)

    # 動詞原則二：動詞和後接時貌標誌連寫
    # 咧
    # 徛-咧 講
    # 我 咧 想
    # 我 咧 遮
    # 我 徛--咧

    def test_徛咧講_正確(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā-leh kóng'
        self.預期 = []
    
    def test_徛咧講_錯誤_前面動詞連寫(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā leh kóng'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_徛咧講_錯誤_後分寫(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā-leh-kóng'
        self.預期 = [('E動詞（二）', 2, '後')]
    
    @skip('應該寫ti7整合試驗')
    def test_徛咧講_錯誤_前面動詞連寫後分寫(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā leh-kóng'
        self.預期 = [('E動詞（二）', 2, '前'), ('E動詞（二）', 2, '後')]
    
    @skip('分析器猶未好')
    def test_徛咧講_錯誤_後面有詞就不用輕聲調(self):
        self.漢字 = '徛咧講'
        self.臺羅 = 'Khiā--leh kóng'
        self.預期 = [('E動詞（二）', 2, '前')]

    def test_我咧講_錯誤_前面不是動詞(self):
        self.漢字 = '我咧講'
        self.臺羅 = 'Guá-leh kóng'
        self.預期 = [('E動詞（二）', 2, '前')]
    
    def test_坐佇咧遮_正確(self):
        # 佇-咧已經連寫了！前一個動詞坐不要再連寫
        self.漢字 = '坐佇咧遮'
        self.臺羅 = 'Tsē tī-leh tsia'
        self.預期 = []
    
    @skip('分析器的 Khiā-leh（錯誤） Khiā--leh（正確） 的詞物件仝款')
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
    
    @skip('分析器的 Khiā-leh（錯誤） Khiā--leh（正確） 的詞物件仝款')
    def test_徛咧_錯誤_語氣完結_應是輕聲符_句尾嘆詞(self):
        self.漢字 = '徛咧矣'
        self.臺羅 = 'Khiā-leh--ah'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 2, '前')]
    
    @skip('分析器的 Khiā-leh（錯誤） Khiā--leh（正確） 的詞物件仝款')
    def test_徛咧_錯誤_語氣完結_應是輕聲符_語尾助詞(self):
        self.漢字 = '欲徛咧無？'
        self.臺羅 = 'Beh khiā-leh--bô?'
        # 正確 'Khiā--leh'
        self.預期 = [('E動詞（二）', 3, '前')]
        
    def test_咧欲_正確(self):
        self.漢字 = '咧欲'
        self.臺羅 = 'teh-beh'
        self.預期 = []