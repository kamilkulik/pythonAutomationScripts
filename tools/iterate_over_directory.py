import os


class IterateOverDirs:

    def __init__(self, root_dir):
        self.root_dir = root_dir

    def get_path_of_every_file(self):
        sub_dirs_list = []
        for subdirs, dirs, files in os.walk(self.root_dir):
            for file in files:
                sub_dirs_list.append(subdirs)
        sub_dirs = list(dict.fromkeys(sub_dirs_list))
        return sub_dirs
