import os

files = os.listdir()
name = "your_name"
gutignore = ['__init__.py', '.venv', '.idea']

def delete_already_named(index = 0):    
    if name in files[index]:
        files.pop(index)
    else:
        index += 1

    if index >= len(files):
        return
    
    delete_already_named(index)

def delete_self():
    py_name = __file__.split('/')
    py_name = py_name[len(py_name) - 1]
    files.remove(py_name)

def handle_gutignore():
    for ignore in gutignore:
        for file in files:
            if file == ignore:
                files.remove(file)

def rename_files():
    for file in files:
            filename = file.split(".py")[0]
            filename += f"-{name}.py"
            os.rename(file, filename)

#
# Prechecks
#
delete_already_named()
delete_self()
handle_gutignore()

#
# Rename
#
rename_files()

print(files)


