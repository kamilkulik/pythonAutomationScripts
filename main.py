from change_extension import ChangeExtension

change_extension = ChangeExtension()


def main():
    dir_path = input('Path to dir with files: ')
    change_extension.change_name_extension(dir_path)


main()
