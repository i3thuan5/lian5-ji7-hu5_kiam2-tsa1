from src.連字符檢查.名詞原則 import 單音節詞綴, 方位詞, 序列詞頭
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 連字符檢查物件:
    句物件 = None

    def __init__(self, 漢字, 臺羅):
        self.句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)

    def 檢查(self):
        單音節詞綴.單音節詞綴原則(self.句物件)
        方位詞.方位詞原則(self.句物件)
        序列詞頭.序列詞頭原則(self.句物件)