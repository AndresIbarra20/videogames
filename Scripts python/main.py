from random import randint
import os
status_menu=True

def main_menu():
    global status_opts
    status_opts=True
    print(":::MAIN MENU:::")
    print("[1]. Star game")
    print("[2]. Help")
    print("[3]. Exit")
    while status_opts:
        opt = int(input("Press any option"))
        if opt <1 or opt >3:
            print("caballo, dijite una opcion valida")
        else:
            status_opts =False
    return opt
    
while status_menu:
    os.system('clear')
    op=main_menu()
    if op==1:
        os.system('clear')
        print("Que comience el juego")
        
        players=int(input("ingrese el numero de jugadores [1:4]"))
        print("::: Menu de NIveles :::")
        print("[1]. Basico")
        print("[2]. intermedio")
        print("[3]. Avanzado")
        print("[4]. Experto")
        opt=int(input("press any option"))
        
        if   opt==1:
             pos=20
        elif opt==2:
             pos=30
        elif opt==3:
             pos=50
        else:
             pos=100
        
        # Que empicen los juegos del hambre 
        status_game=True
        roll_count=0
        roll_acum=0
        while status_game:
            os.system('clear')
            key= input("precione cualquier tecla para tirar los dados")   
            dice1=randint(1,6)
            dice2=randint(1,6)
            
            print(f"Dice1 :{dice1}")
            print(f"Dice1 :{dice2}")
            total= dice1 + dice2
            print(F"total del tiro {total}:")
             
            
            roll_count +=1
            roll_acum += total
            print(F"total del tjuego {roll_acum}:")
            
            if roll_acum >=pos:
                print("Felicidades ,Tu eres el ganador en tantos perdedores")
                status_game=False
            os.system('pause')
        print ("Estadisticas")
        print ( f"Total de tiros :{roll_count}")
        print ( f"Total dices :{roll_acum}")

            
        
        key=input("PRESS ANY KEY TO GO TO THE MAIN MENU")
        
        
    elif op==2:
        
        print(" ayuda en construccion para que nos jodas la vida")
        key=input("PRESS ANY KEY TO GO TO THE MAIN MENU")
        
    else:
        
        print(" Hasta la visa baby")
        key=input("PRESS ANY KEY TO exit")
        
        break
        


