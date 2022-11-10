from inverted_index import build_inverted_index, search_in_inverted_index
import json


f = open("./documents.json")
documents = json.load(f)
built_inverted_index = build_inverted_index(documents)


def test1():
    assert search_in_inverted_index(built_inverted_index, 'performed') == [3, 4]


def test2():
    assert search_in_inverted_index(built_inverted_index, 'reactjs') == []


def test3():
    assert search_in_inverted_index(built_inverted_index, 'delicate') == [2]


def test4():
    assert search_in_inverted_index(built_inverted_index, 'chief') == [1, 2]


def test5():
    assert search_in_inverted_index(built_inverted_index, 'attention') == [1, 3, 4]


def test6():
    assert search_in_inverted_index(built_inverted_index, 'opinions') == [1]
