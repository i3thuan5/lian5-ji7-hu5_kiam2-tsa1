import pytest
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


@pytest.mark.parametrize('漢字, 臺羅, 預期', [
    # 虛詞原則一：介詞與前後詞分寫
    ('伊佇頭前', 'I tī thâu-tsîng', None),
    ('伊佇頭前', 'I-tī thâu-tsîng', [('E虛詞（一）', 2, 'I tī')]),
    ('伊佇頭前', 'I--tī thâu-tsîng', [('E虛詞（一）', 2, 'I tī')]),
    ('伊佇頭前', 'I tī-thâu-tsîng', [('E虛詞（一）', 2, 'tī thâu-tsîng')]),
    ('伊佇頭前', 'I tī--thâu-tsîng', [('E虛詞（一）', 2, 'tī thâu-tsîng')]),
    ('講予你知', 'kóng hōo lí tsai', None),
    ('講予你知', 'kóng hōo--lí tsai', [('E虛詞（一）', 2, 'kóng hōo lí tsai')]),
    # 虛詞原則二：連詞語前後詞分寫 
    # 佮、閣、抑、愈
    ('頭家佮辛勞', 'Thâu-ke kah sin-lô', None),
    ('頭家佮辛勞', 'Thâu-ke-kah sin-lô', [('E虛詞（二）', 2, 'Thâu-ke kah sin-lô')]),
    ('頭家佮辛勞', 'Thâu-ke kah-sin-lô', [('E虛詞（二）', 2, 'Thâu-ke kah sin-lô')]),
    ('頭家佮辛勞', 'Thâu-ke-kah-sin-lô', [('E虛詞（二）', 2, 'Thâu-ke kah sin-lô')]),
    ('頭家佮辛勞', 'Thâu-ke--kah sin-lô', [('E虛詞（二）', 2, 'Thâu-ke kah sin-lô')]),
    ('愈來愈乖', 'Jú lâi-jú kuai', [('E虛詞（二）', 3, 'Jú lâi jú kuai')]),
    ('愈來愈乖', 'Jú-lâi jú kuai', [('E虛詞（二）', 1, 'Jú lâi jú kuai')]),
    ('愈來愈乖', 'Jú-lâi-jú kuai', [('E虛詞（二）', 1, 'Jú lâi jú kuai'), ('E虛詞（一）', 3, 'Jú lâi jú kuai')]),
    ('愈來愈乖', 'Jú lâi jú-kuai', [('E虛詞（二）', 3, 'Jú lâi jú kuai')]),
    ('愈來愈乖', 'Jú lâi-jú-kuai', [('E虛詞（二）', 3, 'Jú lâi jú kuai')]),
    # 虛詞原則三：結構助詞
    # 的
    ('你的物件', '', None),
    ('你的物件', '', None),
    # 虛詞原則四：嘆詞與後面語詞分寫
    # 喔、Hngh8
    ('喔！是你', 'Ooh! Sī lí!', None),
    ('喔是你', 'Ooh Sī lí!', None),
    ('是你喔', 'Sī lí--ooh', None),
    ('喔是你', 'Ooh-Sī lí!', [('E虛詞（四）', 1, 'Ooh Sī lí!')]),
    # 虛詞原則五：結構助詞
    # 否、未、無、啥
    ('有錢無', 'Ū tsînn bô', None),
    ('有錢無', 'Ū tsînn-bô', [('E虛詞（五）', 3, 'Ū tsînn bô')]),
    ('有錢無', 'Ū tsînn--bô', None),
])
def test_虛詞原則(漢字, 臺羅, 預期):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    assert 是否符合原則(句物件) == 預期
