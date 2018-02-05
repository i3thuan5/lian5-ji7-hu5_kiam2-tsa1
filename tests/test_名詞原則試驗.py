from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import pytest
from src.連字符檢查.名詞原則.名詞與單音節詞綴 import 是否符合原則


#
# 附註：由於「原則五_阿與後接人名連寫」，程式無法分出後面是否為人名；所以將原則五合併到原則一。
#
@pytest.mark.parametrize('漢字, 臺羅, 預期', [
    ('阿公', 'a-kong', None),
    ('阿公', 'a kong', [('E名詞（一）', 1, 'a-kong')]),
    ('椅仔', 'Í-á', None),
    ('椅仔', 'Í á', [('E名詞（一）', 1, 'Í-á')]),
    ('阿珠', 'A-tsu', None),
    ('阿珠', 'A tsu',  [('E名詞（一）', 1, 'A-tsu')]),
    ('初一', 'tshe-it', None),
    ('初一', 'tshe it',  [('E名詞（二）', 1, 'tshe-it')]),
    ('第十一', 'tē-tsa̍p-it', None),
    ('第十一', 'tē tsa̍p-it',  [('E名詞（二）', 1, 'tē-tsa̍p-it')]),
    ('山頂', 'suann-tíng', None),
    ('山頂', 'suann tíng', [('E名詞（三）', 1, 'suann-tíng')]),
    ('大門後壁', 'tuā-mn̂g āu-piah', None),
    ('大門後壁', 'tuā-mn̂g-āu-piah', [('E名詞（三）', 2, 'tuā-mn̂g āu-piah')]),
])
def test_名詞原則(漢字, 臺羅, 預期):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    assert 是否符合原則(句物件) == 預期
