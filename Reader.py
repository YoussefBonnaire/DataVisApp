# Reader profiles: In order to develop a readership profile for the site, we want to identify the most
# avid readers. We want to determine, for each user, the total time spent reading documents. The top 10
# readers, based on this analysis, should be printed.
import pandas as pd

dataset = pd.read_json('issuu_cw2.json', lines=True)

def top10():
    df = dataset.copy()
    df = df[df.event_type == 'pagereadtime']
    user_times = pd.DataFrame(df.groupby('visitor_uuid').event_readtime.sum()).nlargest(10,'event_readtime')
    return user_times
