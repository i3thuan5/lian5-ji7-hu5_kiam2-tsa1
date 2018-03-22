from unittest.case import TestCase
from unittest.mock import patch
from 連字符檢查.檢查 import 連字符檢查物件

class mock試驗(TestCase):
    def setUp(self):
        self.一物件 = 連字符檢查物件(
            '阿公會記得初一買我的物件',
            'A kong ē kì-tit tshe it bé guá-ê mi̍h-kiānn'
        )
    # 名詞原則

    @patch('連字符檢查.名詞原則.單音節詞綴.單音節詞綴原則')
    def test用著單音節詞綴原則(self, 單音節詞綴原則):
        self.一物件.檢查()
        單音節詞綴原則.assert_called_once()

    @patch('連字符檢查.名詞原則.方位詞.方位詞原則')
    def test用著方位詞原則(self, 方位詞原則):
        self.一物件.檢查()
        方位詞原則.assert_called_once()

    @patch('連字符檢查.名詞原則.序列詞頭.序列詞頭原則')
    def test用著序列詞頭原則(self, 序列詞頭原則):
        self.一物件.檢查()
        序列詞頭原則.assert_called_once()

    # 動詞原則

    @patch('連字符檢查.動詞原則.動詞.是否符合環綴原則')
    def test用著環綴原則(self, 是否符合環綴原則):
        self.一物件.檢查()
        是否符合環綴原則.assert_called_once()

    @patch('連字符檢查.動詞原則.動詞.是否符合咧原則')
    def test用著咧原則(self, 是否符合咧原則):
        self.一物件.檢查()
        是否符合咧原則.assert_called_once()

    @patch('連字符檢查.動詞原則.動詞.是否符合著原則')
    def test用著著原則(self, 是否符合著原則):
        self.一物件.檢查()
        是否符合著原則.assert_called_once()

    @patch('連字符檢查.動詞原則.動詞.符合單音節補語原則')
    def test用著單音節補語原則(self, 符合單音節補語原則):
        self.一物件.檢查()
        符合單音節補語原則.assert_called_once()

    # 虛詞原則

    @patch('連字符檢查.虛詞原則.虛詞.是否符合介詞原則')
    def test用著介詞原則(self, 是否符合介詞原則):
        self.一物件.檢查()
        是否符合介詞原則.assert_called_once()

    @patch('連字符檢查.虛詞原則.虛詞.是否符合連詞原則')
    def test用著連詞原則(self, 是否符合連詞原則):
        self.一物件.檢查()
        是否符合連詞原則.assert_called_once()

    @patch('連字符檢查.虛詞原則.虛詞.是否符合結構助詞原則')
    def test用著結構助詞原則(self, 是否符合結構助詞原則):
        self.一物件.檢查()
        是否符合結構助詞原則.assert_called_once()

    @patch('連字符檢查.虛詞原則.虛詞.是否符合嘆詞原則')
    def test用著嘆詞原則(self, 是否符合嘆詞原則):
        self.一物件.檢查()
        是否符合嘆詞原則.assert_called_once()

    @patch('連字符檢查.虛詞原則.虛詞.是否符合語尾助詞原則')
    def test用著語尾助詞原則(self, 是否符合語尾助詞原則):
        self.一物件.檢查()
        是否符合語尾助詞原則.assert_called_once()
