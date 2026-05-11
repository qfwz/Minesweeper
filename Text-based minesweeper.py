import os
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

box = ["💣", "⬛" , "💥" , "🚩", "⬜","🟨"]
numbers = ["0️⃣ ","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ "]


inside = []

play_box = []

while True:
    clear()
    print("Welcome to Minesweeper!")

    try:
        size = (int(input("Choose box size:\n1.4x4\n2.6x6\n3.8x8\npick:")) + 1) * 2
        if size not in [4, 6, 8]:
            raise ValueError
    except ValueError:
        continue

    break

for i in range(size):
    play_box.append([])
    inside.append([])

dirs = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),         (0,1),
    (1,-1),  (1,0), (1,1)
]

#table
for i in range(size):
    for j in range(size):
        chance = random.randint(1,100)
        if chance < 30:
            inside[i].append(box[0])
        else:
            inside[i].append(box[1])
            
for i in range(size):
    for j in range(size):
        play_box[i].append(box[4])
        
        
#board
def board():
    print("   ", end="")
    
    # header kolom
    for i in range(size):
        print(f" C{i+1} ", end=" ")
    print()

    # isi board
    for i in range(size):
        print(f"R{i+1}", end="")
        
        for j in range(size):
            print(f"|{play_box[i][j]:^3}", end="")
            
        print("|")
        
def check(baris,kolom):
    display = 0

    for dx, dy in dirs:
        nx = baris + dx
        ny = kolom + dy

        if 0 <= nx < size and 0 <= ny < size:
            if inside[nx][ny] == box[0]:
                display += 1

    play_box[baris][kolom] = f" {numbers[display]} "
    
def win():
    iswinning = True
    
    for i in range(size):
        for j in range(size):
            if play_box[i][j] != box[3] and inside[i][j] == box[4]:
                iswinning = False
                
    return iswinning
    
def boom():
    for i in range(size):
        for j in range(size):
            if inside[i][j] == box[0]:
                play_box[i][j] = box[0]
            # PSEUDOCODE
            # KALAU inside(indeks saat ini) == bomb:
            #       play_box(indeks saat ini) => bomb
            
        

# DEBUG
for i in range(size):
    for j in range(size):
        inside[i][j] = box[0]
inside[0][0] = box[1]

while True:
    clear()
    try:
        board()
        print("1. Open a box\n2. Flag a box/Remove flag")
        choice = int(input("pick:"))
        if choice == 1:
            print("Type 0 to cancel")
            baris = int(input("Pick row (R):"))-1

            if baris == -1:
                raise ValueError
            
            kolom = int(input("Pick column (C):"))-1
            
            if kolom == -1:
                raise ValueError
            
            if play_box[baris][kolom] != box[4]:
                input("Must choose an empty box!")
                continue
            
            elif inside[baris][kolom] == box[0]:
                for i in range (len(play_box)):
                    for j in range (len(play_box[i])):
                        if inside[i][j] == box[0]:
                            play_box[i][j] = box[0]
                play_box[baris][kolom] = box[2]
                clear()
                board()
                print("Game Over! It's a mine. 💣 ")
                break
                
            elif inside[baris][kolom] == box[1]:
                check(baris,kolom)
                input("Not a mine!")

            
         #flag
        elif choice == 2:
            print("Type 0 to cancel")
            baris = int(input("Pick row (R):"))-1

            if baris == -1:
                raise ValueError
            kolom = int(input("Pick column (C):"))-1

            if kolom == -1:
                raise ValueError
            if play_box[baris][kolom] == box[4]:
                play_box[baris][kolom] = box[3]
            elif play_box[baris][kolom] == box[3]:
                play_box[baris][kolom] = box[4]
            else:
                input("Already opened")
        
        if win():
            clear()
            boom()
            board()
            print("You win")
            break
        
    except ValueError:
        continue
    except:
        input("invalid input")
        continue
        
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    