from src.連字符檢查.教典.讀取原始檔 import 讀取原始檔


def 撈取詞組():
    字分詞陣列 = ['佮｜kah4', '佮｜kap4', '閣｜koh4']
    # 佮｜kah4 => 佮-喙｜kah4-tshui3, ...
    教典字典 = 讀取原始檔()
    結果 = set()
    for 一字分詞 in 字分詞陣列:
        for 詞分詞, 字分詞陣列 in 教典字典.items():
            if 一字分詞 in 字分詞陣列:
                結果.add(詞分詞)
    return 結果
                
        