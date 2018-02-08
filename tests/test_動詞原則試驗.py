import pytest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


@pytest.mark.parametrize('漢字, 臺羅, 預期', [
    # 動詞原則一：動詞與環綴連寫
    ('會記得', 'ē-kì-tit', None),
    ('會記得', 'ē kì-tit', [('E動詞（一）', 1, 'ē kì-tit')]),
    ('會記得', 'ē-kì tit', None),
    ('媠姑娘會記得你', 'Suí koo-niû ē-kì tit lí', [('E動詞（一）', 3, 'Suí koo-niû ē kì-tit lí')]),
    ('袂曉得', 'bē-hiáu--tit', None),
    ('袂曉得', 'bē hiáu--tit', [('E動詞（一）', 1, 'bē-hiáu--tit')]),
    # 動詞原則二：動詞和後接的時貌標誌連寫
    ('徛咧', 'Khiā--leh', None),
    ('徛咧', 'Khiā leh', [('E動詞（二）a', 1, 'Khiā--leh')]),
    ('徛咧', 'Khiā-leh', [('E動詞（二）a', 1, 'Khiā--leh')]),
    ('徛咧', 'Khiā --leh', [('E輕聲符', 1, 'Khiā--leh')]),
    ('徛咧講', 'Khiā-leh kóng', None),
    ('徛咧講', 'Khiā leh-kóng', [('E動詞（二）b', 1, 'Khiā-leh kóng')]),
    ('徛咧講', 'Khiā leh kóng', [('E動詞（二）b', 1, 'Khiā-leh kóng')]),
    ('徛咧講', 'Khiā-leh-kóng', [('E動詞（二）b', 1, 'Khiā-leh kóng')]),
    ('徛咧講', 'Khiā--leh kóng', [('E動詞（二）b', 1, 'Khiā-leh kóng')]),
    ('徛咧講', 'Khiā --leh kóng', [('E輕聲符', 1, 'Khiā-leh kóng')]),
    ('來過遮', 'Lâi-kuè tsia', None),
    ('來過矣', 'lâi--kuè--ah', None),
    ('捌來過。', 'bat lâi--kuè.', None),
    ('飛過來', 'pue--kè-lâi', None),
    ('飛過來遮', 'Pue kuè-lâi tsia', None),
    ('看過三本冊', 'Khuànn--kuè sann pún tsheh',
     [('E動詞（二）b', 1, 'Khuànn-kuè sann')]),
    # 原則三
    # a) 單音節動詞（形容詞）接單音節補語，須連寫
    # b) 動詞（形容詞）接補語時，若不是都是單音節，須分寫
    ('講煞', 'Kóng-suah', None),
    ('講煞', 'Kóng suah',  [('E動詞（三）a', 1, 'Kóng-suah')]),
    ('寫了', 'Siá-liáu', None),
    ('講好', 'Kóng-hó', None),
    ('整理好', 'Tsíng-lí hó', None),
    ('整理好', 'Tsíng-lí-hó', [('E動詞（三）b', 1, 'Tsíng-lí hó')]),
    ('整理好勢', 'Tsíng-lí hó-sè', None),
    ('整理好勢', 'Tsíng-lí-hó-sè', [('E動詞（三）b', 1, 'Tsíng-lí hó-sè')]),
    ('排做伙', 'Pâi tsò-hué', None),
    ('排做伙', 'Pâi-tsò-hué',  [('E動詞（三）b', 1, 'Pâi tsò-hué')]),
    # 好：當前面接非動詞
    ('真好', 'tsin hó', None),
    ('你好', 'lí hó', None),
])
def test_動詞原則(漢字, 臺羅, 預期):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    assert 是否符合原則(句物件) == 預期
