#!/usr/bin/python3.4
import shelve, pyperclip

def get_shelf(name='mcb'):
    return shelve.open('mcb')

def get(key):
    with get_shelf() as shelf:
        try:
            pyperclip.copy(shelf[key])

        except KeyError:
            raise Exception('no such key:', key)

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
        if len(shelf.keys()): print(('\n').join(shelf.keys()))

def delete_all():
    with get_shelf() as shelf:
        shelf.clear()

if __name__ == "__main__":
    import sys

    command_map = {
        'save':     lambda: save(key),
        'delete':   lambda: delete(key),
        'del':      lambda: delete(key),
        'get':      lambda: get(key),
        'list':     lambda: list_all(),
        'all':      lambda: list_all(),
        'clean':    lambda: delete_all()
    }

    try:
        command, key = sys.argv[1:]

    except ValueError:
        try:
            command = sys.argv[1]
            key = None

            if command not in ['list', 'all', 'clean']:
                raise Exception('wrong numer of args for the command')

        except IndexError as err:
            command_list = (', ').join(command_map.keys())
            print('Specify a command. One of:', command_list)
            sys.exit()

        except Exception as ex:
            print(ex)
            sys.exit()


    try:
        command_map[command]()
    except Exception as ex:
        print(ex)

