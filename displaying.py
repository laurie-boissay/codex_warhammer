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
            text="Vos unités : ",
            fg="red",
            bg=self.title_color,
            )
        self.label.pack(padx=10, pady=10)

        
    def button_check_choosen(self):
        try:
            list_owned_units = read_an_object("user/owned_units")
        except FileNotFoundError:
            list_owned_units = read_an_object("owned_units")
        
        for k, v in list_owned_units.items():
            text  = ""
            for key, value in units.items():
                if v:
                    if k == key :
                        variable_name[k] = tk.IntVar()
                        text += k + " : "
                        text += value[0]

                        if value[1][0] != value[1][1]:
                            text += " ; de "
                            text += str(value[1][0]) + " à "
                            text += str(value[1][1]) + " rangs."
                            self.checkbutton_choose_unit(text, key)
                        else:
                            text += " ; " + str(value[1][0]) + " rangs."
                            self.checkbutton_choose_unit(text, key)

        self.button_validate_choice()

                        
    def checkbutton_choose_unit(self, text, key):
        self.bouton_2 = tk.Checkbutton(
            self.frame3,
            text=text,
            bg=self.title_color,
            variable=variable_name[key],
            )
        self.bouton_2.pack()


    def button_validate_choice(self):
        self.button_validate = tk.Button(
            self.frame3,
            text="Valider",
            command=self.display_total_value,
            )
        self.button_validate.pack()


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

        self.display_label_frame_choosen()


    def display_label_frame_choosen(self):
        self.label = tk.Label(
            self.frame4,
            text="Puissance totale : ",
            fg="red",
            bg=self.title_color,
            )
        self.label.pack(padx=10, pady=10, side="top")


    def display_total_value(self):
        get_variable_name()
        self.display_frame_choosen()
        power = 0
        for k, v in list_choosen_units.items():
            for key, value in units.items():
                if v and k == key:
                    power += value[1][1]
        
        self.label = tk.Label(
            self.frame4,
            text=str(power),
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