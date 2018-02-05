from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import pytest
from src.連字符檢查.名詞原則.名詞與單音節詞綴 import 檢查單音節詞綴連寫


@pytest.mark.parametrize('漢字, 臺羅, 預期', [
    ('阿公', 'a-kong', None),
    ('阿公', 'a kong', ('E名詞（一）', 1)),
    ('椅仔', 'Í-á', None),
    ('椅仔', 'Í á', ('E名詞（一）', 1))
])
def test_原則一_單音節詞綴連寫(漢字, 臺羅, 預期):
    句物件 = 拆文分析器.對齊句物件(漢字, 臺羅)
    assert 檢查單音節詞綴連寫(句物件) == 預期
