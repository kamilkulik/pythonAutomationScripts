import os

def are_ext_changed(dir_path, orig_ext, new_ext):
  os.chdir(dir_path)
  ext_list = []

  for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == orig_ext:
      ext_list.append(file_ext)

  return all(x == ext_list[0] for x in ext_list)

def change_name_ext():

  dir_path = input('Path to directory with files: ')
  orig_ext = input('Extension you want to change e.g. .txt: ')
  new_ext = input('What extension instead e.g. .srt: ')

  os.chdir(dir_path)

  for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == orig_ext:
      new_name = '{}{}'.format(file_name, new_ext)

      os.rename(f, new_name)

  change_successful = are_ext_changed(dir_path, orig_ext, new_ext)
  if change_successful:
    print('Change successful')
  else:
    print('There was an error')

change_name_ext()