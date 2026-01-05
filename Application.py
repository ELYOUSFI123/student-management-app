import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import cv2
import mysql.connector
from customtkinter import *
import re
class Etudiant:
    def __init__(self,root):
        
         # Connexion à la base de données MySQL
        self.conn = mysql.connector.connect(

            host="localhost",
            user="root",
            password="",
            database="etudiants"
            
        )
        self.c = self.conn.cursor()
        
        self.database_info()

        self.create_interface()
    def run_script(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="etudiants"
        )

        # Création du curseur
        self.c = self.conn.cursor()
        self.c.execute('''SELECT id,etud_id,dat,tim,nom,prenom,email,tel 
                        from listepresence join etudiant 
                       on listepresence.etud_id=etudiant.cne''')
    def run_compte(self):
      subprocess.run(["python", "compte.py"])   

    def create_interface(self) :  

        self.cne = StringVar()
        self.last_name = StringVar()
        self.first_name = StringVar()
        self.email = StringVar()
        self.tel =StringVar()
        self.delet= StringVar()
        self.serch1=StringVar()
        self.serch2=StringVar()

        self.root = root
        self.root.geometry('1680x1080')
        self.root.title('Gestion  des étudiants')
        #self.root.configure(background='#008080')
        img=PhotoImage(file='icon\\graduated.png')
        self.root.iconphoto(False,img)
        self.root.resizable(True, True) # Fixer l'écran

        premier_frame=Frame(self.root)
     
        
       # title=Label(premier_frame , text="Les information d'etudiant",fg="black",font=('monospace',10))
        #title.pack(side="top")
        
        # Éléments de l'interface utilisateur pour gérer les étudiants
        Label(premier_frame, text="CNE:",font=20).pack()
        self.id_entry = Entry(premier_frame,textvariable=self.cne,justify='center',font=2)
        self.id_entry.pack()

        Label(premier_frame, text="Prénom:",font=20).pack()
        self.first_name_entry = Entry(premier_frame,textvariable=self.first_name,font=2,justify='center')
        self.first_name_entry.pack()

        Label(premier_frame, text="Nom:",font=20).pack()
        self.last_name_entry = Entry(premier_frame,textvariable=self.last_name,justify='center',font=2)
        self.last_name_entry.pack()

        Label(premier_frame, text="Email:",font=20).pack()
        self.email_entry = Entry(premier_frame,textvariable=self.email,justify='center',font=2)
        self.email_entry.pack()
         
        Label(premier_frame, text="Telephone:",font=20).pack()
        self.tel_entry = Entry(premier_frame,textvariable=self.tel,justify='center',font=2)
        self.tel_entry.pack()
        
        #prendre_photo_button = Button(self.root, text="Prandre une photo", command=self.scan_presence)
        #prendre_photo_button.pack()
        
        Label(premier_frame,text='Supprimer par (CNE)',font=20).pack()
        self.delet_entry=Entry(premier_frame,textvariable=self.delet,justify='center',font=2)
        self.delet_entry.pack()
        
        premier_frame.place(x=1090,y=3,height=400,width=200)
        
        #------------- bouton ----------------------
        dexieme_frame = Frame(self.root)
        dexieme_frame.place(x=1090, y=340, width=250, height=400)
        #icon2=PhotoImage(file='icon\\settings.png')
        #self.root.dexieme_frame.iconpoto(False,icon2)
        font=CTkFont(size=20)
        #----- boutons ajouter, supprimer, modifier, quitter ....  ------
        #ajoute = CTkButton(dexieme_frame, border_width=2, 
        #width=180, height=38,text_color='white',border_color='white',
        #font=font,fg_color='#351100',text='Ajouter Étudiant',command=self.add_Etudiant)
        #ajoute.place(x=10, y=120)
        
        supprime =CTkButton(dexieme_frame, border_width=2, 
        width=180, height=38,text_color='white',border_color='white',
        font=font,fg_color='#351100', text='Supprimer',command= self.delete_etudiant)
        supprime.place(x=10,y=110)
        
        modifie = CTkButton(dexieme_frame, border_width=2, 
        width=180, height=34,text_color='white',border_color='white',
        font=font,fg_color='#351100', text='Modifier',command= self.modifie_etudiant)
        modifie.place(x=10,y=145)

        clear = CTkButton(dexieme_frame,border_width=2, 
        width=180, height=38,text_color='white',border_color='white',
        font=font,fg_color='#351100', text='Clear les champs',command=self.clear_entries)
        clear.place(x=10,y=180)


        img_quit=PhotoImage(file='icones\\icons8-fermer-48.png')
        exite =CTkButton(dexieme_frame, 
        width=180, height=40,text_color='white',border_color='white',border_width=2, 
        font=font,fg_color='#351100',text="Creer compte",command=self.run_compte)
        exite.place(x=10, y=220)


        exite = CTkButton(dexieme_frame,width=180, height=30,border_color='white',
                          border_width=2,text="Quitter",font=font,fg_color='#ff2626'
        ,text_color="white",command=self.quit_app)
        exite.place(x=10, y=260)
        #-------------------------------------------------------
        Troi_freme = Frame(self.root, bg="gray")
        Troi_freme.place(x=1, y=0, width=1100, height=60)

        searche = Label(Troi_freme, text='Chercher un etudiant :',width=20 ,bg='white')
        searche.place(x=12, y=12)

        combo_search = ttk.Combobox(Troi_freme, justify='right',textvariable=self.serch1)
        combo_search['value'] = ('CNE','Nom', 'Prenom')
        combo_search.set('CNE')
        combo_search.place(x=150, y=12)

        self.search_entry = Entry(Troi_freme,justify='center',textvariable=self.serch2)
        self.search_entry.place(x=300, y=12)

        search_bt = CTkButton(Troi_freme,width=180, height=35,text_color='black',border_color='white',border_width=2, 
        font=font,fg_color='#C0C0C0', text="Recherche",command=self.chercher_etudiant)
        search_bt.place(x=450, y=12)


        #-------- Afiche frame ---------
        self.affiche_frame = Frame(self.root)
        self.affiche_frame.place(x=1, y=60, width=1100, height=900)
        #---------scroll----------------
        scroll_x = Scrollbar(self.affiche_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.affiche_frame, orient=VERTICAL)
        scroll_x.place(x=5)
        #--------- treeveim--------
        self.etudiant_table = ttk.Treeview(self.affiche_frame,
                                            columns=('CNE', 'Nom', 'Prenom', 'Email', 'Telephon'))
        xscrollcommand = scroll_x.set,
        yscrollcommande = scroll_y.set

        self.etudiant_table.place(x=20, y=1, width=1100, height='580')
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.etudiant_table.xview)
        scroll_y.config(command=self.etudiant_table.yview)

        #------ remplisage les case superiuer de table-------
        self.etudiant_table['show'] = 'headings'
        self.etudiant_table.heading('CNE', text='CNE')
        self.etudiant_table.heading('Nom', text='Nom')
        self.etudiant_table.heading('Prenom', text='Prenom')
        self.etudiant_table.heading('Email', text='Email')
        self.etudiant_table.heading('Telephon', text='Telephon')

        self.etudiant_table.column('#0', minwidth=0)  # Cacher la première colonne
        self.etudiant_table.column('CNE', minwidth=120)  # Ajuster la largeur minimale de la colonne CNE
        self.etudiant_table.column('Nom', minwidth=150)  # Ajuster la largeur minimale de la colonne Nom
        self.etudiant_table.column('Prenom', minwidth=150)  # Ajuster la largeur minimale de la colonne Prenom
        self.etudiant_table.column('Email', minwidth=200)  # Ajuster la largeur minimale de la colonne Email
        self.etudiant_table.column('Telephon', minwidth=120)  # Ajuster la largeur minimale de la colonne Telephon
  
        self.fatche_all()
        self.etudiant_table.bind("<ButtonRelease-1>",self.get_cursor)
        
     
     
     
     
     
     #---------------creation des tables dans la base de donnees-------
    
    def database_info(self):
        #self.conn = mysql.connector.connect(host="localhost", user="root",password="",database="etudiants")
        self.c.execute('''CREATE TABLE IF NOT EXISTS etudiant(
                        cne VARCHAR(255) PRIMARY KEY,
                        nom VARCHAR(255),
                        prenom VARCHAR(255),
                        email VARCHAR(255),tel VARCHAR(255))''')
        self.conn.commit()  

     #------------------ajouter un etudiant------------------      

    def add_Etudiant(self):
     if not self.first_name.get() or not self.last_name.get() or not self.email.get() or not self.tel.get() or not self.cne.get():
          messagebox.showinfo("Info", "Tous les champs doivent être remplis.")
     else:
          # Vérifier si l'adresse e-mail est valide en utilisant une expression régulière
         email_pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
         if not re.match(email_pattern, self.email.get()):
             messagebox.showerror("Erreur", "Veuillez saisir une adresse e-mail valide.")
         else:
            try:
                self.c.execute(
                    "INSERT INTO etudiant (cne, nom, prenom, email, tel) VALUES (%s, %s, %s, %s, %s)",
                    (self.cne.get(), self.first_name.get(), self.last_name.get(), self.email.get(), self.tel.get())
                )
                self.conn.commit()
                messagebox.showinfo("Succès", "Étudiant ajouté avec succès!")
                self.clear_entries()
                self.fatche_all()
            except mysql.connector.Error as e:
                messagebox.showerror("Erreur", "Erreur lors de l'ajout de l'étudiant : " + str(e))
     self.con.close()
 
    #------get_cursor  (selection )--------------------
    def get_cursor (self,ev) :
        cursor_row=self.etudiant_table.focus()
        contents =self.etudiant_table.item(cursor_row)
        row=contents['values']
        if row:
         self.cne.set (row[0])
         self.last_name.set (row[1])
         self.first_name.set(row[2])
         self.email.set(row[3])
         self.tel.set(row[4])
    #----------modification-------------
    
    def modifie_etudiant(self) : 
        con = mysql.connector.connect(host='localhost', user='root', password='', database='etudiants')
        cur = con.cursor()
       
          # Vérifier si l'adresse e-mail est valide en utilisant une expression régulière
        email_pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, self.email_entry.get()):
             messagebox.showerror("Erreur", "Veuillez saisir une adresse e-mail valide.")
        else:     
         cur.execute("UPDATE etudiant SET nom=%s, prenom=%s, email=%s, tel=%s WHERE cne=%s",
         (self.first_name.get(), self.last_name.get(), self.email.get(), self.tel.get(), self.cne.get()))
         con.commit()
         self.fatche_all()
         con.close()
  
    #-----------------------------




     #----affiche dans ecran (select * table )----------
    def fatche_all(self):
        con = mysql.connector.connect(host='localhost', user='root', password='', database='etudiants')
        cur = con.cursor()

        cur.execute('SELECT * FROM etudiant')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.etudiant_table.delete(*self.etudiant_table.get_children())
            for row in rows:
                self.etudiant_table.insert("", "end", value=row)
            con.commit()
        con.close()             
     #-------supprim-------------------
    def liste_presence(self):
         #-----------------liste absence table---------
        self.liste_table = ttk.Treeview(self.affiche_frame,
                                        columns=('CNE', 'Nom', 'Prenom', 'Email', 'Telephon','Date','Time'))
        self.liste_table.place(x=20, y=200, width=1100, height='580')
             #------ remplisage les case superiuer de table-------
        self.liste_table['show'] = 'headings'
        self.liste_table.heading('CNE', text='CNE')
        self.liste_table.heading('Nom', text='Nom')
        self.liste_table.heading('Prenom', text='Prenom')
        self.liste_table.heading('Email', text='Email')
        self.liste_table.heading('Telephon', text='Telephon')
        self.liste_table.heading('Date', text='Date')
        self.liste_table.heading('Time', text='Time')
        self.liste_table.column('CNE', width=130)
        self.liste_table.column('Nom', width=130)
        self.liste_table.column('Prenom', width=130)
        self.liste_table.column('Email', width=130)
        self.liste_table.column('Telephon', width=130) 
        self.liste_table.column('Date', width=130)
        self.liste_table.column('Time',width=130 )

        self.liste_table.bind("<ButtonRelease-1>",self.get_cursor)
        con = mysql.connector.connect(host='localhost', user='root', password='', database='etudiants')
        cur = con.cursor()

        cur.execute('''SELECT etud_id,nom,prenom,email,tel,dat,tim
                        from listepresence join etudiant 
                       on listepresence.etud_id=etudiant.cne''')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.liste_table.delete(*self.liste_table.get_children())
            for row in rows:
                self.liste_table.insert("", "end", value=row)
            con.commit()
        con.close()  
    def liste_absence(self):
        self.table_abs= ttk.Treeview(self.affiche_frame,
                                            columns=('CNE', 'Nom', 'Prenom', 'Email', 'Telephon'))
        self.table_abs.place(x=20, y=400, width=1100, height=580)
        #------ remplisage les case superiuer de table-------
        self.table_abs['show'] = 'headings'
        self.table_abs.heading('CNE', text='CNE')
        self.table_abs.heading('Nom', text='Nom')
        self.table_abs.heading('Prenom', text='Prenom')
        self.table_abs.heading('Email', text='Email')
        self.table_abs.heading('Telephon', text='Telephon')

        self.table_abs.column('CNE', width=130)
        self.table_abs.column('Nom', width=130)
        self.table_abs.column('Prenom', width=130)
        self.table_abs.column('Email', width=130)
        self.table_abs.column('Telephon', width=130)  
        con = mysql.connector.connect(host='localhost', user='root', password='', database='etudiants')
        cur = con.cursor()

        cur.execute(''' SELECT etudiant.cne, etudiant.nom, etudiant.prenom, etudiant.email, etudiant.tel
                     FROM etudiant
                   LEFT JOIN listepresence ON listepresence.etud_id = etudiant.cne
            WHERE listepresence.etud_id IS NULL;''')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table_abs.delete(*self.table_abs.get_children())
            for row in rows:
                self.table_abs.insert("", "end", value=row)
            con.commit()
        con.close()  
        self.table_abs.bind("<ButtonRelease-1>",self.get_cursor)

           

    def delete_etudiant(self):
      con = mysql.connector.connect(host='localhost', user='root', password='', database='etudiants')
      cur = con.cursor()

      cne = self.delet.get()  # Récupérer le CNE à partir de l'entrée

      if not cne:
          messagebox.showinfo("Info", "Veuillez entrer le CNE de l'étudiant à supprimer!")
      else:
          
            cur.execute('SELECT * FROM etudiant WHERE cne=%s', (cne,))
            if cur.fetchone() is None:
               messagebox.showerror("Erreur", "Aucun étudiant avec ce CNE={} n'a été trouvé!".format(cne))
            else:
                cur.execute('DELETE FROM etudiant WHERE cne=%s', (cne,))
                con.commit()
                self.fatche_all()
                messagebox.showinfo("Succès", "L'étudiant a été supprimé avec succès!")
      con.close()



    #-------------------chercher un etudiant-------------
    def chercher_etudiant(self):
        self.con = mysql.connector.connect(host='localhost', user='root', password='', database='etudiants')
        self.c = self.con.cursor() 
        if not self.serch1.get() or not  self.serch2.get(): 
            messagebox.showinfo("Info", "Veuillez entrer le champ de l'étudiant à chercher!")  
        else:
           self.c.execute("SELECT * FROM etudiant WHERE "+ str(self.serch1.get())+" like '%"+str(self.serch2.get())+"%'")
            
           rows =self.c.fetchall()
           if len(rows) != 0:
              self.etudiant_table.delete(*self.etudiant_table.get_children())
           for row in rows:
                self.etudiant_table.insert("", "end", value=row) 
           self.con.commit()
        self.con.close()

     #---------------clear les champs de saisir----------------
    def clear_entries(self):
        
        self.id_entry.delete(0, END)
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.tel_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.delet_entry.delete(0,END)
        self.fatche_all()


     #--------------quiter le programme---------

    def quit_app(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()
            
           
root = Tk()
app = Etudiant(root)
root.mainloop()
