import pandas as pd
import pycountry_convert as cconv


# Takes in string for document and optionally database and returns grouped-by pandas dataframe to plot viewers by
# country and a dataframe for continents to use.
def Get_countries(document, database='issuu_cw2.json'):
    df = views(document, database)
    country_group = df.groupby(['visitor_country']).size()
    if country_group.empty:
        country_group = 'No views for this document'
    return country_group, df


# Takes in dataframe produced by Get_countries and outputs the continent version to plot the viewers by continent
def Get_continents(df):
    if df.empty:
        return 'No views for this document'
    continents = pd.DataFrame(df['visitor_country']).applymap(cconv.country_alpha2_to_continent_code)
    continent_groups = continents.groupby(['visitor_country']).size()
    return continent_groups


# Takes in string for document and optionally database and returns grouped-by pandas dataframe to plot viewers by
# browser
def Get_browser(document, database='issuu_cw2.json'):
    df = views(document, database)
    df.visitor_useragent = df.visitor_useragent.str.split('/').str[0]
    browsers = df.groupby(['visitor_useragent']).size()
    if browsers.empty:
        browsers = 'No views for this document'
    return browsers


# Helper function to reduce duplicate lines
def views(document, database='issuu_cw2.json'):
    df = pd.read_json(database, lines=True)
    df = df[df.subject_doc_id == document]
    df = df[df.event_type == 'read']
    return df
