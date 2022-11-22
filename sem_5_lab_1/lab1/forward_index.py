import json


def build_forward_index(docs):
    built_index = []
    for doc in docs:
        # print(doc)
        new_row = {'id': get_id_from_doc(doc), 'words': get_keywords_from_doc(doc)}
        built_index.append(new_row)
    return built_index


def search_in_forward_index(index, keyword):
    result_docs = []
    for index_row in index:
        if keyword in index_row['words']:
            result_docs.append(index_row['id'])
    return result_docs


def get_id_from_doc(doc):
    return doc['id']


def get_keywords_from_doc(doc):
    return doc['keywords']


def main():
    f = open('./documents.json')
    documents = json.load(f)
    built_forward_index = build_forward_index(documents)
    print(built_forward_index)
    results = search_in_forward_index(built_forward_index, 'performed')
    print(results)


main()
