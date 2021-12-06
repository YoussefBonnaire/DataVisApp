from collections import Counter

import graphviz
import numpy

import Viewer as v


#  Returns the a list of visitor ids for the users
#  that have visited the document
def findReaders(document):
    df = v.views(document)
    users = df['visitor_uuid']
    return users.values


#  Takes a visitorid and returns a list of documents
#  they have visited as a list of ids
def userHasRead(user):
    df = v.dataset.copy()
    df = df[df.visitor_uuid == user]
    df = df[df.event_type == 'read']
    documents = df['env_doc_id']
    return documents.values


#  Takes a list of document ids and sorts them
def sortDocuments(documents):
    documents.sort(key=Counter(documents).get, reverse=True)
    documents = list(dict.fromkeys(documents))
    return documents


#  Takes a document and optionally a user and a sorting function
#  and returns a list of the ten documents that have been
#  read by the most users, sorted with the inputted sorting algorithm
#  that have also read the input document
def alsoLikes(document, user=None, sortF=None):
    users = findReaders(document)
    if user is not None:
        numpy.append(users, user)
    documents = []
    for user in users:
        userDocs = userHasRead(user)
        documents.extend(userDocs)
    if sortF is None:
        documents = sortDocuments(documents)[:9]
    else:
        documents = sortF(documents)[:9]
    return documents


#
def buildGraph(documentIn, userIn=None, sortF=None):
    documents = alsoLikes(documentIn, userIn, sortF)
    graph = graphviz.Graph
    addedUsers = []
    graph.node('Readers', 'Readers', shape='plaintext', rank='Readers')
    graph.node('Documents', 'Documents', shape='plaintext', rank='Documents')
    graph.edge('Readers', 'Documents')
    for document in documents:
        docNodeLabel = document[41:45]
        if document == documentIn:
            graph.node(document, docNodeLabel, color='green', shape='circle', rank='Readers')
        else:
            graph.node(document, docNodeLabel, shape='circle', rank='Readers')
        users = findReaders(document)
        for user in users:
            userNodeLabel = user[11:15]
            if not addedUsers.__contains__(user):
                if user == userIn:
                    graph.node(user, docNodeLabel, color='green', shape='box', rank='Readers')
                else:
                    graph.node(user, docNodeLabel, shape='box', rank='Readers')
            graph.edge(user, document)

    return graph
