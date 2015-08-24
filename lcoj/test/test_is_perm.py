from lcoj.is_perm import is_perm


def test_short_perm():
    assert is_perm('ab', 'ba')


def test_long_perm():
    assert is_perm('abcdefg', 'gfedcba')


def test_short_not_perm():
    assert not is_perm('ab', 'ab')


def test_long_not_perm():
    assert not is_perm('abcdefg', 'gfddcba')
