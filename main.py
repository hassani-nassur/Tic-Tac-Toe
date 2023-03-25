import tkinter as tk
from tkinter import messagebox,ttk
import ia
import time,json
# from fonctionJeux import *

def accueil():
    
    global btn_play_ia,btn_play_joueur,btn_quit,labelPartie
    if 'btn_play_ia' and 'btn_play_joueur' in globals():
        btn_play_ia.destroy()
        btn_play_joueur.destroy()
    
    if 'canvas' in globals():
        if 'btn_replay' in globals():
            btn_replay.destroy()
        for key,value in enumerate(list):
            list[key]=None
        canvas.destroy()
        
    if 'form' in globals():
            form.destroy()
            
    if 'labelscore' in globals():
        labelscore.destroy() 
    
    if 'labelPartie' in globals():
        labelPartie.destroy()
                
    if 'btn_next_part' in globals():
        btn_next_part.destroy() 
    if 'btn_replay' in globals():
        btn_replay.destroy() 
    if 'mot' in globals():
        mot.destroy()   
    #button jouer avec ordinateur
    btn_play_ia = tk.Button(premiere_fn,text="Jouer avec l'ordi",font=("calibri 14"),fg="black",bg='#a7d9f5',width=15,command=Ia_game)
    btn_play_ia.pack(padx=10,pady=75)

    # button 2 joueur
    btn_play_joueur = tk.Button(premiere_fn,text="2 joueur",font=("calibri 14"),fg="black",bg='#a7d9f5',width=15,command=jouer)
    btn_play_joueur.pack(padx=10,pady=15)
    
    # Quiter
    btn_quit = tk.Button(premiere_fn,text="Quiter",font=("calibri 14"),fg="black",bg='#a7d9f5',width=15,command=premiere_fn.quit)
    btn_quit.place(x=370,y=370)

#jouer avec l'ordinateur 
def Ia_game():
    
    # destruction des deux btn
    btn_play_ia.destroy()
    btn_play_joueur.destroy()
    
    global form
    form = tk.Canvas(premiere_fn,width=300,height=300,bg="#a7d9f5")
    form.pack(padx=12,pady=50)
    
    # definition des variable globale
    global nameplayer_one,nameplayer_two,symboleJoueur,nombrePartie
    
    # champs nom joueur
    label_nameplayer_one = tk.Label(form,text="Name player :",font=("times new roman",15),width=15,bg="#a7d9f5")
    label_nameplayer_one.place(x=20,y=35)
    
    nameplayer_one = tk.Entry(form,fg="black",font=("times new roman",14),name="1")
    nameplayer_one.place(x=40,y=70,width=155,height=30)
    
    # champ symbole joueur
    symboleJoueur = ttk.Combobox(form,font=("times new roman",14),stat='readonly',justify="center")
    symboleJoueur["values"] = ("X","O")
    symboleJoueur.current(0)
    symboleJoueur.place(x=205,y=70,width=80,height=30)
    
    # nombre de partie
    label_nbr_partie = tk.Label(form,text="Nombre de partie :",font=("times new roman",15),bg="#a7d9f5")
    label_nbr_partie.place(x=40,y=150)
    
    nombrePartie = ttk.Combobox(form,font=("times new roman",14),stat='readonly',justify="center")
    nombrePartie["values"] = ("1","3","5","10","15")
    nombrePartie.current(0)
    nombrePartie.place(x=205,y=150,width=80,height=25)
    
    # button de soumission du formulaire
    btn_nameplayer = tk.Button(form,text="Valider",command=downloadData,bg="#0e69a9",fg='#ffffff',font=("times new roman",14))
    btn_nameplayer.place(x=180,y=260,width=100,height=30)
    
def jouer():
    
    # destruction des 3 boutton
    btn_play_ia.destroy()
    btn_play_joueur.destroy()
    # btn_quit.destroy()
    
    global form
    form = tk.Canvas(premiere_fn,width=300,height=300,bg="#a7d9f5")
    form.pack(padx=12,pady=50)
    
    global nameplayer_one,nameplayer_two,symboleJoueur,nombrePartie
    
    label_nameplayer_one = tk.Label(form,text="Name player 1 :",font=("times new roman",15),width=15,bg="#a7d9f5")
    label_nameplayer_one.place(x=20,y=35)
    nameplayer_one = tk.Entry(form,fg="black",font=("times new roman",14),name="2")
    nameplayer_one.place(x=40,y=70,width=155,height=30)
    
    symboleJoueur = ttk.Combobox(form,font=("times new roman",14),stat='readonly',justify="center")
    symboleJoueur["values"] = ("X","O")
    symboleJoueur.current(0)
    symboleJoueur.place(x=205,y=70,width=80,height=30)
    
    
    label_nameplayer_two = tk.Label(form,text="Name player 2 :",font=("times new roman",15),width=15,bg="#a7d9f5")
    label_nameplayer_two.place(x=20,y=115)
    nameplayer_two = tk.Entry(form,fg="black",font=("times new roman",14))
    nameplayer_two.place(x=40,y=150,width=155,height=30)
    
    # # nombre de partie
    label_nbr_partie = tk.Label(form,text="Nombre de partie :",font=("times new roman",15),bg="#a7d9f5")
    label_nbr_partie.place(x=40,y=200)
    
    nombrePartie = ttk.Combobox(form,font=("times new roman",14),stat='readonly',justify="center")
    nombrePartie["values"] = ("1","3","5","10","15")
    nombrePartie.current(0)
    nombrePartie.place(x=205,y=200,width=80,height=25)
    
    btn_nameplayer = tk.Button(form,text="Valider",command=downloadData,bg="#0e69a9",fg="#ffffff",font=("times new roman",14))
    btn_nameplayer.place(x=180,y=260,width=100,height=30)

# recuperation des donnée du formulaire

def downloadData():
    global symbol_player_one,player_one,player_two,nbr_partie,nowPart,score_player_one,score_player_two,id_one,id_two,players,scores
    
    score_player_one = 0
    score_player_two = 0
    nowPart = 1
    nbr_partie = int(nombrePartie.get())
    
    symbol_player_one = symboleJoueur.get()
    player_one = nameplayer_one.get()
    
    if int(str(nameplayer_one)[-1]) == 1:
        player_two = 'Ordinateur'
    else:
        player_two = nameplayer_two.get()
    
    if(player_one == "" or player_two == ""):
        messagebox.showerror("Erreur","Tous les champs doivent être remplis")
    else:
        try:
            with open("db.json","r") as db:
                data = json.load(db)
        except Exception:
            file = open("db.json","w")
            data = {'players':[],'Scores':[]}
            file.write(json.dumps(data))
            file.close()
        
        if(data != {}):
            
            players = data["players"]
            scores = data["Scores"]
            id_one = id_two = None
            
            for i in players:
                if player_one == i["name"]:
                    id_one = i["idplayer"]
                elif player_two == i["name"]:
                    id_two = i["idplayer"]
            # file = open("db.json","w")
            
            if id_one == None:
                
                id_one = len(players)
                edit = {
                    "idplayer":id_one,
                    "name":player_one
                }
                players.append(edit)   
            
            if(id_two == None):
                
                id_two = len(players)
                edit = {
                    "idplayer":len(players),
                    "name":player_two
                }
                players.append(edit)
        
        form.destroy()
        global play
        play = symbol_player_one
        initaliseList()
        
# renitialisation de la teble de jeu
def initaliseList():
    global nowPart,score_player_two,score_player_one
    
    for key,value in enumerate(list):
        list[key] = None
        
    if 'btn_replay' in globals():
        btn_replay.destroy()
    if 'canvas' in globals():
        canvas.destroy()
    if 'labelPartie' in globals():
        labelPartie.destroy()
    table_player()
    
    if(play == symbol_player_one):
        message("{} à Vous de joueur \"{}\"".format(player_one,symbol_player_one))
    else:
        message("{} à Vous de joueur \"{}\"".format(player_two,play))
# afficage du score
def score():
    global labelscore
    labelscore = tk.Label(premiere_fn,font=("times new roman",14),text = "Score \n\n{} : {} \n{} : {}".format(player_one,score_player_one,player_two,score_player_two),bg="#a7d9f5")
    labelscore.place(x=460,y=100,width=135,height=140)   
# table de jeu 
def table_player():
    global canvas,score_player_one,score_player_two,labelPartie
    
    labelPartie = tk.Label(premiere_fn,text="Partie : {}".format(nowPart),bg="#a7d9f5",font=("times new roman",15))
    labelPartie.place(x=470,y=30,width=120,height=40)
    
    canvas = tk.Canvas(premiere_fn,width=300,height=300,bg="#ffffff")
    canvas.pack(padx=12,pady=50)
      
    # Les cases du jeu
    global c0,c1,c2,c3,c4,c5,c6,c7,c8
    
    c0 = tk.Label(canvas,name="0",bg='#a7d9f5')
    c0.place(x=5,y=5,width=95,height=95)
        
    c1 = tk.Label(canvas,name="1",bg='#a7d9f5')
    c1.place(x=105,y=5,width=95,height=95)
        
    c2 = tk.Label(canvas,name="2",bg='#a7d9f5')
    c2.place(x=205,y=5,width=95,height=95)
        
    c3 = tk.Label(canvas,name="3",bg='#a7d9f5')
    c3.place(x=5,y=105,width=95,height=95)
        
    c4 = tk.Label(canvas,name="4",bg='#a7d9f5')
    c4.place(x=105,y=105,width=95,height=95)
        
    c5 = tk.Label(canvas,name="5",bg='#a7d9f5')
    c5.place(x=205,y=105,width=95,height=95)
        
    c6 = tk.Label(canvas,name="6",bg='#a7d9f5')
    c6.place(x=5,y=205,width=95,height=95)
        
    c7 = tk.Label(canvas,name="7",bg='#a7d9f5')
    c7.place(x=105,y=205,width=95,height=95)
        
    c8 = tk.Label(canvas,name="8",bg='#a7d9f5')
    c8.place(x=205,y=205,width=95,height=95)
    
    canvas.bind_class('Label','<Button>',Action)

# fonction executer lors d'un click 
def Action(event):
    # recuperation de l'element cliqué
    element = event.widget
    text = element.cget("text")
    element.config(font=("new times roman",50))
    indexCase = int(str(element)[-1])
    
    global play,list
    
    if(player_two == "Ordinateur"):
        if(text == "" and list[indexCase] == None):
            
            event.widget.config(text = play)
            list[indexCase] = play
            
            if play == "O" :
                symbole_ordi = "X"
            else:
                symbole_ordi = "O"
            
            game_over(list)
            
            if not win and None in list:
                play_ia = ia.ia(list,symbole_ordi)
                if(play_ia[0]==0):
                    c0.config(text=symbole_ordi)
                    c0.config(font=("new times roman",50))
                elif(play_ia[0] == 1):
                    c1.config(text=symbole_ordi)
                    c1.config(font=("new times roman",50))
                elif(play_ia[0] == 2):
                    c2.config(text=symbole_ordi)
                    c2.config(font=("new times roman",50))
                elif(play_ia[0] == 3):
                    c3.config(text=symbole_ordi)
                    c3.config(font=("new times roman",50))
                elif(play_ia[0] == 4):
                    c4.config(text=symbole_ordi)
                    c4.config(font=("new times roman",50))
                elif(play_ia[0] == 5):
                    c5.config(text=symbole_ordi)
                    c5.config(font=("new times roman",50))
                elif(play_ia[0] == 6):
                    c6.config(text=symbole_ordi)
                    c6.config(font=("new times roman",50))
                elif(play_ia[0] == 7):
                    c7.config(text=symbole_ordi)
                    c7.config(font=("new times roman",50))
                elif(play_ia[0] == 8):
                    c8.config(text=symbole_ordi) 
                    c8.config(font=("new times roman",50))
                list[play_ia[0]] = symbole_ordi
                game_over(list) 
    else:
        if(play == "X"):
            if(text == "" and list[indexCase] == None):
                
                event.widget.config(text=play)
                list[indexCase] = play
                play = "O"
        else:
            if(text =="" and list[indexCase] == None):
                event.widget.config(text=play)
                list[indexCase] = play
                play = "X"
        game_over(list)

# verification de la fin du jeu
def game_over(list):
    
    global win
    win = False
    if(list[0] == list[1] == list[2] and (list[2] == "O" or list[2] == "X")):
        c0.config(font = ("new times roman",70),bg = "green")
        c1.config(font = ("new times roman",70),bg = "green")
        c2.config(font = ("new times roman",70),bg = "green")
        win = True
        win_player(list[2])
        
    elif(list[3] == list[4] == list[5] and (list[4] == 'O' or list[4] == 'X')):
   
        c3.config(font = ("new times roman",70),bg = "green")
        c4.config(font = ("new times roman",70),bg = "green")
        c5.config(font = ("new times roman",70),bg = "green")
        win = True
        win_player(list[4])

    elif (list[6] == list[7] == list[8] and (list[7] == 'O' or list[7] == 'X')):
        
        c6.config(font = ("new times roman",70),bg = "green")
        c7.config(font = ("new times roman",70),bg = "green")
        c8.config(font = ("new times roman",70),bg = "green")
        win = True
        win_player(list[7])
 
    elif (list[0] == list[3] == list[6] and (list[3] == 'O' or list[3] == "X")):
        c0.config(font = ("new times roman",70),bg = "green")
        c3.config(font = ("new times roman",70),bg = "green")
        c6.config(font = ("new times roman",70),bg = "green")
        win = True
        win_player(list[3])

    elif (list[1] == list[4] == list[7] and (list[4] == "O" or list[4] == "X")):
        c1.config(font = ("new times roman",70),bg = "green")
        c4.config(font = ("new times roman",70),bg = "green")
        c7.config(font = ("new times roman",70),bg = "green")
        win = True
        win_player(list[4])

    elif (list[2] == list[5] == list[8] and (list[5] == "O" or list[5] == 'X')):
        c2.config(font = ("new times roman",70),bg = "green")
        c5.config(font = ("new times roman",70),bg = "green")
        c8.config(font = ("new times roman",70),bg = "green")
        win = True
        win_player(list[5])
    elif (list[0] == list[4] == list[8] and (list[4]=='O' or list[4]=="X")):
        c0.config(font = ("new times roman",70),bg="green")
        c4.config(font = ('new times roman',70),bg="green")
        c8.config(font = ("new times roman",70),bg="green")
        win = True
        win_player(list[4])

    elif(list[2] == list[4] == list[6] and (list[4] == "O" or list[4] == "X")):
        c2.config(font = ("new times roman",70),bg = "green")
        c4.config(font = ("new times roman",70),bg = "green")
        c6.config(font = ("new times roman",70),bg = "green")
        win = True
        win_player(list[4])

    else:
        again = False
        for i in list:
            if(i == None):
                again = True
        if(not again):
            message("Match Null","#ffe5ae")
            global btn_next_part
            btn_next_part = tk.Button(premiere_fn,text="prochaine Partie",command = again_player,font = ("times new roman",15))
            btn_next_part.place(x=10,y=370,width=160,height=40)
                

# verification du joueur remportant une partie
def win_player(l):
    
    global nowPart,score_player_one,score_player_two,btn_next_part
    if(l == symbol_player_one ):
        
        score_player_one += 5
        if(player_two == "Ordinateur"):
            message("Vous avez gagnez","#FFD700")
        else:
            message("{} à gager la partie".format(player_one),"#FFD700")
            
    else:
        score_player_two += 5
        if(player_two == "Ordinateur"):
            message("Vous Avez perdu","#a60808")
        else:
            message("{} à gager la partie".format(player_two),"#FFD700")
    canvas.unbind_class("Label",'<Button>')
    
    if(nowPart < nbr_partie):
        btn_next_part = tk.Button(premiere_fn,text = "prochaine Partie",bg = "#a7d9f5",command = again_player,font = ("times new roman",15))
        btn_next_part.place(x=10,y=370,width=160,height=40)
    else:
        temps = time.strftime("%d/%M/%Y %H:%M:%S")
        score1 = {
            "idscore" :len(scores),
            "nameScore" : score_player_one,
            "idplayer":id_one,
            "timePlayer": temps
        }
        score2 = {
            "idscore" :len(scores) +1,
            "nameScore" : score_player_two,
            "idplayer":id_two,
            "timePlayer": temps
        }
        scores.append(score1)
        scores.append(score2)
        file = open("db.json","w")
        data = {"players":players,"Scores":scores}
        file.write(json.dumps(data,indent=True))
        file.close()
        again_player()
    
    if 'labelscore' in globals():
        labelscore.destroy()
    score()
# rejouer
def rejouer():
    global nowPart,nbr_partie,score_player_one,score_player_two,nbr_partie
    if nowPart == nbr_partie:
        nowPart = 1
        score_player_one = 0
        score_player_two = 0
    if 'labelscore' in globals():
        labelscore.destroy()
    initaliseList()
# relacer le jeu   
def again_player():
        
    global btn_replay,nowPart
    btn_replay = tk.Button(premiere_fn,text="Rejouer",bg="#a7d9f5",command = rejouer,font = ("times new roman",15))
    btn_replay.place(x=10,y=30,width=120,height=40)
    
    if(nowPart < nbr_partie):
        nowPart += 1
        initaliseList()
        if 'btn_next_part' in globals():
            btn_next_part.destroy()
# message venceur
def message(msg, color = "black"):
    global mot,x_max
    mot = tk.Label(premiere_fn, font = ("Arial", 15),text="",bg = "#2f929f",justify = "center")
    mot.config(text = msg,fg = color)
    mot.place(x=190,y=190,height=50)
    x_max = 20 
    animMessage()  

list = [None,None,None,None,None,None,None,None,None]

# animationi du message venqueure
speed =  230 #1000 = 1s
pos = 10

def animMessage():
    global pos
    global x_max,mot
    mot.config(font=("times new roman",15,"bold"))
    if pos <= x_max:
        pos +=1
        mot.after(speed,animMessage)
    if pos == x_max:
        pos = 10  
        mot.destroy() 


# premier interface
premiere_fn = tk.Tk()
premiere_fn.title("Tic tac toe")

premiere_fn.config(background="#0e69a9")
premiere_fn.geometry("600x450+500+160")
premiere_fn.resizable(width=False,height=False)

menu = tk.Menu(premiere_fn)

menu.add_command(label="Accueil",command=accueil)
# menu.add_command(label="Nouveau jeu")
# menu.add_command(label="Historique")

accueil()

premiere_fn.config(menu=menu)
premiere_fn.mainloop()
