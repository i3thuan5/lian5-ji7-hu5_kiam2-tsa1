from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.檢查 import 連字符檢查物件
from unittest import mock
from unittest.mock import patch


class mock試驗(TestCase):
    def setUp(self):
        self.一物件 = 連字符檢查物件('漢字', 'Hàn-jī')
        
    @patch('src.連字符檢查.名詞原則.單音節詞綴.單音節詞綴原則')
    def test用著單音節詞綴原則(self, 單音節詞綴原則):
        self.一物件.檢查()
        單音節詞綴原則.assert_called_once()
        
    @patch('src.連字符檢查.名詞原則.方位詞.方位詞原則')
    def test用著方位詞原則(self, 方位詞原則):
        self.一物件.檢查()
        方位詞原則.assert_called_once()
    
    @patch('src.連字符檢查.名詞原則.序列詞頭.序列詞頭原則')
    def test用著序列詞頭原則(self, 序列詞頭原則):
        self.一物件.檢查()
        序列詞頭原則.assert_called_once()
    
    