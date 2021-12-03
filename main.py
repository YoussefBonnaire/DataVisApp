import Reader
import Viewer


def main():
    """ Testing different methods """
    document = '140228202800-6ef39a241f35301a9a42cd0ed21e5fb0'
    country_group, df = Viewer.Get_countries(document)
    print(country_group)
    continents = Viewer.Get_continents(df)
    print(continents)
    browsers = Viewer.Get_browser(document)
    print(browsers)

    top10 = Reader.top10()
    print(top10)
    return 0


if __name__ == "__main__":
    main()
