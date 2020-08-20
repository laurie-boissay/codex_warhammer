############ TEXT UNITS APTITUDES ####################################
anges_mort_text = "[voir Codex : Space Marines]"

halo_fer_text = "Cette figurine a une sauvegarde invulnérable de 4+."

oblitération_totale = "A votre phase de Tir, vous pouvez déclarer "
oblitération_totale += "que cette unité ne tirera que sur une cible unique."
oblitération_totale += "Dans ce cas, choisissez 1 unité cible pour cette unité "
oblitération_totale += "; les figurines de cette unité peuvent tirer deux fois "
oblitération_totale += "à cette phase, mais elles ne peuvent cibler que cette "
oblitération_totale += "unité ennemie."

rites_bataille_aura_text = "Relancez les jets de touche de 1 pour les attaques "
rites_bataille_aura_text += "des figurines des unités <Chapitre> amies tant que "
rites_bataille_aura_text += "leur unité est à 6\" de cette figurine."


############ TEXT WEAPONS APTITUDES ##################################
bouclier_relique_text = ""

epee_e_maitre_text = "-"

fusil_fuser_text = "Quand vous résolvez une attaque contre une unité "
fusil_fuser_text += "à mi-portée, jetez deux D6 lorsque vous infligez "
fusil_fuser_text += "ses dégats et défaussez un des résultats."

grenade_frag_text = "Déflagration"

grenade_krak_text = "-"

pistolet_bolter_text = "-"

pistolet_bolter_l_text = "-"


############ DICTIONARIES #####################################
units = {
    "ESCOUADE ERADICATOR" : [
        "Soutien", # Role.
        (5, 5), # (power_min, power_max),
        ["Imperium", "Adeptus Astartes", "<Chapitre>"], # Faction key words.
        ["Infanterie", "Mk X Gravis", "Primaris", "ESCOUADE ERADICATOR"], # key words.
        False, # Half-escouade.
        [ # Figurines.
            ["Eradicator", (2,2)], # "Name", (nbr_min, nbr_max),
            ["Sergent Eradicator", (1,1)], # "Name", (nbr_min, nbr_max),
        ], # End figurines.
        ["Pistolet bolter", "Fusil fuser"], # Equipment.
        ["Anges de la mort", "Oblitération Totale"], # Aptitudes.
    ], # End escouade ESCOUADE ERADICATOR ****************************************

    "CAPITAINE PRIMARIS" : [
        "QG", # Role.
        (5, 5), # (power_min, power_max),
        ["Imperium", "Adeptus Astartes", "<Chapitre>"], # Faction key words.
        ["Infanterie", "Personnage", "Primaris", "Capitaine"], # key words.
        False, # Half-escouade.
        [ # Figurines.
            ["Capitaine Primaris", (1,1)], # "Name", (nbr_min, nbr_max),
        ], # End figurines.
        ["Pistolet bolter lourd", "Epée énergétique de maître", "Grenade Frag", "Grenade Krak", "Bouclier relique",], # Equipment.
        ["Anges de la mort", "Rites de Bataille [Aura]", "Halo de Fer",], # Aptitudes.
    ], # End escouade CAPITAINE PRIMARIS ****************************************

    "PRIMARIS" : [
        "Soutien", # Role.
        (2, 5), # (power_min, power_max),
        ["Imperium", "Adeptus Astartes", "<Chapitre>"], # Faction key words.
        ["Infanterie", "Mk X Gravis", "Primaris", "ESCOUADE ERADICATOR"], # key words.
        False, # Half-escouade.
        [ # Figurines.
            ["Eradicator", (2,2)], # "Name", (nbr_min, nbr_max),
            ["Sergent Eradicator", (1,1)], # "Name", (nbr_min, nbr_max),
        ], # End figurines.
        ["Pistolet bolter", "Fusil fuser"], # Equipment.
        ["Anges de la mort", "Oblitération Totale"], # Aptitudes.
    ], # End escouade CAPITAINE PRIMARIS ****************************************

    "CAPITAINE" : [
        "Soutien", # Role.
        (3, 5), # (power_min, power_max),
        ["Imperium", "Adeptus Astartes", "<Chapitre>"], # Faction key words.
        ["Infanterie", "Mk X Gravis", "Primaris", "ESCOUADE ERADICATOR"], # key words.
        False, # Half-escouade.
        [ # Figurines.
            ["Eradicator", (2,2)], # "Name", (nbr_min, nbr_max),
            ["Sergent Eradicator", (1,1)], # "Name", (nbr_min, nbr_max),
        ], # End figurines.
        ["Pistolet bolter", "Fusil fuser"], # Equipment.
        ["Anges de la mort", "Oblitération Totale"], # Aptitudes.
    ], # End escouade CAPITAINE PRIMARIS ****************************************

    "CP" : [
        "Soutien", # Role.
        (3, 6), # (power_min, power_max),
        ["Imperium", "Adeptus Astartes", "<Chapitre>"], # Faction key words.
        ["Infanterie", "Mk X Gravis", "Primaris", "ESCOUADE ERADICATOR"], # key words.
        False, # Half-escouade.
        [ # Figurines.
            ["Eradicator", (2,2)], # "Name", (nbr_min, nbr_max),
            ["Sergent Eradicator", (1,1)], # "Name", (nbr_min, nbr_max),
        ], # End figurines.
        ["Pistolet bolter", "Fusil fuser"], # Equipment.
        ["Anges de la mort", "Oblitération Totale"], # Aptitudes.
    ], # End escouade CAPITAINE PRIMARIS ****************************************

} # End units # # # # # # # # # # # # # # # # # # # # # # # # # # #


figurines = {
    # "Name" : ['M"', "CC", "CT", "F", "E", "PV", "A", "Cd", "Sv"],
    "Capitaine Primaris" : ['6"', "2+", "2+", "4", "4", "6", "5", "9", "3+"],

    "Eradicator" : ['5"', "3+", "3+", "4", "5", "3", "2", "7", "3+"],

    "Sergent Eradicator" : ['5"', "3+", "3+", "4", "5", "3", "3", "8", "3+"],
    
}# End figurines # # # # # # # # # # # # # # # # # # # # # # # # # # #


equipment = {
    # "Name" : Is a weapon,
    "Bouclier relique" : False,

    "Epée énergétique de maître" : True,

    "Fusil fuser" : True,

    "Grenade Frag" : True,
    "Grenade Krak" : True,

    "Pistolet bolter" : True,
    "Pistolet bolter lourd" : True,   
}# End equipement # # # # # # # # # # # # # # # # # # # # # # # # #


units_aptitudes = {
    # "Name" : Text,
    "Anges de la mort" : anges_mort_text,

    "Halo de Fer" : halo_fer_text,

    "Oblitération Totale" : oblitération_totale,

    "Rites de Bataille [Aura]" : rites_bataille_aura_text,
}# End units_aptitudes # # # # # # # # # # # # # # # # # # # # # #


equipment_aptitudes = {
    # "Name" : Text,
    "Bouclier relique" : bouclier_relique_text,

    "Epée énergétique de maître" : epee_e_maitre_text,

    "Fusil fuser" : fusil_fuser_text,

    "Grenade Frag" : grenade_frag_text,
    "Grenade Krak" : grenade_krak_text,

    "Pistolet bolter" : pistolet_bolter_text,
    "Pistolet bolter lourd" : pistolet_bolter_l_text,
}# End equipment_aptitudes # # # # # # # # # # # # # # # # # # # #


weapon_characteristics = {
    # "Name" : ['range"', "type", "F", "PA", "D"],
    "Epée énergétique de maître" : ["Mélée", "Mélée", "+1", "-3", "2"],

    "Fusil fuser" : ['24"', "Assaut 1", "8", "-4", "D6"],

    "Grenade Frag" : ['6"', "Grenade D6", "3", "0", "1"],
    "Grenade Krak" : ['6"', "Grenade 1", "6", "-1", "D3"],

    "Pistolet bolter" : ['12"', "Pistolet 1", "4", "0", "1"],
    "Pistolet bolter lourd" : ['18"', "Pistolet 1", "4", "-1", "1"],
}# End weapon_characteristics # # # # # # # # # # # # # # # # # # #


owned_var_name = {}

add_var_name = {}

del_var_name = {}


list_owned_units = {}

choosen_units = {}


choosen_units_value = []

choosen_units_name = []



