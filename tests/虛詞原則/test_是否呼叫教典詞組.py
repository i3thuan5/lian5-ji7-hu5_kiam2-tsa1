from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from unittest.case import TestCase
from src.連字符檢查.虛詞原則.虛詞 import 是否符合介詞原則
from unittest.mock import patch


class mock試驗(TestCase):
    @patch('src.連字符檢查.教典.是教典詞組.是教典詞組')
    def test_介詞有呼叫教典詞組(self, 是教典詞組):
        句物件 = 拆文分析器.對齊句物件('漢字佇', 'han-ji-tī')
        是否符合介詞原則(句物件)
        是教典詞組.assert_called_once()  