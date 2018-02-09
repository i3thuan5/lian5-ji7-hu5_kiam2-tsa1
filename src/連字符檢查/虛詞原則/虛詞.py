from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def 是否孤字介詞(字分詞):
    介詞集合 = ('佇｜ti7', '向｜hiong3', '替｜the3', '對｜tui3', '共｜ka7', '予｜hoo7')
    if 字分詞 in 介詞集合:
        return True
    return False


def 是否連詞(字分詞):
    連詞集合 = ('佮｜kah4', '閣｜koh4', '抑｜iah8', '愈｜ju2', '那｜na1')
    if 字分詞 in 連詞集合:
        return True
    return False


def 是否結構助詞(字分詞):
    結構助詞集合 = ('的｜e5', '甲｜kah4')
    if 字分詞 in 結構助詞集合:
        return True
    return False


def 是否嘆詞(字分詞):
    嘆詞集合 = ('喔｜ooh4', '哼｜hngh4', '哼｜hmh4', '啊｜ah4', '啦｜lah4')
    if 字分詞 in 嘆詞集合:
        return True
    return False


def 虛詞(漢字, 臺羅):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    return 是否符合原則(句物件)


def 是否符合原則(句物件):
    錯誤訊息陣列 = []
    詞物件陣列 = 句物件.網出詞物件()
    print(詞物件陣列)
    for 詞位置, 詞物件 in enumerate(詞物件陣列):
        print('詞位置={}'.format(詞位置))
        該詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(該詞的字物件陣列)
        for 字位置, 字物件 in enumerate(該詞的字物件陣列):
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
            print('字位置={}'.format(字位置), 字分詞, 是否孤字介詞(字分詞))
            # 原則一：介詞和前後詞不可連寫
            # 佇，詞長度 = 1
            # 人-佇，詞長度 != 1
            if 是否孤字介詞(字分詞) and 詞長度 != 1:
                print('孤字介詞={}'.format(字分詞))
                # 檢查前面錯誤的連字符
                if 字位置 != 0:
                    錯誤行數 = 字位置 + 1
                    錯誤連字符位置 = '前'
                    正確文字 = ''
                    錯誤訊息陣列.append(('E虛詞（一）', 錯誤行數, 錯誤連字符位置, 正確文字))
                # 檢查後面錯誤的連字符
                if (字位置+1) < 詞長度:
                    錯誤連字符位置 = '後'
                    
    return 錯誤訊息陣列

