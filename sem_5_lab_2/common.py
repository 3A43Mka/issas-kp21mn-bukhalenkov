def common(list1, list2):
    return list(set(list1).intersection(list2))


def test_cases():
    assert sorted(common(['a', 'b', 'c'], ['c', 'a', 'z'])) == ['a', 'c']
    assert sorted(common(['a', 'b', 'c'], ['x', 'y', 'z'])) == []
    assert sorted(common(['a', 'a', 'b'], ['x', 'a', 'a'])) == ['a']
