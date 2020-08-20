###### RESSOURCES #################################################
#https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232431-utilisez-des-fichiers
#https://www.guru99.com/python-check-if-file-exists.html


import pickle
from os import path, mkdir, chdir, getcwd, listdir


from data import list_owned_units


def read_an_object(target_file):
    """
    This function open the target_file and return
    the oject inside.

    """
    with open(target_file, "rb") as backup_file:
        pick = pickle.Unpickler(backup_file)
        return pick.load()


def save_an_object(object, destination_file):
    """
    This function save the object in the destination_file.

    """
    try:
        chdir("user")
    except FileNotFoundError:
        check = listdir()
        if check == ['owned_units']:
            pass
        else:
            print("PATH ERROR : save_an_object")

    with open(destination_file, "wb") as backup_file:
        pick = pickle.Pickler(backup_file)
        pick.dump(object)


def create_user_folder():
    """
    If it doesn't exist, this function creates
    a folder "user".        

    """
    if not path.exists("user"):
        mkdir("user")

    if not path.exists("user/owned_units"):
        save_an_object(list_owned_units, "owned_units")