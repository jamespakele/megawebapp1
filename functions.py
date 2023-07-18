FIlEPATH = 'todos.txt'


def get_todos(file_path=FIlEPATH):
    """ Read a text file and return the list
    of to-do items.
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    for index, todo in enumerate(todos_local):
        todos_local[index] = todo.strip('\n')
    return todos_local


def write_todos(todos_arg, file_path=FIlEPATH):
    """ Add line breaks """
    for index,todo in enumerate(todos_arg):
        todos_arg[index] = todo+'\n'

    """ Write the to-do items list in the text file. """
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())