import Viewer
import alsoLikes
import graphviz

def main():
    """ Testing different methods """
    document = '140228202800-6ef39a241f35301a9a42cd0ed21e5fb0'
    user = '2f63e0cca690da91'
    country_group, df = Viewer.Get_countries(document)
    print(country_group)
    continents = Viewer.Get_continents(df)
    print(continents)
    browsers = Viewer.Get_browser(document)
    print(browsers)

    documents = alsoLikes.userHasRead(user)
    print('The user has read')
    print(documents)
    print('Document 1 has been read by')
    users = alsoLikes.findReaders(documents[0])
    print(users)
    alsoDocs = alsoLikes.alsoLikes(documents[0])
    print('Users who like document 1 also like')
    print(alsoDocs)
    graph = alsoLikes.buildGraph(documents[0])
    graph.render('test',view=True)
    # top10 = Reader.top10()
    # print(top10)
    return 0


if __name__ == "__main__":
    main()
