#a journal entry system

import os, shelve


def view_entry(array):
    '''Prints the names of all log entries'''
    print('Log entries:')
    for i in array.keys():
        print(i.rjust(len(i)+2, ' '))


def show_entry(key):
    '''Print the entry at a certain key in the log'''
    if key in entries.keys():
        print('\n' + '#' * (len(key) + 6))
        print(key.upper().center(len(key) +2, ' ').center(len(key) + 6, '#'))
        print('#' * (len(key) + 6))
        print(entries[key])
    else:
        print('That entry does not exist.  Would you like to create it? ', end=' ')
        decision = input('Y/N: ')
        if decision == 'n':
            return
        else:
            new_entry(key=key)


def new_entry(key=0):
    # Create a new journal entry
    if key == 0:
      print('What do you want to call your new log?', end= ' ')
      key = input()
    print(key.upper() + ':')
    contents = []
    while True:
        line = input()
        if line != '':
            contents.append(line)
        else:
            break
    value = '\n'.join(contents)
    entries[key] = value

def remove_entry(key):
    # Remove entry
    if key in entries.keys():
        print('Are you sure you want to remove', key + '?')
        decision = input('Y/N: ')
        if decision.lower() == 'y':
            del entries[key]
            print('Entry successfully removed.')
        else:
            return 0
    else:
        print('Entry does not exist.')

def edit_entry(key):
    # Append to the end of an existing entry
    if key in entries.keys():
        print('You may begin appending to log ...\n')
        value_init = entries[key]
        print(value_init)
        contents = []
        while True:
            line = input()
            if line != '':
                contents.append(line)
            else:
                break
        value = '\n'.join(contents)
        entries[key] = value_init + '\n' + value
    else:
        print('Entry does not exist.')

def get_key(choice):
    # Grab name of key from input
    if ' ' in choice:
        index = choice.index(' ')
        key = choice[index+1:]
        return key
    else:
        print('That is not a valid entry')
        return 0


if os.path.exists('logs.logs'):
    myShelf = shelve.open('logs.logs')
    entries = myShelf['logs']
    myShelf.close()
else:
    entries = dict()
 
while True:
    print('\nWhat do you want to do?  Enter Q to quit.', end=' ')
    choice = input().lower()
    if choice == 'q':
        myShelf = shelve.open('logs.logs')
        myShelf['logs'] = entries
        myShelf.close()
        break
    elif choice == 'view':
        view_entry(entries)
    elif choice.startswith('new'):
        new_entry()
    elif choice.startswith('show'):
        key = get_key(choice)
        if key!= 0:
            show_entry(key)
    elif choice.startswith('remove'):
        key = get_key(choice)
        if key!= 0:
            remove_entry(key)
    elif choice.startswith('edit'):
        key = get_key(choice)
        if key!= 0:
          edit_entry(key)