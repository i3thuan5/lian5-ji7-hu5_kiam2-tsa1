import pytest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


@pytest.mark.parametrize('漢字, 臺羅, 預期', [
    ('會記得', 'ē-kì-tit', None),
    ('會記得', 'ē kì-tit', [('E動詞（一）', 1, 'ē kì-tit')]),
    ('媠姑娘會記得你', 'Suí koo-niû ē-kì tit lí', [('E動詞（一）', 3, 'ē kì-tit')]),
    ('袂曉得', 'bē-hiáu--tit', None),
    ('袂曉得', 'bē hiáu--tit', [('E動詞（一）', 1, 'bē-hiáu--tit')]),
    ('徛咧', 'Khiā--leh', None),
    ('徛咧講', 'Khiā-leh kóng', None),
    ('徛咧講', 'Khiā--leh kóng', None),
    ('徛咧講', 'Khiā --leh kóng', [('E動詞（二）a', 1, 'Khiā-leh')]),
    ('徛咧講', 'Khiā --leh-kóng', [('E動詞（二）a', 1, 'Khiā-leh')]),
    ('徛咧講', 'Khiā--leh-kóng', [('E動詞（二）a', 1, 'Khiā-leh')]),
    ('徛咧講', 'Khiā-leh-kóng', [('E動詞（二）b', 1, 'Khiā-leh kóng')]),
    #     (,,None),
    #     (,,None),
])
def test_名詞原則(漢字, 臺羅, 預期):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    assert 是否符合原則(句物件) == 預期
