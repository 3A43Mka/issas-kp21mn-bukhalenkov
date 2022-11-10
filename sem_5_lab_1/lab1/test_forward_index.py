from forward_index import build_forward_index, search_in_forward_index
import json


f = open("./documents.json")
documents = json.load(f)
built_forward_index = build_forward_index(documents)


def test_index_structure():
    assert built_forward_index == [
        {'id': 1, 'words': ['opinions', 'resolved', 'friendly', 'sufficient', 'law', 'chatty', 'chief', 'attention']},
        {'id': 2, 'words': ['delicate', 'landlord', 'dashwood', 'farther', 'frankness', 'juvenile', 'chief']},
        {'id': 3, 'words': ['tiled', 'attention', 'cold', 'sake', 'assure', 'performed', 'discourse', 'marriage', 'blessing']},
        {'id': 4, 'words': ['greatest', 'performed', 'invitation', 'difficulty', 'solicitude', 'attention']}]


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
