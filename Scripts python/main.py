from random import randint
import os
status_game=True
def main_menu():
    print(":::MAIN MENU:::")
    print("[1]. Star game")
    print("[2]. Help")
    print("[3]. Exit")
    opt = int(input("Press any option"))
    return opt
    
while status_game:
    os.system('clear')
    op=main_menu()
    if op==1:
        
        print(" Game under construction")
        key=("PRESS ANY KEY TO GO TO THE MAIN MENU")
        
    elif op==2:
        
        print(" Help under construction")
        key=("PRESS ANY KEY TO GO TO THE MAIN MENU")
        
    else:
        
        print(" Hasta la visa baby")
        key=input("PRESS ANY KEY TO exit")
        
        break
        
'''    
dice1=randint(1,6)
dice2=randint(1,6)

print(f"Dice1 :{dice1}")
print(f"Dice1 :{dice2}")
'''

