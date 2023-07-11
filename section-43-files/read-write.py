from pathlib import Path

test_file = Path('test.txt')

# ============================================================= Create file -> open(test_file, 'x')

if not test_file.exists():
    with open(test_file, 'x'):
        print(f"[{test_file}] created")
else:
    print(f"[{test_file}] already exists")

# ============================================================= Write to file -> open(test_file, ['a', 'w'])

# ======================================= Add new line to file

with open(test_file, "a") as add_to_file:
    add_to_file.write("001 Added new line to file\n")
    add_to_file.write("002 Added new line to file\n")
    add_to_file.write("003 Added new line to file\n")

with open(test_file) as read_from_file:
    print(read_from_file.read())  # <class 'str'>

# ======================================= Rewrite file
with open('test.txt', "w") as rewrite_file:
    rewrite_file.write("001 Rewritten Added new line to file\n")
    rewrite_file.write("002 Rewritten Added new line to file\n")
    rewrite_file.write("003 Rewritten Added new line to file\n")

with open('test.txt') as read_file:
    print(read_file.read())  # <class 'str'>

# ============================================================= Read file -> .read(), .readline(), .readlines()
print("test_file.read() => ")
with open('test.txt') as test_file_read:
    print(test_file_read.read())  # <class 'str'>
print("========================\n")

print("test_file.readline() => ")  # return first line
with open('test.txt') as test_file_readline:
    # print(test_file_readline.readline())  # <class 'str'>
    # readline(5) read first 5 symbols from line

    # next_line = test_file_readline.readline()
    # while next_line:
    #     print(next_line)
    #     next_line = test_file_readline.readline()

    while True:
        next_line = test_file_readline.readline()
        if not next_line:
            break
        print(next_line)

print("========================\n")

print("test_file.readlines() => ")  # return list of lines
with open('test.txt') as test_file_readlines:
    print(test_file_readlines.readlines())  # <class 'list'>
    # readlines(2) read first 2 lines from file
print("========================\n")

# ============================================================= Remove file -> unlink
if test_file.exists():
    test_file.unlink()

print(test_file.exists())
