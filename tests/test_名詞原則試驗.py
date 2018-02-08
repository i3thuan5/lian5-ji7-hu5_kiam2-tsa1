from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import pytest
from src.連字符檢查.名詞原則.名詞與單音節詞綴 import 是否符合原則


#
# 附註：
#
@pytest.mark.parametrize('漢字, 臺羅, 預期', [
    # 名詞原則一：名詞與單音節的前中後詞綴連寫
    # 名詞原則五：阿與後接人名連寫。
    # 程式無法分出後面是否為人名；所以將原則五合併到原則一。
    ('阿公', 'a-kong', None),
    ('阿公', 'a kong', [('E名詞（一）', 1, 'a-kong')]),
    ('阮阿公', 'guán a kong', [('E名詞（一）', 2, 'a-kong')]),
    ('椅仔', 'Í-á', None),
    ('椅仔', 'Í á', [('E名詞（一）', 1, 'Í-á')]),
    ('阿珠', 'A-tsu', None),
    ('阿珠', 'A tsu',  [('E名詞（一）', 1, 'A-tsu')]),
    # 名詞原則二：序列詞頭與後接數字連寫
    ('初一', 'tshe-it', None),
    ('初一', 'tshe it',  [('E名詞（二）a', 1, 'tshe-it')]),
    ('第十一', 'tē-tsa̍p-it', None),
    ('第十一', 'tē tsa̍p-it',  [('E名詞（二）a', 1, 'tē-tsa̍p-it')]),
    ('第一千三百五十', 'Tē tsi̍t-tshing sann-pah gōo-tsa̍p',  None),
    # 名詞原則三：
    # a)單音節方位詞，和前面名詞連寫 
    # b)雙音節方位詞，和前面名詞分寫
    ('椅仔頂', 'Í-á-tíng', None),
    ('椅仔頂', 'Í-á tíng', [('E名詞（三）a', 1, 'Í-á-tíng')]),
    ('大門後壁', 'tuā-mn̂g āu-piah', None),
    ('大門後壁', 'tuā-mn̂g-āu-piah', [('E名詞（三）b', 1, 'tuā-mn̂g āu-piah')]),
    # 混合試驗名詞原則
    ('阿公初一', 'A kong tshe it',  [
     ('E名詞（一）', 1, 'A-kong'), ('E名詞（二）', 3, 'tshe-it')
     ]),
])
def test_名詞原則(漢字, 臺羅, 預期):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    assert 是否符合原則(句物件) == 預期
