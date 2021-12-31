import argparse
from getpass import getpass

import configHandler


betawatchVersion = '0.1.0'
betawatchDescription =\
'''
This program is made for Employees or Students with an account at the Hochschule Furtwangen University. It allows the user to easily enter an alfaview room without having to open their browser and type in the credentials every time.
'''

parser = argparse.ArgumentParser(description=betawatchDescription, prog='betawatch')
parser.add_argument('--version', action='version', version='%(prog)s ' + betawatchVersion)
parser.add_argument('room', nargs='?')
parser.add_argument('-u', '--username',
    help='Specify your HFU account username')
parser.add_argument('-p', '--password',
    help='Specify your HFU account password')
parser.add_argument('-n', '--displayName',
    help='Specify the name that should be shown in Alfaview')
parser.add_argument('--config',
    action='store_true',
    help='Edit the configuration file')
parser.add_argument('--noUI',
    action='store_true',
    help='Execute this script in the terminal only')
args = parser.parse_args()



def openAlfaview(room, username, password, displayName):
    print('TODO: OPEN Alfaview')


def editConfig():
    config = configHandler.getConfig()

    # set room
    print()
    print('What room do you want to join by default?')
    if config['myRoom'] == None:
        print('Enter value or press ENTER to skip: ', end='')
    else:
        print('Enter value or press ENTER to keep current value (', config['myRoom'] ,'): ', sep='', end='')
    tmp_room = input()
    if tmp_room != '':
        config['myRoom'] = tmp_room

    # set username
    print()
    print('Your HFU account username?')
    if config['myUsername'] == None:
        print('Enter value or press ENTER to skip: ', end='')
    else:
        print('Enter value or press ENTER to keep current value (', config['myUsername'] ,'): ', sep='', end='')
    tmp_username = input()
    if tmp_username != '':
        config['myUsername'] = tmp_username

    # set password
    print()
    print('Your HFU account password?')
    if config['myPassword'] == None:
        print('Enter value or press ENTER to skip: ', end='')
    else:
        print('Enter value or press ENTER to keep current value (', config['myPassword'] ,'): ', sep='', end='')
    tmp_password = input()
    if tmp_password != '':
        config['myPassword'] = tmp_password

    # set displayName
    print()
    print('What should we call you?')
    if config['myName'] == None:
        print('Enter value or press ENTER to skip: ', end='')
    else:
        print('Enter value or press ENTER to keep current value (', config['myName'] ,'): ', sep='', end='')
    tmp_displayName = input()
    if tmp_displayName != '':
        config['myName'] = tmp_displayName

    configHandler.setConfig(config)


def startGUI():
    print('TODO: START GUI')


def main():
    if args.config:
        editConfig()

    if not args.noUI and args.room == None and args.username == None and args.password == None and args.displayName == None and not args.config:
        startGUI()

    config = configHandler.getConfig()

    if args.room != None:
        config['myRoom'] = args.room
    if args.username != None:
        config['myUsername'] = args.username
    if args.password != None:
        config['myPassword'] = args.password
    if args.displayName != None:
        config['myName'] = args.displayName

    if config['myRoom'] == None:
        config['myRoom'] = input('What room do you want to join?: ')
    if config['myUsername'] == None:
        config['myUsername'] = input('Your HFU account username: ')
    if config['myPassword'] == None:
        config['myPassword'] = getpass('Your HFU account password: ')
    if config['myName'] == None:
        config['myName'] = input('What should we call you?: ')

    openAlfaview(args.room, args.username, args.password, args.displayName)


if __name__ == "__main__":
    main()
