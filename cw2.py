## Example 1
import argparse

import matplotlib.pyplot as plt

import Reader
import Viewer
import alsoLikes

parser = argparse.ArgumentParser(prog='cw2', description='Perform tasks for F21SC cw2.',
                                 usage='%(prog)s -u user_uuid -d doc_uuid -t task_id -f file_name')
parser.add_argument('-u',
                    metavar='user_uuid',
                    type=str,
                    default=None,
                    action='store',
                    help='the user_uuid required.')

parser.add_argument('-d',
                    metavar='doc_uuid',
                    type=str,
                    action='store',
                    help='the doc_uuid required.')

parser.add_argument('-t',
                    metavar='task_id',
                    type=str,
                    action='store',
                    help='the task_id required.')

parser.add_argument('-f',
                    metavar='file_name',
                    type=str,
                    action='store',
                    help='the file_name required.')

args = parser.parse_args()

if args.t == '2a':
    countries, _ = Viewer.Get_countries(args.d, args.f)
    ax1 = plt.gca()
    if type(countries) is not str:
        countries.plot(kind='bar', ax=ax1)
        ax1.set_ylabel('Number of viewers')
        ax1.set_xlabel('Countries')
        ax1.set_title('Views by country')
        plt.show()
    else:
        print(countries)

elif args.t == '2b':
    _, countries = Viewer.Get_countries(args.d, args.f)
    continents = Viewer.Get_continents(countries)
    ax1 = plt.gca()
    if type(continents) is not str:
        continents.plot(kind='bar', ax=ax1)
        ax1.set_ylabel('Number of viewers')
        ax1.set_xlabel('Continents')
        ax1.set_title('Views by Continents')
        plt.show()
    else:
        print(continents)

elif args.t == '3a':
    browsers = Viewer.Get_browser(args.d, args.f)
    ax1 = plt.gca()
    if type(browsers) is not str:
        browsers.plot(kind='bar', ax=ax1)
        ax1.set_ylabel('Number of viewers')
        ax1.set_xlabel('Browsers')
        ax1.set_title('Views by Browsers')
        plt.show()
    else:
        print(browsers)

elif args.t == '3b':
    browsers = Viewer.Get_browser_clean(args.d, args.f)
    ax1 = plt.gca()
    if type(browsers) is not str:
        browsers.plot(kind='bar', ax=ax1)
        ax1.set_ylabel('Number of viewers')
        ax1.set_xlabel('Browsers')
        ax1.set_title('Views by Browsers')
        plt.show()
    else:
        print(browsers)

elif args.t == '4':
    top10 = Reader.top10(args.f)
    print(top10)

elif args.t == '5d':
    likes = alsoLikes.alsoLikes(args.d, args.u, database=args.f)
    print(likes)

elif args.t == '6':
    graph = alsoLikes.buildGraph(args.d, args.u, database=args.f)
    graph.render()

# elif args.t == '7':
#     root = Tk()
#     gui = MyGUIInterface(root)
#     gui.document_also = args.d
#     gui.user_also = args.u
#     gui.database_also = args.f
#     gui.graph_alsoLikes()
#     root.mainloop()
