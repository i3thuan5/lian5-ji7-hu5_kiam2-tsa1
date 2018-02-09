

def 是否介詞(字分詞):
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