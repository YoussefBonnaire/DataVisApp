import Reader
import Viewer
import alsoLikes

def main():
    """ Testing different methods """
    document = '140228202800-6ef39a241f35301a9a42cd0ed21e5fb0'
    user = 'dd326898d5605e63'
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
    users=alsoLikes.findReaders(documents[0])
    print(users)
    #top10 = Reader.top10()
    #print(top10)
    return 0


if __name__ == "__main__":
    main()
