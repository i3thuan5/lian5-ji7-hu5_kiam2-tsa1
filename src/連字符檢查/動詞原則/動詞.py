from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.基本物件.詞 import 詞


def 是環綴起始(字分詞):
    集合 = ('會｜e7', '袂｜be7')
    return 字分詞 in 集合


def 是環綴結尾(字分詞):
    集合 = ('得｜tit4',)
    return 字分詞 in 集合


def 是動詞(詞分詞):
    集合 = ('徛｜khia7',)
    return 詞分詞 in 集合


def 是助詞(字分詞):
    集合 = ('咧｜leh4', '咧｜teh4', '著｜tioh8', '過｜kue3')
    return 字分詞 in 集合

def 是咧詞組(詞分詞):
    集合 = ('佇-咧｜ti7-leh4')
    return 詞分詞 in 集合

def 是否符合環綴原則(句物件):
    # 動詞原則一：動詞與環綴連寫
    # 會...得，袂...得
    錯誤訊息陣列 = []
    累積字長度 = 0
    #
    # 我會記得你 -> 我, 會記得, 你
    詞物件陣列 = 句物件.網出詞物件()
    #
    # 會-記-得  1-1-1
    # 會-記 得  1-1 2 後面沒連寫
    # 會 記-得  1 2-2 錯誤
    # 會 記 得  1 2 3 錯誤
    #
    環綴起始詞 = dict()
    for 詞位置, 詞物件 in enumerate(詞物件陣列):
        詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(詞的字物件陣列)

        for 字物件 in 詞的字物件陣列:
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
            if 是環綴起始(字分詞):
                環綴起始詞.update({'詞位置': 詞位置, '字陣列': 詞的字物件陣列})
            # 檢查環綴的書寫是否正確
            elif 是環綴結尾(字分詞) and 環綴起始詞 != None and 環綴起始詞['詞位置'] != 詞位置:
                環綴結尾詞 = 詞的字物件陣列
                # 會 記-得  1 2-2 錯誤
                if len(環綴起始詞['字陣列']) == 1:
                    錯誤行數 = 累積字長度
                    錯誤連字符位置 = '後'
                    錯誤訊息陣列.append(('E動詞（一）', 錯誤行數, 錯誤連字符位置))
                # 會-記 得  1-1 2 錯誤
                if len(環綴結尾詞) == 1:
                    錯誤行數 = 累積字長度
                    錯誤連字符位置 = '前'
                    錯誤訊息陣列.append(('E動詞（一）', 錯誤行數, 錯誤連字符位置))

        累積字長度 += 詞長度

    return 錯誤訊息陣列


def 是否符合咧原則(句物件):
    錯誤訊息陣列 = []
    累積字長度 = 0
    詞物件陣列 = 句物件.網出詞物件()
    總詞數 = len(詞物件陣列)
    前一个詞分詞 = None
    for 詞位置, 詞物件 in enumerate(詞物件陣列):
        詞的字物件陣列 = 詞物件.篩出字物件()
        詞長度 = len(詞的字物件陣列)
        詞分詞 = 詞物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
        是最後一個詞 = (詞位置+1 == 總詞數)
        for 字位置, 字物件 in enumerate(詞的字物件陣列):
            字分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()

            是咧 = (字分詞 in ('咧｜leh4', '咧｜teh4'))
            前半段的詞 = 詞(詞的字物件陣列[:字位置]).轉音(臺灣閩南語羅馬字拼音).看分詞()
            
            # 咧應和前面動詞連寫 徛咧講 => 徛-咧講
            # if 是咧 and 這個詞只有咧 and 前一個詞是動詞:
            if 是咧 and 詞長度 == 1 and 前一个詞分詞 and 是動詞(前一个詞分詞):
                錯誤行數 = 累積字長度 + 字位置 + 1
                錯誤連字符位置 = '前'
                錯誤訊息陣列.append(('E動詞（二）', 錯誤行數, 錯誤連字符位置))

            # 咧應和前面非動詞分寫 我-咧講 => 我咧講
            #  elif 是咧 and 這個詞的前半段不是動詞:
            elif 是咧 and not 是咧詞組(詞分詞) and not 是動詞(前半段的詞):
                錯誤行數 = 累積字長度 + 字位置 + 1
                錯誤連字符位置 = '前'
                錯誤訊息陣列.append(('E動詞（二）', 錯誤行數, 錯誤連字符位置))
            
            # 咧在句尾時和前面動詞分寫 徛-咧 => 徛咧/徛--咧
            # elif 是咧 and 是最後一個詞 and 前半段的詞是動詞 and 咧是最後一個字:
            elif 是咧 and (是最後一個詞 and 是動詞(前半段的詞) and 字位置 + 1 == 詞長度):
                錯誤行數 = 累積字長度 + 字位置 + 1
                錯誤連字符位置 = '前'
                錯誤訊息陣列.append(('E動詞（二）', 錯誤行數, 錯誤連字符位置))

            # 咧應和後面分寫 咧-講 => 咧講
            # if 是咧 and 這個詞的後半段還有字:
            if 是咧 and (詞長度 - 字位置 - 1 > 0):
                錯誤行數 = 累積字長度 + 字位置 + 1
                錯誤連字符位置 = '後'
                錯誤訊息陣列.append(('E動詞（二）', 錯誤行數, 錯誤連字符位置))

        累積字長度 += 詞長度
        前一个詞分詞 = 詞分詞
    return 錯誤訊息陣列


def 是否符合著原則(句物件):
    return None

def 是否符合時貌標誌原則(句物件):
    # 動詞原則二：動詞和後接時貌標誌連寫
    # 咧、著、過
    是否符合咧原則(句物件)
