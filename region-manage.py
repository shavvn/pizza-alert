import sys
import os
# This file create & maintain csv files where user emails are stored

region_list = ['dc', 'nyc', 'baltimore']


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
    if len(sys.argv) < 3:
        print('Please use "python csv.py add dc email1@gmail.com " to add a user')
        print('Please use "python csv.py del efg@gmail.com" to delete a user')
        exit(0)
    else:
        if sys.argv[1] == 'add':
            if sys.argv[2] in region_list:
                add_new_user(sys.argv[3], sys.argv[2])
            else:
                print('Invalid argument! Use "python csv.py -h" for help')
                exit(0)
        elif sys.argv[1] == 'del':
            for region in region_list:
                delete_user(sys.argv[2], region)
        elif sys.argv[1] == '-h':
            # TODO should print out the help info here.. but who cares..
            # oh it will probably never get here...
            print('under construction... ')
        else:
            print('Invalid argument! Use "python csv.py -h" for help')
            exit(0)

