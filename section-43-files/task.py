from pathlib import Path

files_folder = Path('task_files')

# if not files_folder.exists():
#     files_folder.mkdir()

#OR!

files_folder.mkdir(exist_ok=True)

with open(files_folder.joinpath('first.txt'), 'w') as first:
    first.write("first one\n")
    first.write("first two\n")
    first.write("first three\n")

with open(files_folder.joinpath('second.txt'), 'w') as second:
    lines = ["second one", "second two", "second three"]
    for line in lines:
        second.write(line + "\n")

with open(files_folder.joinpath('first.txt')) as first:
    print(first.read())

with open(files_folder.joinpath('second.txt')) as second:
    # while True:
    #     next_line = second.readline()
    #     if not next_line:
    #         break
    #     print(next_line.strip())

    for line in lines:
        print(line.strip())

for file in Path(files_folder).iterdir():
    print(f"[{file}] removed")
    file.unlink()

print(f"folder [{files_folder}] was removed")
files_folder.rmdir()
