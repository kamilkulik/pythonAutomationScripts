from tools import new_extensions_for_subdirs, change_extension


def main():
    script = input(
        'TYPE\nA to change file extensions in single directory, \nB to change extensions in directory and all its subdirectories.\nSELECTION: '
    )
    if(script == 'A'):
        change_extension()
    elif(script == 'B'):
        new_extensions_for_subdirs()


main()
