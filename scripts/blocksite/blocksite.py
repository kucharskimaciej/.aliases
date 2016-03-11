#!/usr/bin/python3
from modules.hosts import Hosts
from modules.blocked_sites import BlockedSites
from os import path


def current_path():
    return path.dirname(path.realpath(__file__)) + '/'

def pretty_list(dictionary):
    return ', '.join(dictionary.keys())

if __name__ == "__main__":
    import sys
    script_path = current_path()

    hosts = Hosts(backup_file_path='./hosts.bkp', script_path=script_path)
    sites = BlockedSites(hosts, filename='%ssites' % script_path)

    if not hosts.backup_ready():
        print('creating hosts.bkp')
        hosts.make_backup()

    command_map = {
        'restore': lambda: hosts.restore(),
        'list': lambda: sites.list(),
        'update': lambda: hosts.update(sites.sites.values()),
        'unblock': lambda short_name, time: sites.unblock(short_name, time)
    }

    try:
        command, *args = sys.argv[1:]
    # no args specified
    except ValueError as ve:
        try:
            command = sys.argv[1]
            args = None

        # no command specified
        except IndexError as err:
            print('Specify a command. One of:', pretty_list(command_map))

            sys.exit()

    try:
        command_map[command](*args)
    except KeyError as kerr:
        print('%s is not a valid command. Must be one of: %s' %
            (kerr, pretty_list(command_map)))
        sys.exit()

    except KeyboardInterrupt:
        command_map['update']()
        sys.exit()

    except Exception as ex:
        print(ex)
        sys.exit()
