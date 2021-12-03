import pandas as pd
import Viewer as v

def findReaders(document):
    df = v.views(document)
    users = df['visitor_uuid']
    return users

def userHasRead(user):
    df = v.dataset.copy()
    df = df[df.visitor_uuid == user]
    df = df[df.event_type == 'read']
    return df

