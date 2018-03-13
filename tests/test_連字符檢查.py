from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.檢查 import 連字符檢查物件
# from unittest.mock import MagicMock
from unittest import mock
from unittest.mock import patch


class mock試驗(TestCase):
    @patch('src.連字符檢查.名詞原則.單音節詞綴.單音節詞綴原則')
    def test用著單音節詞綴原則(self, 單音節詞綴原則):
        一物件 = 連字符檢查物件('漢字', 'Hàn-jī')
        一物件.檢查()
        單音節詞綴原則.assert_called_once()

# class 整合試驗(TestCase):
#     def tearDown(self):
#         句物件 = 拆文分析器.對齊句物件(self.漢字, self.臺羅)
#         self.assertEqual(檢查連字符(句物件), self.預期)
# 
#     def test名詞原則(self):
#         self.漢字 = '阿公初一蹛山頂啦，'
#         self.臺羅 = 'A kong tshe it tuà suann tíng--lah,'
#         self.預期 = [('E名詞（一）', 2, '前'), ('E名詞（二）', 4, '前'),  ('E名詞（二）', 7, '前')]
# 
#     def test動詞原則(self):
#         self.漢字 = ''
#         self.臺羅 = ''
#         self.預期 = []
# 
#     def test虛詞原則(self):
#         self.漢字 = ''
#         self.臺羅 = ''
#         self.預期 = []
