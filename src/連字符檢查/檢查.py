from 連字符檢查.名詞原則 import 單音節詞綴, 方位詞, 序列詞頭
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 連字符檢查.動詞原則 import 動詞
from 連字符檢查.虛詞原則 import 虛詞


class 連字符檢查物件:
    句物件 = None

    def __init__(self, 漢字, 臺羅):
        self.句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)

    def 檢查(self):
        函式串 = [單音節詞綴.單音節詞綴原則,
               方位詞.方位詞原則,
               序列詞頭.序列詞頭原則,
               動詞.是否符合環綴原則,
               動詞.是否符合咧原則,
               動詞.是否符合著原則,
               動詞.符合單音節補語原則,
               虛詞.是否符合介詞原則,
               虛詞.是否符合連詞原則,
               虛詞.是否符合結構助詞原則,
               虛詞.是否符合嘆詞原則,
               虛詞.是否符合語尾助詞原則,
               ]
        結果 = []
        for 一函式 in 函式串:
            結果 += 一函式(self.句物件)
        return sorted(結果, key = lambda x : x[1])
