import os


class ChangeExtension:
    def are_extensions_changed(self, dir_path, original_extension, new_extension):
        os.chdir(dir_path)
        extensions_list = []

        for f in os.listdir():
            _, file_extension = os.path.splitext(f)
            if file_extension == new_extension:
                extensions_list.append(file_extension)

        return len(extensions_list) > 0 and all(x == extensions_list[0] for x in extensions_list)

    def change_name_extension(self, dir_path, original_extension, new_extension):

        os.chdir(dir_path)

        # TO_DO:
        # handle files with the same names

        for f in os.listdir():
            file_name, file_extension = os.path.splitext(f)
            if file_extension == original_extension:
                new_name = '{}{}'.format(file_name, new_extension)

                os.rename(f, new_name)

        change_successful = self.are_extensions_changed(
            dir_path, original_extension, new_extension)
        if change_successful:
            print('PATH: ' + dir_path + ' RESULT: Change successful')
        else:
            print('PATH: ' + dir_path +
                  ' RESULT: There were no files with given extension')
