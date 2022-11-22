Information retrieval systems. Assignment 2. Forward and inverted indexes


Theoretical part
 
It is a data structure that stores mapping from words to documents or set of documents i.e. directs you from word to document.
Steps to build Inverted index are:
Fetch the document and gather all the words.
Check for each word, if it is present then add reference of document to index else create new entry in index for that word.
Repeat above steps for all documents and sort the words.
Indexing is slow as it first checks that word is present or not.
Searching is very fast.
Example of Inverted index:
Word                              Documents
hello                             doc1      
sky                               doc1, doc3
coffee                            doc2
hi                                doc2
greetings                         doc3                              
It does not store duplicate keywords in index.
Real life examples of Inverted index:
Index at the back of the book.
Reverse lookup
Forward Index:
It is a data structure that stores mapping from documents to words i.e. directs you from document to word.
Steps to build Forward index are:
Fetch the document and gather all the keywords.
Append all the keywords in the index entry for this document.
Repeat above steps for all documents
Indexing is quite fast as it only append keywords as it move forwards.
Searching is quite difficult as it has to look at every contents of index just to retrieve all pages related to word.
Example of forward index:
Document                          Keywords
doc1                              hello, sky, morning      
doc2                              tea, coffee, hi
doc3                              greetings, sky
It stores duplicate keywords in index. Eg: word “sky” is stored multiple times.
Real life examples of Forward index:
Table of contents in book.
DNS lookup
Similarity between Forward index and Inverted Index:
Both are used to search text in documents or sets of documents.
Tasks
      0.   Build unit-tests for the tasks below
Build forward index for a set of documents
Build inverted index  for a set of documents
Try to search information based on the indexes

Max: 20 points
DEADLINE Nov 15

