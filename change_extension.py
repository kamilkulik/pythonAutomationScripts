import os


class ChangeExtension:
    def are_extensions_changed(self, dir_path, original_extension, new_extension):
        os.chdir(dir_path)
        extensions_list = []

        for f in os.listdir():
            file_name, file_extension = os.path.splitext(f)
            if file_extension == original_extension:
                extensions_list.append(file_extension)

        return all(x == extensions_list[0] for x in extensions_list)

    def change_name_extension(self):
        dir_path = input('Path to dir with files: ')
        original_extension = input('Extension you want to change e.g. .txt: ')
        new_extension = input('What extension instead e.g. .srt: ')

        os.chdir(dir_path)

        for f in os.listdir():
            file_name, file_extension = os.path.splitext(f)
            if file_extension == original_extension:
                new_name = '{}{}'.format(file_name, new_extension)

                os.rename(f, new_name)

        change_successful = self.are_extensions_changed(dir_path, original_extension, new_extension)
        if change_successful:
            print('Change successful')
        else:
            print('There was an error')
