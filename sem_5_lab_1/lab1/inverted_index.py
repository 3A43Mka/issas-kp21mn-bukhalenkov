import json


def build_inverted_index(docs):
    built_index = {}
    for doc in docs:
        words = get_keywords_from_doc(doc)
        for word in words:
            if word not in built_index:
                built_index[word] = []
            built_index[word].append(get_id_from_doc(doc))
    return built_index


def get_id_from_doc(doc):
    return doc['id']


def get_keywords_from_doc(doc):
    return doc['keywords']


def search_in_inverted_index(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return []


def main():
    f = open('./documents.json')
    documents = json.load(f)
    built_inverted_index = build_inverted_index(documents)
    print(built_inverted_index)
    results = search_in_inverted_index(built_inverted_index, 'marriage')
    print(results)


main()