from .iterate_over_directory import IterateOverDirs
from .change_extension import ChangeExtension
from .user_inputs_for_scripts import UserInputs


def new_extensions_for_subdirs():
    user_inputs = UserInputs()

    root_dir = user_inputs.root_dir()
    original_extension = user_inputs.original_extension()
    new_extension = user_inputs.new_extension()

    change_extension = ChangeExtension()
    iterate_over_dirs = IterateOverDirs(root_dir)

    for subdir in iterate_over_dirs.get_path_of_every_file():
        change_extension.change_name_extension(
            subdir,
            original_extension,
            new_extension)


def change_extension():
    change_extension = ChangeExtension()
    user_inputs = UserInputs()

    root_dir = user_inputs.root_dir()
    original_extension = user_inputs.original_extension()
    new_extension = user_inputs.new_extension()

    change_extension.change_name_extension(
        root_dir, original_extension, new_extension)
