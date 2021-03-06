import Reader
import Viewer
import AlsoLikes


def main():
    """ Testing different methods """
    document = '140204115519-f5fa6ce8b288c9f10e0c8bc7e1a456a0'
    user = '2f63e0cca690da91'
    country_group, df = Viewer.Get_countries(document)
    print(country_group)
    continents = Viewer.Get_continents(df)
    print(continents)
    browsers = Viewer.Get_browser_clean(document)
    print(browsers)

    documents = AlsoLikes.userHasRead(user)
    print('The user has read')
    print(documents)
    print('Document 1 has been read by')
    users = AlsoLikes.findReaders(documents[0])
    print(users)
    print('Users who like document 1 also like')
    alsoDocs = AlsoLikes.alsoLikes(documents[0], None, AlsoLikes.sortDocumentsAsc)
    print(alsoDocs)
    alsoDocs = AlsoLikes.alsoLikes(documents[0], None, AlsoLikes.sortDocumentsDesc)
    print(alsoDocs)

    top10 = Reader.top10()
    print(top10)

    incorrect_document = 1
    incorrect_user = 5
    country_group, df = Viewer.Get_countries(incorrect_document)
    print(country_group)
    continents = Viewer.Get_continents(df)
    print(continents)
    browsers = Viewer.Get_browser_clean(incorrect_document)
    print(browsers)

    top10 = Reader.top10(database='incorrect')
    print(top10)

    documents = alsoLikes.userHasRead(incorrect_user)
    print('The user has read')
    print(documents)
    print('Document 1 has been read by')
    users = alsoLikes.findReaders(documents[0])
    print(users)
    print('Users who like document 1 also like')
    alsoDocs = alsoLikes.alsoLikes(documents[0], None, alsoLikes.sortDocumentsAsc)
    print(alsoDocs)
    alsoDocs = alsoLikes.alsoLikes(documents[0], None, alsoLikes.sortDocumentsDesc)
    print(alsoDocs)

    return 0


if __name__ == "__main__":
    main()
