from collections import Counter

import Viewer as v


# Returns the a list of visitor ids for the users
# that have visited the document
def findReaders(document):
    df = v.views(document)
    users = df['visitor_uuid']
    return users.values


# Takes a visitorid and returns a list of documents
# they have visited as a list of ids
def userHasRead(user):
    df = v.dataset.copy()
    df = df[df.visitor_uuid == user]
    df = df[df.event_type == 'read']
    documents = df['env_doc_id']
    return documents.values


# takes a list of document ids and sorts them
def sortDocuments(documents):
    documents.sort(key=Counter(documents).get, reverse=True)
    documents = list(dict.fromkeys(documents))
    # The function didn't return anything so alsolikes wouldn't have sorted the documents (added it there)
    return documents


# Takes a document and returns a list of the
# ten documents that have been read by the most users
# that have also read the input document
def alsoLikes(document,sortF):
    users = findReaders(document)
    documents = []
    for user in users:
        # Not entirely sure views works on multiple documents but have not tested it on that at all so very well could
        userDocs = userHasRead(user)
        documents.extend(userDocs)
    # This may not work if sortDocuments is made for pandas df, you can test it the way I did in the main if you want
    if(sortF==None):
        documents = sortDocuments(documents)[:9]
    else:
        document= sortF(documents)[:9]
    return documents
