import tkinter as tk
from os import path,chdir, listdir


from data import *
from commands import *
from file_management import *


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.background_color = "#0C090A"   #grey
        self.title_color = "#FFEBCD"        #parchment
        self.letter_color = "cyan"     
        self.other_color = "#00FF00"        #green
        self.board_color ="#6F4E37"         #brown

        self.master = master
        self.pack()

    ######## MAIN FRAME #####################################################################
    def display_main_frame(self):
        # frame 1
        self.frame1 = tk.Frame(
            self.master,
            bg=self.title_color,
            borderwidth=2,
            relief="flat",
            )
        self.frame1.pack(side="top", padx=30, pady=30)

        self.main_frame_label()

    
    def main_frame_label(self):
        self.label = tk.Label(
            self.frame1,
            text="Liste d'armée Blood Angels :",
            fg="red",
            bg="black",
            )
        self.label.pack(padx=10, pady=10, side="top")


    ######## FRAME EXISTING #####################################################################
    def display_frame_existing(self):
        self.frame2 = tk.Frame(
            self.frame1,
            bg=self.title_color,
            borderwidth=2,
            relief="flat",
            )
        self.frame2.pack(side="left", padx=10, pady=10)

        self.label = tk.Label(
            self.frame2,
            text="Quelles unités possédez-vous ?",
            fg="red",
            bg=self.title_color,
            )
        self.label.pack(padx=10, pady=10)

        self.button_check_owned()
        
    
    def button_check_owned(self):
        for k in units.keys():
            var_name[k] = tk.IntVar()
            self.bouton = tk.Checkbutton(
                self.frame2,
                text=k,
                bg=self.title_color,
                variable=var_name[k],
                )
            self.bouton.pack()

        self.button_save_owned()
        self.button_display_owned()


    def button_save_owned(self):
        self.button_save_owned = tk.Button(
            self.frame2,
            text="Sauver",
            command=get_var_name,
            )
        self.button_save_owned.pack(side="left")


    def button_display_owned(self):
        self.button_display_owned = tk.Button(
            self.frame2,
            text="Afficher",
            command=self.display_frame_owned,
            )
        self.button_display_owned.pack(side="right")


    ######## FRAME OWNED #####################################################################
    def display_frame_owned(self):
        try :
            self.frame3.pack_forget()
        except AttributeError:
            pass

        self.frame3 = tk.Frame(
            self.frame1,
            bg=self.title_color,
            borderwidth=2,
            relief="flat"
            )
        self.frame3.pack(side="left", padx=30, pady=30)

        self.frame_owned_label()
        self.button_check_choosen()
        


    def frame_owned_label(self):
        self.label = tk.Label(
            self.frame3,
            text="Choisissez vos unités : ",
            fg="red",
            bg=self.title_color,
            )
        self.label.pack(padx=10, pady=10)

        
    def button_check_choosen(self):
        choice = choice_owned_units()
        # k = var_name
        # v[0] = unit name
        # v[1] = "escouade complète"/"demie-escouade"
        # v[2] = value
        
        for k, v in choice.items():
            label_text = v[0]
            Checkbutton_text = v[1] + " : " + str(v[2])

            variable_name[k] = tk.IntVar()
            self.choose_unit_label(label_text)
            self.checkbutton_choose_unit(Checkbutton_text, k, v[2])

        self.button_add_choice()


    def choose_unit_label(self, text):
        self.label = tk.Label(
            self.frame3,
            text=text,
            fg="black",
            bg=self.title_color,
            )
        self.label.pack(padx=10, pady=10, side="top")

                        
    def checkbutton_choose_unit(self, text, key, value):
        self.bouton_choose = tk.Checkbutton(
            self.frame3,
            text=text,
            bg=self.title_color,
            variable=variable_name[key],
            onvalue=value,
            )
        self.bouton_choose.pack()


    def button_add_choice(self):
        self.button_add = tk.Button(
            self.frame3,
            text="Ajouter",
            command=self.display_total_value,
            )
        self.button_add.pack()


    ######## FRAME CHOSEEN #####################################################################
    def display_frame_choosen(self):
        try :
            self.frame4.pack_forget()
        except AttributeError:
            pass

        self.frame4 = tk.Frame(
            self.frame1,
            bg=self.title_color,
            borderwidth=2,
            relief="flat"
            )
        self.frame4.pack(side="right", padx=30, pady=30)

        self.display_label_frame_choosen("Puissance totale : ")


    def display_label_frame_choosen(self, text):
        self.label = tk.Label(
            self.frame4,
            text=text,
            fg="red",
            bg=self.title_color,
            )
        self.label.pack(padx=10, pady=10, side="top")


    def display_total_value(self):
        # Work in progress.
        self.display_frame_choosen()
        get_variable_name()

        power = 0
        for value in choosen_units_value:
            power += value
        self.total_power(str(power))
        
        self.display_label_frame_choosen("Unités selectionnées : ")
        for name in choosen_units_name:
                self.total_power(name)
                
    
    def total_power(self, text):
        self.label = tk.Label(
            self.frame4,
            text=text,
            fg="black",
            bg=self.title_color,
            )
        self.label.pack(padx=10, pady=10, side="top")


    ######## LAST FRAME #####################################################################
    def display_last_frame(self):
        self.last_frame = tk.Frame(
            self.master,
            bg=self.title_color,
            borderwidth=2,
            relief="flat",
            )
        self.last_frame.pack(side="bottom", padx=10, pady=10)

        self.quit_button()
        self.file_button()


    def quit_button(self):
        self.quit_bouton = tk.Button(
            self.last_frame,
            text="Quitter",
            command=self.master.quit,
            )
        self.quit_bouton.pack(side="right")


    def file_button(self):
        self.quit_bouton = tk.Button(
            self.last_frame,
            text="Imprimer",
            command=self.make_a_file,
            )
        self.quit_bouton.pack(side="left")


    def make_a_file(self):
        print("A parametrer.")