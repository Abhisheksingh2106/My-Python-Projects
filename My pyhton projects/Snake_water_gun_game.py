import random
# Snake, water and gun game
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
      if you == 'w':
        return False
    elif you == 'g':
        return 
    elif comp == 'w':
          if you == 'g':
                   return False
    elif you == 's':
        return 
    elif comp == 'g':
          if you == 's':
            return False
    elif you == 'w':
        return 
    
    
print("Computer Turn: Snake(s) Water(w) or Gun(g?")
randNo  = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
     comp = 'g'
     
you = input("Your's Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)
print(f"Computer Chose {comp} ")
print(f"you Chose {you} ")
if a == None:
    print("The Game is a Tie!")
elif a:
    print("you Win!")
else:
    print("you Loose!")
