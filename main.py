import Reader
import Viewer


def main():
    """ Testing different methods """
    document = '140228202800-6ef39a241f35301a9a42cd0ed21e5fb0'
    plot_countries, country_group = Viewer.Display_countries(document)
    plot_continents = Viewer.Display_continents(country_group)
    plot_browser = Viewer.Display_browser(document)
    top10 = Reader.top10()
    print(top10)
    return 0


if __name__ == "__main__":
    main()
