FIlEPATH = 'todos.txt'
def get_todos(file_path=FIlEPATH):
    """ Read a text file and return the list
    of to-do items.
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return [todo.strip('\n') for todo in todos_local]


def write_todos(todos_arg, file_path=FIlEPATH):
    """ Write the to-do items list in the text file. """
    with open(file_path, 'w') as file_local:
        file_local.writelines([todo+'\n' for todo in todos_arg])


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())