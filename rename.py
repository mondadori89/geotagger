import os

folder_path = 'organizer'

prefix = 'a'    # prefix that goes before the file name

files_list = os.listdir(folder_path)

for i in range(len(files_list)) :

    img_filename = files_list[i]

    old_file_name = f'{folder_path}/{img_filename}'

    new_name = prefix + img_filename

    # Uncomment this to treat detele special characters
    """ for letter in img_filename :
        if ' ' == letter or '(' == letter or ')' == letter:
            continue
        else:
            new_name = new_name + letter """

    new_file_name = f'{folder_path}/{new_name}'

    print(new_name)

    # Renaming the file
    os.rename(old_file_name, new_file_name)