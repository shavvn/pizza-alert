import sys
import os
import argparse
# This file create & maintain csv files where user emails are stored

region_list = ['dc', 'nyc', 'baltimore', 'philly']


def add_new_user(email, region):
    csv_file_name = region+'.csv'
    # if region file exists, append, otherwise create region file
    if os.path.exists('./'+csv_file_name):
        csv_file = open(csv_file_name, 'a')
    else:
        csv_file = open(csv_file_name, 'w+')
    csv_file.write(email + '\n')
    csv_file.close()
    # TODO send a welcome email to new user?


def delete_user(email, region):
    # TODO delete from the file
    print("under construction...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add or delete users for a region'
                                                 '(in a csv file), use -h for usage')
    parser.add_argument('email', nargs='+', help='user email to be added')
    parser.add_argument('--region', nargs=1, required=True, choices=region_list, help='region to be subscribed')
    parser.add_argument('-a', dest='action', action='store_const', const='add', help='add')
    parser.add_argument('-d', dest='action', action='store_const', const='del', help='delete user')
    args = parser.parse_args(sys.argv[1:])
    if args.action in 'add':
        print 'add user ' + str(args.email) + ' to ' + str(args.region)
        for each_user in args.email:
            add_new_user(each_user, args.region[0])
    else:
        print 'delete user ' + str(args.email) + ' from ' + str(args.region)
        for each_user in args.email:
            delete_user(each_user, args.region[0])

