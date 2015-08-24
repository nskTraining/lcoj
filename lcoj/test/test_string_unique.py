from lcoj.string_unique import all_unique


def test_one_char():
    assert all_unique('a')


def test_long_string_unique():
    assert all_unique('abcdefghi')


def test_long_not_unique():
    assert not all_unique('abcdefgrtyuia')


def test_short_not_unique():
    assert not all_unique('aa')
