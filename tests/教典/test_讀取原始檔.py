from unittest.case import TestCase
from 連字符檢查.教典.讀取原始檔 import 讀取原始檔


class 單元試驗(TestCase):
        #
        # ('佮意', 'kah-ì', ('動',))
        # => ['佮-意｜kah4-i3']
        #
    def setUp(self):
        self.教典 = 讀取原始檔()

    def test_原本的詞轉成詞分詞(self):
        self.assertIn('佮-意｜kah4-i3', self.教典)
