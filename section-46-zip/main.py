from zipfile import ZipFile
from pathlib import Path

files_folder = Path('test_files')
# ========================================== Create 1000 files
# if not files_folder.exists():
#     files_folder.mkdir()
#
# for i in range(1000):
#     with open(files_folder.joinpath(f"{i}_some_file.txt"), 'w') as file:
#         for j in range(10):
#             file.write(f"file [{i}] - {j} -> This is some text for file\n")

# ========================================== Add files to zip archive
# with ZipFile('all-files.zip', mode='w') as zip_file:
#     print(zip_file)
#     for file in Path(files_folder).iterdir():
#         zip_file.write(file)

# ========================================== Extract files from zip archive
with ZipFile('all-files.zip') as zip_arch:
    # print(zip_arch.infolist()) # [<ZipInfo filename='test_files/0_some_file.txt' filemode='-rw-rw-rw-' file_size=440>,..]
    # print(zip_arch.filename)  # arch name all-files.zip
    zip_arch.extractall('unzipped')


