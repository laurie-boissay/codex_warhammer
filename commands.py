from tkinter import *


from data import *
from file_management import save_an_object, read_an_object


def get_var_name():
    for k in var_name.keys():
        list_owned_units[k] = var_name[k].get()
    save_an_object(list_owned_units, "owned_units")


def get_variable_name():
    for k in variable_name.keys():
        if variable_name[k].get() != 0:
            choosen_units_value.append(variable_name[k].get())

    for k, v in variable_name.items():
        if variable_name[k].get() != 0:
            choosen_units_name.append(k)


def get_new_variable_name():
    for k in variable_name.keys():
        if variable_name[k].get() != 0:
            choosen_units_value.append(variable_name[k].get())

    for k, v in variable_name.items():
        if variable_name[k].get() != 0:
            choosen_units_name.append(k)


def choice_owned_units():
    # k = var_name
    # v[0] = unit name
    # v[1] = "escouade complète"/"demie-escouade"
    # v[2] = value

    choice = {}

    try:
        list_owned_units = read_an_object("user/owned_units")
    except FileNotFoundError:
        list_owned_units = read_an_object("owned_units")
    
    for k, v in list_owned_units.items():
        for key, value in units.items():
            if v: # figurine is owned.
                if k == key : # not doubles.
                    var_name = key
                    
                    if value[1][0] != value[1][1]:
                        var_name_min = var_name + "_min"
                        choice[var_name_min] = (k, "demie-escouade", value[1][0])

                        var_name_max = var_name + "_max"
                        choice[var_name_max] = (k, "escouade complète", value[1][1])
                       
                    else:
                        choice[var_name] = (k, "escouade complète", value[1][1])

    for k, v in choice.items():
        choosen_units[k] = v
    return choice
 

def count_power():
    power = 0
    for value in choosen_units_value:
        power += value
    return power



   



