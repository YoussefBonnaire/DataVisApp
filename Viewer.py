import matplotlib as plt
import pandas as pd
import pycountry_convert as cconv

# We want to analyse, for a given document, from which countries and
# continents the document has been viewed. The data should be displayed as a histogram of countries,
# i.e. counting the number of occurrences for each country in the input file.
# The application should take a string as input, which uniquely specifies a document (a document
# UUID), and return a histogram of countries of the viewers. The histogram can be displayed
# using matplotlib.

dataset = pd.read_json('issuu_cw2.json', lines=True)


def Get_countries(document):
    df = views(document)
    country_group = df.groupby(['visitor_country']).size()
    plt.rcParams["figure.figsize"] = [15, 10]
    try:
        ax = country_group.plot(kind='bar')
        ax.set_ylabel('Number of viewers')
        ax.set_xlabel('Countries')
        ax.set_title('Views by country')

        return plt.pyplot.show(), df
    except IndexError as error:
        raise Exception('No views for this file') from error


# Use the data you have collected in the previous task, group the countries by continent, and
# generate a histogram of the continents of the viewers. The histogram can be displayed using
# matplotlib.

def Get_continents(df):
    continents = pd.DataFrame(df['visitor_country']).applymap(cconv.country_alpha2_to_continent_code)
    continent_groups = continents.groupby(['visitor_country']).size()
    return continent_groups


# Views by browser: In this task we want to identify the most popular browser. To this end, the
# application has to examine the visitor useragent field and count the number of occurrences
# for each value in the input file.
# The application should return and display a histogram of all browser identifiers of the viewers
# In the previous task, you will see that the browser strings are very verbose, distinguishing
# browser by e.g. version and OS used. Process the input of the above task, so that only the
# main browser name is used to distinguish them (e.g. Mozilla), and again display the result as
# a histogram.

def Get_browser(document):
    df = views(document)
    df.visitor_useragent = df.visitor_useragent.str.split('/').str[0]
    browsers = df.groupby(['visitor_useragent']).size()
    plt.rcParams["figure.figsize"] = [15, 10]
    try:
        ax = browsers.plot(kind='bar')
        ax.set_ylabel('Number of viewers')
        ax.set_xlabel('browsers')
        ax.set_title('Views by Browser')
        return plt.pyplot.show()
    except IndexError as error:
        return 'No views for this file'


def views(document):
    df = dataset.copy()
    df = df[df.subject_doc_id == document]
    df = df[df.event_type == 'read']
    return df
