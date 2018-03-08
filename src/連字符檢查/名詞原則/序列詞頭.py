from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.基本物件.詞 import 詞


def 是序列詞頭(詞分詞):
    集合 = ('初｜tshe1', '初｜tshue1', '第｜te7',)
    return 詞分詞 in 集合


def 是數詞(詞分詞):
    集合 = ('一｜it4', '一｜tsit8', '二｜ji7', '二｜nng7', '三｜sam1', '三｜sann1', '四｜su3', '四｜si3', '五｜ngoo7', '五｜goo7',
          '六｜liok8', '六｜lak8', '七｜tshit4', '八｜pat4', '八｜peh4', '九｜kiu2', '九｜kau2', '十｜sip8', '十｜tsap8',
          '百｜pah4', '百｜peh4', '千｜tshian1', '千｜tshing1', '萬｜ban7', '億｜ik4',)
    return 詞分詞 in 集合


def 序列詞頭原則(句物件):
    #
    # 名詞原則二：序列詞頭與後接數詞連寫
    # 初一、第五
    #
    錯誤訊息陣列 = []
    詞物件陣列 = 句物件.網出詞物件()
    累積字長度 = 0
    前一个詞分詞 = None
    for 詞物件 in 詞物件陣列:
        詞分詞 = 詞物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
        字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(字物件陣列)
        第一個字分詞 = 詞(字物件陣列[:1]).轉音(臺灣閩南語羅馬字拼音).看分詞()
        # 序列詞頭與後接數詞連寫
        # 初一 => 初-一
        # 初十一 => 初-十-一
        if 前一个詞分詞 and 是序列詞頭(前一个詞分詞) and 是數詞(第一個字分詞):
            錯誤行數 = 累積字長度 + 1
            錯誤連字符位置 = '前'
            錯誤訊息陣列.append(('E名詞（二）', 錯誤行數, 錯誤連字符位置))

        前一个詞分詞 = 詞分詞
        累積字長度 += 詞長度
    return 錯誤訊息陣列
