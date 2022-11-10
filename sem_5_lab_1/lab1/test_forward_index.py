from forward_index import build_forward_index, search_in_forward_index
import json


f = open("./documents.json")
documents = json.load(f)
built_forward_index = build_forward_index(documents)


def test1():
    assert search_in_forward_index(built_forward_index, 'performed') == [3, 4]


def test2():
    assert search_in_forward_index(built_forward_index, 'reactjs') == []


def test3():
    assert search_in_forward_index(built_forward_index, 'delicate') == [2]


def test4():
    assert search_in_forward_index(built_forward_index, 'chief') == [1, 2]


def test5():
    assert search_in_forward_index(built_forward_index, 'attention') == [1, 3, 4]


def test6():
    assert search_in_forward_index(built_forward_index, 'opinions') == [1]
