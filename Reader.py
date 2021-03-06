# Reader profiles: In order to develop a readership profile for the site, we want to identify the most
# avid readers. We want to determine, for each user, the total time spent reading documents. The top 10
# readers, based on this analysis, should be printed.
import pandas as pd


def top10(database='issuu_cw2.json'):
    df = pd.read_json(database, lines=True)
    df = df[df.event_type == 'pagereadtime']
    df.rename(columns={'event_readtime': 'Total time spent reading', 'visitor_uuid': 'User Id'}, inplace=True)
    user_times = pd.DataFrame(df.groupby('User Id')['Total time spent reading'].sum()).nlargest(10,
                                                                                                'Total time spent '
                                                                                                'reading')
    user_times = user_times.reset_index()
    return user_times
