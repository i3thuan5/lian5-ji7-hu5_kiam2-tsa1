import pytest


# pytest 支援中文函式單獨測試
# `pytest -k test_is_word_中文['a1'-True]` works.
@pytest.mark.parametrize('word, expected', [
    ('a1', True),
])
def test_is_word_中文(word, expected):
    assert word == expected


# pytest 支援中文引數單獨測試
# `pytest -k test_is_word['a1'-True]` works.
@pytest.mark.parametrize('中文, 預期', [
    ('a1', True),
])
def test_is_word(中文, 預期):
    assert 中文 == 預期


# pytest 不支援中文參數！
# `pytest -k test_is_word_zh_param['中文'-True]` will error
@pytest.mark.parametrize('word, expected', [
    ('中文', True),
])
def test_is_word_zh_param(word, expected):
    assert word == expected
