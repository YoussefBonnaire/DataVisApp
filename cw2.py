## Example 1
import argparse

import Viewer

parser = argparse.ArgumentParser(prog='cw2', description='Perform tasks for F21SC cw2.',
                                 usage='%(prog)s -u user_uuid -d doc_uuid -t task_id -f file_name')
parser.add_argument('-u',
                    metavar='user_uuid',
                    type=str,
                    default=None,
                    help='the user_uuid required.')

parser.add_argument('-d',
                    metavar='doc_uuid',
                    type=str,
                    help='the doc_uuid required.')

parser.add_argument('-t',
                    metavar='task_id',
                    type=str,
                    help='the task_id required.')

parser.add_argument('-f',
                    metavar='file_name',
                    type=str,
                    help='the file_name required.')

args = parser.parse_args()

if args.task_id == '2a':
    countries, _ = Viewer.Get_countries(args.doc_uuid)
