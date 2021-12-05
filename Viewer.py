import pandas as pd
import pycountry_convert as cconv


def Get_countries(document, database='issuu_cw2.json'):
    df = views(document, database)
    country_group = df.groupby(['visitor_country']).size()
    if country_group.empty:
        country_group = 'No views for this document'
    return country_group, df


def Get_continents(df):
    if df.empty:
        return 'No views for this document'
    continents = pd.DataFrame(df['visitor_country']).applymap(cconv.country_alpha2_to_continent_code)
    continent_groups = continents.groupby(['visitor_country']).size()
    return continent_groups


def Get_browser(document, database='issuu_cw2.json'):
    df = views(document, database)
    df.visitor_useragent = df.visitor_useragent.str.split('/').str[0]
    browsers = df.groupby(['visitor_useragent']).size()
    if browsers.empty:
        browsers = 'No views for this document'
    return browsers


def views(document, database='issuu_cw2.json'):
    df = pd.read_json(database, lines=True)
    df = df[df.subject_doc_id == document]
    df = df[df.event_type == 'read']
    return df
