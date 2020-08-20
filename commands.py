from tkinter import *


from data import *
from file_management import save_an_object, read_an_object


def get_var_name():
    for k in var_name.keys():
        list_owned_units[k] = var_name[k].get()
    save_an_object(list_owned_units, "owned_units")


def get_variable_name():
    for k in variable_name.keys():
        list_choosen_units[k] = variable_name[k].get()

    


   



