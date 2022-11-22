from inverted_index import build_inverted_index, search_in_inverted_index
import json


f = open("./documents.json")
documents = json.load(f)
built_inverted_index = build_inverted_index(documents)


def test_index_structure():
    assert built_inverted_index == {'opinions': [1],
                                    'resolved': [1],
                                    'friendly': [1],
                                    'sufficient': [1],
                                    'law': [1],
                                    'chatty': [1],
                                    'chief': [1, 2],
                                    'attention': [1, 3, 4],
                                    'delicate': [2],
                                    'landlord': [2],
                                    'dashwood': [2],
                                    'farther': [2],
                                    'frankness': [2],
                                    'juvenile': [2],
                                    'tiled': [3],
                                    'cold': [3],
                                    'sake': [3],
                                    'assure': [3],
                                    'performed': [3, 4],
                                    'discourse': [3],
                                    'marriage': [3],
                                    'blessing': [3],
                                    'greatest': [4],
                                    'invitation': [4],
                                    'difficulty': [4],
                                    'solicitude': [4]}


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
