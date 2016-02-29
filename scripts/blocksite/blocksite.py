#!/usr/bin/python3
from modules.hosts import Hosts
from modules.blocked_sites import BlockedSites
from os import path


def current_path():
    return path.dirname(path.realpath(__file__))

if __name__ == "__main__":
    import sys
    script_path = current_path()

    hosts = Hosts(backup_file_path='%s/hosts.bkp' % script_path, bare_hosts_path='%s/hosts.base' % script_path)
    sites = BlockedSites(hosts, filename='%s/sites' % script_path)

    command_map = {
        'restore': lambda: hosts.restore(),
        'backup': lambda: hosts.make_backup(),
        'list': lambda: sites.list(),
        'add': lambda: sites.add(args),
        'remove': lambda: sites.remove(args),
        'update': lambda: hosts.update(sites.sites.values()),
        'unblock': lambda: sites.unblock(args[0], args[1])
    }

    try:
        command, args = sys.argv[1], sys.argv[2:]

    # no args specified
    except ValueError as ve:
        try:
            command = sys.argv[1]
            args = None

        # no command specified
        except IndexError as err:
            command_list = ', '.join(command_map.keys())
            print('Specify a command. One of:', command_list)

            sys.exit()

    try:
        command_map[command]()
    except Exception as ex:
        print(ex)
