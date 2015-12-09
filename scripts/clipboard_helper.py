#!/usr/bin/python3.4
import shelve, pyperclip

def get_shelf(name='mcb'):
    return shelve.open('mcb')

def get(key):
    with get_shelf() as shelf:
        try:
            pyperclip.copy(shelf[key])
        except KeyError:
            print('no such key')

def save(key):
    with get_shelf() as shelf:
        shelf[key] = pyperclip.paste()

def delete(key):
    with get_shelf() as shelf:
        try:
            del shelf[key]
        except KeyError: pass

def list_all():
    with get_shelf() as shelf:
        print(('\n').join(shelf.keys()))


if __name__ == "__main__":
    import sys

    try:
        command, key = sys.argv[1:]
    except ValueError:
        command = sys.argv[1]
        key = None
        if command not in ['list', 'all']:
            print('wrong number of args')
            sys.exit()


    command_map = {
        'save':     lambda: save(key),
        'delete':   lambda: delete(key),
        'del':      lambda: delete(key),
        'get':      lambda: get(key),
        'list':     lambda: list_all(),
        'all':      lambda: list_all()
    }

    command_map[command]()
