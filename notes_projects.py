import os


def remove_note(note_num: int):
    new_file = open("data.txt", "r")
    lines = new_file.readlines()
    new_file.close()
    file_path = 'data.txt'
    for line in lines:
        line = line.split('|')
        wanted_index_remove = note_num - 1
        for index in range(len(line)):
            if index == wanted_index_remove:
                print(f"You deleted {line[index]}")
                line.pop(index)
                new_file = open("data.txt", "w")
                line = [str(x) for x in line]
                new_list_to_save = '|'.join(line)
                new_file.write(new_list_to_save)
                break


def add_note(file_name: str, note: str, title: str):
    file_path = 'data.txt'
    new_file = open("data.txt", "a")
    if os.stat(file_path).st_size == 0:
        new_file.write(f'{title}-' + note)
    else:
        new_file.write('|' + f'{title}-' + note)
    new_file.close()


def view_notes():
    new_file = open("data.txt", "r")
    lines = new_file.readlines()
    file_path = "data.txt"
    if os.stat(file_path).st_size == 0:
        print("You don't have any notes.")
    else:
        for line in lines:
            line = line.split('|')
            print('This is all of your notes:')
            counter = 1
            for element in line:
                element = element.split('-')
                print(f'{counter}. ' + element[0])
                counter += 1


def see_specific_note(given_note: str):
    if given_note.lower() == 'n':
        pass
    else:
        given_note = int(given_note)
        new_file = open("data.txt", "r")
        lines = new_file.readlines()
        file_path = "data.txt"
        for line in lines:
            line = line.split('|')
            element = line[given_note - 1].split('-')
            print(f'Your note: {element[1]}')


def search_notes(note: str):
    any_notes = False
    store_found_notes = []
    new_file = open("data.txt", "r")
    lines = new_file.readlines()
    for line in lines:
        line = line.split('|')
        for element in line:
            if note in element.lower():
                store_found_notes.append(element)
                any_notes = True
            else:
                if any_notes:
                    pass
                else:
                    any_notes = False
        if any_notes:
            print("All notes that you are looking for:")
            for found_note in store_found_notes:
                print(found_note)
        else:
            print("It look's like you don't have similar notes.")
    new_file.close()


print('----->  Note Project  <-----')
print()
print('1. Remove note from storage.')
print('2. Add note to storage.')
print('3. View all notes in storage.')
print('4. Search for note in storage.')
# print('5. Edit note.')
print('5. If you want to quit.')
print()
print('-----------------------------')
user_input = input('What do you want to do? ')

while True:
    # remove
    if '1' in user_input:
        file_path_name = "data.txt"
        if os.stat(file_path_name).st_size == 0:
            print("You don't have any notes.")
        else:
            view_notes()
            value = int(input("Choose which note to delete: "))
            remove_note(value)
    # Add
    elif '2' in user_input:
        title_name = input("Choose a title for your note: ")
        value = input("Write what you want to add: ")
        add_note("data.txt", value, title_name)
    # View
    elif '3' in user_input:
        view_notes()
        file_path_name = "data.txt"
        if os.stat(file_path_name).st_size == 0:
            pass
        else:
            specific_note = input('Do you want to see a note in detail?("n" for no) ')
            see_specific_note(specific_note)
    # Search
    elif '4' in user_input:
        file_path_name = "data.txt"
        if os.stat(file_path_name).st_size == 0:
            print("You don't have any notes.")
        else:
            value = input("Write what you want to search for: ")
            while len(value) < 2:
                print('You should write at least two letters.')
                value = input("Write what you want to search for: ")
            search_notes(value)
    # Quit
    elif '5' in user_input:
        break
    print('-----------------------------')
    user_input = input('What do you want to do? ')
print("Thanks for using our app.")
