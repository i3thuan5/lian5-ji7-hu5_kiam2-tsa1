from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from src.連字符檢查.教典 import 是教典詞組


def 是否孤字介詞(字分詞):
    介詞集合 = ('佇｜ti7', '向｜hiong3', '替｜the3', '對｜tui3', '共｜ka7', '予｜hoo7')
    if 字分詞 in 介詞集合:
        return True
    return False


def 是否孤字連詞(字分詞):
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
    嘆詞集合 = ('喔｜ooh4', '哼｜hngh4', '哼｜hmh4',
            '啊｜ah4', '啦｜lah4', '哎｜aih4', '諾｜hioh4', '乎｜honnh4')
    if 字分詞 in 嘆詞集合:
        return True
    return False


def 是否語尾助詞(字分詞):
    語尾助詞集合 = ('矣｜ah4', '啦｜lah4', '嘛｜mah4',
              '乎｜honnh4', '啊｜ah4', '呢｜neh4', '無｜bo5')
    if 字分詞 in 語尾助詞集合:
        return True
    return False


def 虛詞(漢字, 臺羅):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    return 是否符合介詞原則(句物件) + 是否符合連詞原則(句物件)


def 是否符合原則(句物件):
    pass


def 是否符合介詞原則(句物件):
    錯誤訊息陣列 = []
    詞物件陣列 = 句物件.網出詞物件()
    累積詞長度 = 0
    for 詞物件 in 詞物件陣列:
        詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(詞的字物件陣列)
        詞分詞 = 詞物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
        for 字位置, 字物件 in enumerate(詞的字物件陣列):
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
            # 原則一：介詞和前後詞不可連寫
            # 佇，詞長度 = 1
            # 人-佇，詞長度 != 1
            if 是否孤字介詞(字分詞) and 詞長度 != 1 and (not 是教典詞組.是教典詞組(詞分詞)):
                # 檢查前面錯誤的連字符
                if 字位置 != 0:
                    錯誤行數 = 累積詞長度 + 字位置 + 1
                    錯誤連字符位置 = '前'
                    錯誤訊息陣列.append(('E虛詞（一）', 錯誤行數, 錯誤連字符位置))
                # 檢查後面錯誤的連字符
                if (字位置 + 1) < 詞長度:
                    錯誤行數 = 累積詞長度 + 字位置 + 1
                    錯誤連字符位置 = '後'
                    錯誤訊息陣列.append(('E虛詞（一）', 錯誤行數, 錯誤連字符位置))
        累積詞長度 += 詞長度
    return 錯誤訊息陣列


def 是否符合連詞原則(句物件):
    # 虛詞原則二：連詞語前後詞分寫
    錯誤訊息陣列 = []
    詞物件陣列 = 句物件.網出詞物件()
    累積詞長度 = 0
    for 詞物件 in 詞物件陣列:
        詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(詞的字物件陣列)
        詞分詞 = 詞物件.轉音(臺灣閩南語羅馬字拼音).看分詞()

        # 找出全部書寫錯誤的連詞位置
        連詞位置陣列 = []
        for 字位置, 字物件 in enumerate(詞的字物件陣列):
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
            if 是否孤字連詞(字分詞) and 詞長度 != 1 and (not 是教典詞組.是教典詞組(詞分詞)):
                連詞位置陣列.append(字位置)

        # 輸出錯誤資訊
        for 連詞位置 in 連詞位置陣列:
            # 檢查前面錯誤的連字符
            if 連詞位置 != 0:
                錯誤行數 = 累積詞長度 + 連詞位置 + 1
                錯誤連字符位置 = '前'
                錯誤訊息陣列.append(('E虛詞（二）', 錯誤行數, 錯誤連字符位置))
            # 檢查後面錯誤的連字符
            if (連詞位置 + 1) < 詞長度:
                錯誤行數 = 累積詞長度 + 連詞位置 + 1
                錯誤連字符位置 = '後'
                錯誤訊息陣列.append(('E虛詞（二）', 錯誤行數, 錯誤連字符位置))
        累積詞長度 += 詞長度
    return 錯誤訊息陣列


def 是否符合結構助詞原則(句物件):
    # 虛詞原則三：結構助詞與前後詞分寫
    錯誤訊息陣列 = []
    詞物件陣列 = 句物件.網出詞物件()
    累積詞長度 = 0
    for 詞位置, 詞物件 in enumerate(詞物件陣列):
        詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(詞的字物件陣列)
        詞分詞 = 詞物件.轉音(臺灣閩南語羅馬字拼音).看分詞()

        # 找出全部書寫錯誤的結構助詞位置
        結構助詞位置陣列 = []
        for 字位置, 字物件 in enumerate(詞的字物件陣列):
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
            # 詞長度不等於結構助詞的長度，表示有錯誤連寫
            if 是否結構助詞(字分詞) and 詞長度 != 1 and (not 是教典詞組.是教典詞組(詞分詞)):
                結構助詞位置陣列.append(字位置)

        # 輸出錯誤資訊
        for 詞位置 in 結構助詞位置陣列:
            # 檢查前面錯誤的連字符
            if 詞位置 != 0:
                錯誤行數 = 累積詞長度 + 詞位置 + 1
                錯誤連字符位置 = '前'
                錯誤訊息陣列.append(('E虛詞（三）', 錯誤行數, 錯誤連字符位置))
            # 檢查後面錯誤的連字符
            if (詞位置 + 1) < 詞長度:
                錯誤行數 = 累積詞長度 + 詞位置 + 1
                錯誤連字符位置 = '後'
                錯誤訊息陣列.append(('E虛詞（三）', 錯誤行數, 錯誤連字符位置))
        累積詞長度 += 詞長度
    return 錯誤訊息陣列


def 是否符合嘆詞原則(句物件):
    # 虛詞原則四：嘆詞與後面語詞分寫
    錯誤訊息陣列 = []
    詞物件陣列 = 句物件.網出詞物件()
    累積詞長度 = 0
    for 詞位置, 詞物件 in enumerate(詞物件陣列):
        詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(詞的字物件陣列)
        詞分詞 = 詞物件.轉音(臺灣閩南語羅馬字拼音).看分詞()

        # 找出全部書寫錯誤的嘆詞位置
        嘆詞位置陣列 = []
        for 字位置, 字物件 in enumerate(詞的字物件陣列):
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
            # 詞長度不等於嘆詞的長度，表示有錯誤連寫
            if 是否嘆詞(字分詞) and 詞長度 != 1 and (not 是教典詞組.是教典詞組(詞分詞)):
                嘆詞位置陣列.append(字位置)

        # 輸出錯誤資訊
        for 詞位置 in 嘆詞位置陣列:
            # 檢查前面錯誤的連字符
            if 詞位置 != 0:
                錯誤行數 = 累積詞長度 + 詞位置 + 1
                錯誤連字符位置 = '前'
                錯誤訊息陣列.append(('E虛詞（四）', 錯誤行數, 錯誤連字符位置))
            # 檢查後面錯誤的連字符
            if (詞位置 + 1) < 詞長度:
                錯誤行數 = 累積詞長度 + 詞位置 + 1
                錯誤連字符位置 = '後'
                錯誤訊息陣列.append(('E虛詞（四）', 錯誤行數, 錯誤連字符位置))
        累積詞長度 += 詞長度
    return 錯誤訊息陣列


def 是否符合語尾助詞原則(句物件):
    # 虛詞原則五：語尾助詞與前面語詞分寫
    錯誤訊息陣列 = []
    詞物件陣列 = 句物件.網出詞物件()
    累積詞長度 = 0
    for 詞位置, 詞物件 in enumerate(詞物件陣列):
        詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(詞的字物件陣列)
        詞分詞 = 詞物件.轉音(臺灣閩南語羅馬字拼音).看分詞()

        # 找出全部書寫錯誤的語尾助詞位置
        語尾助詞位置陣列 = []
        for 字位置, 字物件 in enumerate(詞的字物件陣列):
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
            # 詞長度不等於嘆詞的長度，表示有錯誤連寫
            if 是否語尾助詞(字分詞) and 詞長度 != 1 and (not 是教典詞組.是教典詞組(詞分詞)):
                語尾助詞位置陣列.append(字位置)

        # 輸出錯誤資訊
        for 詞位置 in 語尾助詞位置陣列:
            # 檢查前面錯誤的連字符（檢查第二個字到最後一個字）
            if 詞位置 != 0:
                錯誤行數 = 累積詞長度 + 詞位置 + 1
                錯誤連字符位置 = '前'
                錯誤訊息陣列.append(('E虛詞（五）', 錯誤行數, 錯誤連字符位置))
        累積詞長度 += 詞長度
    return 錯誤訊息陣列
