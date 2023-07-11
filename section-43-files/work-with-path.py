from pathlib import Path  # OOP style

# --------------------------------------------------------- cwd, home, joinpath, /, absolute
cwd = Path('.')
print("cwd => ", cwd)
print("type(cwd) => ", type(cwd))  # <class 'pathlib.WindowsPath'>
print("Path.__subclasses__()", Path.__subclasses__())  # [<class 'pathlib.PosixPath'>, <class 'pathlib.WindowsPath'>]

# --------------------------- Create hath
print("cwd.absolute() => ", cwd.absolute())  # cwd.absolute() =>  D:\Python\python-by-bogdan-stashchuk\section-43-files
current = Path('D:/').joinpath('Python').joinpath('python-by-bogdan-stashchuk').joinpath('section-43-files')
# current = Path('D:/') / 'Python' / 'python-by-bogdan-stashchuk' / 'section-43-files'
print('current => ', current)

file_path = Path('test.txt')
print("Path.cwd() => ", Path.cwd())  # D:\Python\python-by-bogdan-stashchuk\section-43-files
print("Path.home() => ", Path.home())  # C:\Users\Max

# D:\Python\python-by-bogdan-stashchuk\section-43-files\inner_folder\folder
print(Path.cwd().joinpath('inner_folder').joinpath('folder'))
print(Path.cwd() / 'inner_folder' / 'folder')
print(Path('C:/') / 'inner_folder' / 'folder')

# --------------------------------------------------------- exists
print(Path('main.py').exists())  # True
print(Path('C:/Users/Max').exists())  # True

# --------------------------------------------------------- is_file, is_dir
print(Path('main.py').is_file())  # True
print(Path('C:/Users/Max').is_dir())  # True

# --------------------------------------------------------- iterdir
print("Path('../').iterdir() => ", len(list(Path('../').iterdir())))
for file_dir in Path('../').iterdir():
    continue  # comment it if you want to see all dirs
    print(file_dir)

# --------------------------------------------------------- mkdir, rmdir
# folder_django = Path('.').joinpath('django')  # 1. Where to create
folder_django = Path('.') / 'django'  # 1. Where to create
if not folder_django.exists():
    folder_django.mkdir()  # 2. Create
else:
    print(f"file/folder [{folder_django}] already exists")
# if file Exists -> FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'django'

if folder_django.exists():
    folder_django.rmdir()  # OSError: [WinError 145] The directory is not empty: 'django'


# filtered = filter(lambda attr: not attr.startswith('_'), dir(file_path))
# print(list(filtered))
# ['absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive',
# 'exists', 'expanduser', 'glob', 'group', 'hardlink_to', 'home',
# 'is_absolute', 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_file',
# 'is_mount', 'is_relative_to', 'is_reserved', 'is_socket', 'is_symlink',
# 'iterdir', 'joinpath', 'lchmod', 'link_to', 'lstat', 'match', 'mkdir',
# 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes', 'read_text',
# 'readlink', 'relative_to', 'rename', 'replace', 'resolve', 'rglob', 'rmdir', 'root',
# 'samefile', 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink',
# 'with_name', 'with_stem', 'with_suffix', 'write_bytes', 'write_text']
