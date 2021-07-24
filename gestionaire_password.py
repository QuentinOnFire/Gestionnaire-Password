from tkinter import *
from hashlib import sha256
import os

"""

Bonjour, ceci est un gestionnaire de mot de passe, il a été créé par Quentin Borras
Tous droit reservée
Quentin Borras Copyright ©
Les clés de decryptage sont a la ligne 52 et la ligne 53, pour les changez, il suffit de changez les caracteres de ces lignes.

"""


class App(Tk):

    def __init__(self):
        super().__init__()
        self.password_good = False
        self.label_key = Label(self, text="Entrer la clé", font=("Courrier", 20), bg='pink')
        self.label_key.pack()
        self.entry_key = Entry(self, font=("Courrier", 20), bg='pink')
        self.entry_key.pack()
        self.button_key = Button(self, text="Valider", font=("Courrier", 20), bg='pink',
                                 command=self.valide_key)
        self.button_key.pack()
        self.button_quit = Button(self, text="Fermer", font=("Courrier", 20), bg='pink',
                                  command=self.crypt_or_and_close)
        self.button_quit.place(x=770, y=530)
        self.label_invalid_key = Label(self, text="", font=("Courrier", 20), bg='pink')
        self.label_invalid_key.pack()
        self.menu_bar = Menu(self)
        self.menu_fichier = Menu(self)
        self.config(menu=self.menu_bar)
        self.menu_bar.add_cascade(label="Fichier", menu=self.menu_fichier)
        self.menu_fichier.add_command(label="Add password", command=self.add_password_app)
        self.menu_fichier.add_command(label="Shearch", command=self.shearch)
        self.menu_fichier.add_command(label="Delete shearch button/label", command=self.suppr_shearch)
        self.label_attention = Label(self, text="! Attention, bien cliquer sur fermer, pas sur la croix ni alt + f4 !",
                                     font=("Courrier", 20), bg='pink')
        self.label_attention.place(x=15, y=540)
        self.delete = True
        self.a = 20
        self.b = 0
        self.x = 40
        self.r = 0
        self.create = False
        self.dico_button_plus_moins = {}
        self.plus_moins = True
        self.g = 20
        self.h = True
        self.cle_1 = "A12b3C"
        self.cle_2 = "9*7#/@"

    def crypt_or_decrypt(self, entree, sortie, key):
        keys = sha256(key.encode('utf-8')).digest()
        with open(entree, 'rb') as f_entree:
            with open(sortie, 'wb') as f_sortie:
                i = 0
                while f_entree.peek():
                    c = ord(f_entree.read(1))
                    j = i % len(keys)
                    b = bytes([c ^ keys[j]])
                    f_sortie.write(b)
                    i = i + 1

    def shearch_affiche(self):
        name_nbr = int(self.entry_shearch.get()) - 1
        f_name = open('decrypt_name.txt', 'r')
        f_login = open('decrypt_login.txt', 'r')
        f_password = open('decrypt_password.txt', 'r')
        txt_name = f_name.readlines()[int(name_nbr)]
        txt_login = f_login.readlines()[int(name_nbr)]
        txt_password = f_password.readlines()[int(name_nbr)]
        self.label_shearch_app = Label(self, text=txt_name, font=("Courrier", 20), bg='pink')
        self.label_shearch_app.place(x=400, y=100)
        self.entry_shearch_login = Entry(self, font=("Courrier", 20), bg='pink', width=30)
        self.entry_shearch_login.place(x=260, y=140)
        self.entry_shearch_password = Entry(self, font=("Courrier", 20), bg='pink', width=30)
        self.entry_shearch_password.place(x=260, y=175)
        self.entry_shearch_login.insert(0, txt_login)
        self.entry_shearch_password.insert(0, txt_password)
        self.button_shearch_suppr = Button(self, text="Finish", font=("Courrier", 20), bg='pink',
                                           command=self.suppr_affich, width=28)
        self.button_shearch_suppr.place(x=260, y=210)
        print("Jeu : {} \nLogin : {} \nPassword : {} \n".format(txt_name, txt_login, txt_password))
        f_name.close()
        f_login.close()
        f_password.close()
        self.suppr_shearch()

    def suppr_affich(self):
        self.label_shearch_app.destroy()
        self.entry_shearch_password.destroy()
        self.entry_shearch_login.destroy()
        self.button_shearch_suppr.destroy()

    def suppr_password(self):
        nbr = int(self.entry_shearch.get()) - 1
        f_name = open('decrypt_name.txt', 'r')
        f_login = open('decrypt_login.txt', 'r')
        f_password = open('decrypt_password.txt', 'r')
        f_name_line = f_name.readlines()
        f_login_line = f_login.readlines()
        f_password_line = f_password.readlines()
        print(len(f_name_line))
        print(len(f_login_line))
        print(len(f_password_line))
        print("nbr = {}".format(nbr))
        f_password.close()
        f_name.close()
        name = 0
        login = 0
        password = 0
        f_name_reset = open('decrypt_name.txt', 'w')
        f_name_reset.close()
        for line in f_name_line:
            if line != f_name_line[nbr]:
                f_name_write = open('decrypt_name.txt', 'a')
                f_name_write.write(line)
                f_name_write.close()
                name += 1
            else:
                name += 1
        f_login_reset = open('decrypt_login.txt', 'w')
        f_login_reset.close()
        for line in f_login_line:
            if line != f_login_line[nbr]:
                f_login_write = open('decrypt_login.txt', 'a')
                f_login_write.write(line)
                f_login_write.close()
                login += 1
            else:
                login += 1
        f_password_reset = open('decrypt_login.txt', 'w')
        f_password_reset.close()
        for line in f_password_line:
            if line != f_password_line[nbr]:
                f_password_write = open('decrypt_password.txt', 'a')
                f_password_write.write(line)
                f_password_write.close()
                password += 1
            else:
                password += 1
        self.suppr_shearch()

    def shearch(self):
        if self.password_good and self.delete:
            with open("decrypt_name.txt", "r") as f:
                txt = f.readlines()
                nbr_lines = len(txt)
                self.nbr_of_login_app_password = nbr_lines
                f.close()
                self.r = 0
                if self.plus_moins and self.nbr_of_login_app_password > 20:
                    self.button_plus = Button(self, text="Suivant", font=("Courrier", 20), bg='pink',
                                              command=self.shearch_plus, width=8)
                    self.button_plus.place(x=600, y=450)
                    self.button_moins = Button(self, text="Précédent", font=("Courrier", 20), bg='pink',
                                               command=self.shearch_moins, width=8)
                    self.button_moins.place(x=735, y=450)
                if self.plus_moins:
                    self.entry_shearch = Entry(self, font=("Courrier", 20), bg='pink', width=4)
                    self.entry_shearch.place(x=710, y=200)
                    self.label_shearch_2 = Label(self, font=("Courrier", 20), bg='pink', text="Entrer le numéro")
                    self.label_shearch_2.place(x=650, y=150)
                    self.button_shearch = Button(self, text="Valider", font=("Courrier", 20), bg='pink',
                                                 command=self.shearch_affiche)
                    self.button_shearch.place(x=690, y=240)
                    self.button_shearch_2 = Button(self, text="Supprimer", font=("Courrier", 20), bg='pink',
                                                   command=self.suppr_password)
                    self.button_shearch_2.place(x=690, y=290)
                    self.plus_moins = False
                self.delete = False
                self.create = True
                self.shearch_list = {}
                i = 0
                y = -40
                self.q = 0
                for x in range(self.nbr_of_login_app_password):
                    fi = open("decrypt_name.txt", "r")
                    data = fi.readlines()[i]
                    self.r += 1
                    v = self.r % 10
                    i += 1
                    f.close()
                    if self.r <= self.a and self.r > self.b:
                        self.q += 1
                        y += 50
                        self.label_shearch = Label(self, text="{} = ".format(self.r) + data, bg='pink',
                                                   font=("Courrier", 20))
                        self.label_shearch.place(x=self.x, y=y)
                        self.shearch_list[self.q] = self.label_shearch
                        if v == 0:
                            y = -40
                            e = self.r % 10
                            if e == 0:
                                self.x = 300
                print(self.shearch_list)

    def shearch_plus(self):
        if self.g <= self.nbr_of_login_app_password:
            self.g += 20
            self.a += 20
            self.b += 20
            self.x = 40
            self.suppr_shearch_button()
            self.shearch()

    def shearch_moins(self):
        if self.g - 20 >= 20:
            self.g -= 20
            self.a -= 20
            self.b -= 20
            self.x = 40
            self.suppr_shearch_button()
            self.shearch()

    def valider_shearch(self):
        pass

    def suppr_shearch_button(self):
        if self.create:
            i = 1
            len_shearch_list = len(self.shearch_list)
            self.delete = True
            self.create = False
            if len_shearch_list != 0:
                for x in range(len_shearch_list):
                    self.shearch_list[i].destroy()
                    i += 1

    def suppr_shearch(self):
        if self.create:
            self.r = 0
            len_shearch_list = len(self.shearch_list)
            i = 1
            self.delete = True
            self.create = False
            if len_shearch_list != 0:
                for x in range(len_shearch_list):
                    self.shearch_list[i].destroy()
                    i += 1
            if self.nbr_of_login_app_password > 20:
                self.button_moins.destroy()
                self.button_plus.destroy()
            self.entry_shearch.destroy()
            self.label_shearch_2.destroy()
            self.button_shearch.destroy()
            self.button_shearch_2.destroy()
            self.plus_moins = True
            self.a = 20
            self.b = 0
            self.x = 40
            self.g = 20

    def write_app(self):
        app = self.entry_add_password.get()
        f = open("decrypt_name.txt", "a")
        f.write(app + "\n")
        f.close()
        self.add_password_id()
        self.entry_add_password.delete(0, END)

    def write_id(self):
        id = self.entry_add_password.get()
        f = open("decrypt_login.txt", "a")
        f.write(id + "\n")
        f.close()
        self.add_password_mdp()
        self.entry_add_password.delete(0, END)

    def write_password(self):
        password = self.entry_add_password.get()
        f = open("decrypt_password.txt", "a")
        f.write(password + "\n")
        f.close()
        self.entry_add_password.delete(0, END)
        self.add_password_destroy()

    def add_password_destroy(self):
        self.label_add_password.destroy()
        self.entry_add_password.destroy()
        self.button_add_password.destroy()
        self.button_add_password_see.destroy()

    def add_password_app(self):
        if self.password_good:
            self.label_add_password = Label(self, text="Jeu/App/Site", font=("Courrier", 20), bg='pink')
            self.label_add_password.place(x=550, y=50)
            self.entry_add_password = Entry(self, font=("Courrier", 20), bg='pink', width=25)
            self.entry_add_password.place(x=450, y=100)
            self.button_add_password = Button(self, text="Valider", font=("Courrier", 20), bg='pink', width=23,
                                              command=self.write_app)
            self.button_add_password.place(x=450, y=137)

    def add_password_id(self):
        self.label_add_password['text'] = "Id/Login"
        self.button_add_password['command'] = self.write_id

    def add_password_mdp(self):
        self.button_add_password_see = Button(self, font=("Courrier", 20), bg='pink', command=self.see_password,
                                              text="See password", width=23)
        self.button_add_password_see.place(x=450, y=190)
        self.entry_add_password['show'] = "?"
        self.label_add_password['text'] = "Mdp/Password"
        self.button_add_password['command'] = self.write_password

    def see_password(self):
        password = self.entry_add_password.get()
        self.label_add_password['text'] = password
        self.after(3000, self.see)

    def see(self):
        self.label_add_password['text'] = "Mdp/Password"

    def crypt_or_and_close(self):
        if self.password_good:
            self.label_key.destroy()
            self.entry_key.destroy()
            self.button_key.destroy()
            self.crypt_or_decrypt('decrypt_password.txt', 'crypt_moitie_password.txt', self.cle_1)
            self.crypt_or_decrypt('crypt_moitie_password.txt', 'crypt_password.txt', self.cle_2)
            os.remove('decrypt_password.txt')
            os.remove('crypt_moitie_password.txt')
            self.crypt_or_decrypt('decrypt_login.txt', 'crypt_moitie_login.txt', self.cle_1)
            self.crypt_or_decrypt('crypt_moitie_login.txt', 'crypt_login.txt', self.cle_2)
            os.remove('decrypt_login.txt')
            os.remove('crypt_moitie_login.txt')
            self.crypt_or_decrypt('decrypt_name.txt', 'crypt_moitie_name.txt', self.cle_1)
            self.crypt_or_decrypt('crypt_moitie_name.txt', 'crypt_name.txt', self.cle_2)
            os.remove('decrypt_name.txt')
            os.remove('crypt_moitie_name.txt')
        self.quit()

    def valide_key(self):
        self.password_good = True
        self.label_invalid_key['text'] = ""
        mdp = self.entry_key.get()
        if mdp == "a":
            self.label_key.destroy()
            self.entry_key.destroy()
            self.button_key.destroy()
            self.crypt_or_decrypt('crypt_password.txt', 'crypt_moitie_password.txt', self.cle_1)
            self.crypt_or_decrypt('crypt_moitie_password.txt', 'decrypt_password.txt', self.cle_2)
            os.remove('crypt_moitie_password.txt')
            os.remove('crypt_password.txt')
            self.crypt_or_decrypt('crypt_login.txt', 'crypt_moitie_login.txt', self.cle_1)
            self.crypt_or_decrypt('crypt_moitie_login.txt', 'decrypt_login.txt', self.cle_2)
            os.remove('crypt_moitie_login.txt')
            os.remove('crypt_login.txt')
            self.crypt_or_decrypt('crypt_name.txt', 'crypt_moitie_name.txt', self.cle_1)
            self.crypt_or_decrypt('crypt_moitie_name.txt', 'decrypt_name.txt', self.cle_2)
            os.remove('crypt_moitie_name.txt')
            os.remove('crypt_name.txt')
        else:
            self.label_invalid_key['text'] = "Clé invalide ! "


fen = App()
fen.title("Gestionaire de mot de passe")
fen.iconbitmap('img/canena.ico')
fen.geometry("900x600")
fen.maxsize(900, 600)
fen.minsize(900, 600)
fen.config(bg='pink')
fen.mainloop()
