import os
from string import ascii_uppercase

# Task 1: List only directories, files, and all directories, files in a specified path.
def list_dir_files(path):
    all_files = os.listdir(path)
    dirs = [f for f in all_files if os.path.isdir(os.path.join(path, f))]
    files = [f for f in all_files if os.path.isfile(os.path.join(path, f))]
    return dirs, files, all_files

# Task 2: Check for access to a specified path.
def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

# Task 3: Test whether a given path exists or not.
def test_path(path):
    exists = os.path.exists(path)
    if exists:
        return os.path.basename(path), os.path.dirname(path)
    else:
        return None, None

# Task 4: Count the number of lines in a text file.
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

# Task 5: Write a list to a file.
def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        file.writelines(f"{item}\n" for item in lst)

# Task 6: Generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generate_text_files(directory):
    for char in ascii_uppercase:
        with open(os.path.join(directory, f"{char}.txt"), 'w') as file:
            file.write(f"This is file {char}.txt\n")

# Task 7: Copy the contents of a file to another file.
def copy_file(src_path, dest_path):
    with open(src_path, 'r') as src, open(dest_path, 'w') as dest:
        dest.writelines(src.readlines())

# Task 8: Delete file by specified path.
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
    else:
        print("File does not exist or is not writable")



print(list_dir_files('/path/to/directory'))
print(check_access('/path/to/path'))
print(test_path('/path/to/file.txt'))
print(count_lines('/path/to/file.txt'))
write_list_to_file('/path/to/file.txt', ['line1', 'line2', 'line3'])
generate_text_files('/path/to/directory')
copy_file('/path/to/source.txt', '/path/to/destination.txt')
delete_file('/path/to/file.txt')

