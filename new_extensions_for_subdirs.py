from iterate_over_directory import IterateOverDirs
from change_extension import ChangeExtension

root_dir = input('Path to root directory: ')
original_extension = input('Extension you want to change e.g. .txt: ')
new_extension = input('What extension instead e.g. .srt: ')

change_extension = ChangeExtension()
iterate_over_dirs = IterateOverDirs(root_dir)

for subdir in iterate_over_dirs.get_path_of_every_file():
    change_extension.change_name_extension(
        subdir,
        original_extension,
        new_extension)
