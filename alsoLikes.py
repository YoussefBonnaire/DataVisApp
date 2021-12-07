from collections import Counter

import graphviz
import numpy
import pandas as pd

import Viewer as v


#  Returns the a list of visitor ids for the users
#  that have visited the document
def findReaders(document, database='issuu_cw2.json'):
    df = v.views(document, database)
    users = df['visitor_uuid']
    return users.values


#  Takes a visitorid and returns a list of documents
#  they have visited as a list of ids
def userHasRead(user, database='issuu_cw2.json'):
    df = pd.read_json(database, lines=True)
    df = df[df.visitor_uuid == user]
    df = df[df.event_type == 'read']
    documents = df['subject_doc_id']
    return documents.values


#  Takes a list of document ids and sorts them in descending order order
def sortDocumentsDesc(documents):
    documents.sort(key=Counter(documents).get, reverse=True)
    documents = list(dict.fromkeys(documents))
    return documents


#  Takes a list of document ids and sorts them in descending order order
def sortDocumentsAsc(documents):
    documents.sort(key=Counter(documents).get)
    documents = list(dict.fromkeys(documents))
    return documents


#  Find most read
def findTop(documents, documentIn):
    sorty = documents.copy()
    sorty.remove(documentIn)
    return sorty[0]


#  Takes a document and optionally a user and a sorting function
#  and returns a list of the ten documents that have been
#  read by the most users, sorted with the inputted sorting algorithm
#  that have also read the input document
def alsoLikes(document, userIn=None, sortF=sortDocumentsDesc, database='issuu_cw2.json'):
    users = findReaders(document, database=database)
    if userIn is not None:
        if users.__contains__(userIn):
            numpy.delete(users, userIn)
    documents = []
    for user in users:
        userDocs = userHasRead(user, database=database)
        documents.extend(userDocs)
    documents = sortF(documents)[:9]
    return documents


#  Takes a document and optionally a user and a sorting function
#  and returns a graph based on the documents returned by the alsoLikes
def buildGraph(documentIn, userIn=None, sortF=sortDocumentsDesc, database='issuu_cw2.json'):
    documents = alsoLikes(documentIn, userIn, sortF, database=database)
    graph = graphviz.Digraph()
    topDocument = findTop(documents, documentIn)

    graph.node('Documents', 'Documents', shape='plaintext', rank='Documents')
    graph.node('Readers', 'Readers', shape='plaintext', rank='Readers')
    graph.edge('Readers', 'Documents')
    addedUsers = findReaders(documentIn, database=database)
    for addedUser in addedUsers:
        userNodeLabel = addedUser[11:15]
        if addedUser == userIn:
            graph.node(addedUser, userNodeLabel, style='filled', color='green', shape='box', rank='Readers')
        else:
            graph.node(addedUser, userNodeLabel, shape='box', rank='Readers')

    for document in documents:
        docNodeLabel = document[41:45]
        if document == documentIn:
            graph.node(document, docNodeLabel, style='filled', color='green', shape='circle', rank='Readers')
        elif document == topDocument:
            graph.node(document, docNodeLabel, style='filled', color='red', shape='circle', rank='Readers')
        else:
            graph.node(document, docNodeLabel, shape='circle', rank='Readers')
        users = findReaders(document, database=database)
        for user in users:
            if addedUsers.__contains__(user):
                graph.edge(user, document)
    graph.format = 'png'
    return graph
