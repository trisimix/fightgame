import random
import tkinter
###############################################
#MAIN MENU WINDOW
def boxer():
    global cclass
    cclass="boxer"
    gameplay()
def kickboxer():
    global cclass
    cclass="kickboxer"
    gameplay()
def wrestler():
    global cclass
    cclass="wrestler"
    gameplay()

def menug():
    global menu
    menu=tkinter.Tk()
    menu.title("Fight Game - Menu")
    menu.geometry("300x300")
    menu.configure(background="#7F0404", cursor="dot")
    menu.attributes("-fullscreen",True)
    print("Game initialised.\n")

    title=tkinter.Label(menu, text="Fight Game", font=("Courier", 28, "bold"), pady=20,bg="#7F0404", fg="white")
    boxert=tkinter.Button(menu, text="Boxer", command=boxer, pady=20, width=100)
    kickboxert=tkinter.Button(menu, text="Kick Boxer",command=kickboxer, pady=20, width=100)
    wrestlert=tkinter.Button(menu, text="Wrestler",command=wrestler, pady=20, width=100)
    mexit=tkinter.Button(menu, text="Exit", command=exit)

    mexit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    title.pack()
    boxert.pack()
    kickboxert.pack()
    wrestlert.pack()
###############################################
#GAME WINDOW
def gameplay():
    global menu
    menu.destroy()
    window=tkinter.Tk()
    window.title("Fight Game - Playing")
    window.geometry("640x480")
    window.configure(background="#7F0404", cursor="dot")
    window.attributes("-fullscreen",True)
    global basehp
    global health
    global cclass
    tdmg=0
    if cclass=="boxer":
        pmodifier=1.5
        kmodifier=0.5
        gmodifier=0.25
        health=125
        basehp=125
    elif cclass=="kickboxer":
        pmodifier=0.75
        kmodifier=1.5
        gmodifier=0.25
        health=125
        basehp=125
    elif cclass=="wrestler":
        pmodifier=0.5
        kmodifier=0.5
        gmodifier=2
        health=175
        basehp=175

    global ehealth
    ehealth=int(round(health*1.25))
    global emodifier
    emodifier=1.3
    global ebasehp
    ebasehp=ehealth

    global pwin
    pwin=0

    def pwin():
        global ehealth
        if ehealth<=0:
            ehealthl.configure(text="Health: 0"+"/"+str(ebasehp))
            print("Player has won")
            global pwin
            pwin=1
            winner.configure(text="Player has won")

    def ewin():
        global health
        if health<=0:
            healthl.configure(text="Health: 0"+"/"+str(basehp))
            print("Enemy has won")
            global pwin
            pwin=1
            winner.configure(text="Enemy has won")

    def echance():
        global pwin
        global tdmg
        
        if pwin!=1:
            global health
            missche=random.randint(0,13)
            echance=random.randint(0,13)
            if echance>=5:
                if missche>=11:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(10,20)*emodifier))
                    health-=dmgdealt
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(int(round(health)))+"/"+str(basehp))
                    enemymove.configure(text="Enemy used: Punch(Damage dealt: "+(str(dmgdealt))+")")
                    
            elif echance>=10:
                if missche>=10:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(14,26)*emodifier))
                    health-=dmgdealt
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(health)+"/"+str(basehp))
                    enemymove.configure(text="Enemy used: Kick(Damage dealt: "+(str(dmgdealt))+")")
            
            elif echance<=4:
                chance=1
                while chance<7:
                    dmgdealt=random.randint(2,7)*emodifier
                    tdmg+=int(round(dmgdealt))
                    health-=dmgdealt
                    chance=int(round(random.randint(0,11)))
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(int(round(health)))+"/"+str(basehp))
                enemymove.configure(text="Enemy used: Grapple(Damage dealt: "+(str(tdmg))+")")           
            tdmg=0
    def punchp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=11:
                print("Player attack missed!")
            else:
                global dmgdealtp
                dmgdealtp=int(round(random.randint(9,21)*pmodifier))
                ehealth-=dmgdealtp
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()


    def kickp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=10:
                print("Player attack missed!")
            else:
                global dmgdealtp
                dmgdealtp==int(round(random.randint(14,26)*kmodifier))
                ehealth-=dmgdealtp
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()

    def grapplep():
        if pwin!=1:
            global ehealth
            chance=1
            while chance<7:
                dmgdealtp=random.randint(2,7)*gmodifier
                tdmgp+=dmgdealtp
                ehealth-=dmgdealtp
                chance=int(round(random.randint(0,11)))
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
            playerddealt.configure(text="Damage dealt to enemy: "+str(tdmgp))
            tdmgp=0                
            pwin()
            echance()
            ewin()
    def restart():
        print("\nNew game loaded\n")
        window.destroy()
        menug()
		
    player=tkinter.Label(window, text="Player", font=("Courier", 24, "bold"))
    healthl=tkinter.Label(window, text=("Health: "+str(health)+"/"+str(basehp)), font=("Courier", 18))
    enemy=tkinter.Label(window, text="Enemy", font=("Courier", 24, "bold"))
    ehealthl=tkinter.Label(window, text=("Health: "+str(ehealth)+"/"+str(ebasehp)), font=("Courier", 18))
    punch=tkinter.Button(window, text="Punch",command=punchp)
    kick=tkinter.Button(window, text="Kick", command =kickp)
    grapple=tkinter.Button(window, text="Grapple", command=grapplep)
    restart=tkinter.Button(window, text="Restart", command=restart)
    texit=tkinter.Button(window, text="Exit", command=exit)
    enemymove=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404",fg="white")
    playerddealt=tkinter.Label(window,text="", font=("Courier", 14), bg="#7F0404", fg="white")
    winner=tkinter.Label(window, text="", font=("Courier", 14, "bold"), bg="#7F0404", fg="white")

    texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    player.pack(pady=10, padx=20, fill=tkinter.X)
    healthl.pack()
    punch.pack(pady=5)
    kick.pack(pady=5)
    grapple.pack(pady=5)
    playerddealt.pack()
    enemy.pack(pady=10, padx=20, fill=tkinter.X)
    ehealthl.pack()
    enemymove.pack()
    restart.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    winner.pack(side=tkinter.BOTTOM)

#Initialises the game
menug()
