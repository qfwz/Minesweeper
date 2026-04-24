import os
import random

#5x5 grid
line = "- - - - - - - - - - - - - - -"
box = ["💣", "⬛" , "💥" , "🚩", "⬜","🟨"]
numbers = ["0️⃣ ","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ "]


isi = [[],[],[],[],[]]

table = [   [],
            [],
            [],
            [],
            []    ]

dirs = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),         (0,1),
    (1,-1),  (1,0), (1,1)
]

#table
for i in range(5):
    for j in range(5):
        chance = random.randint(1,100)
        if chance < 30:
            isi[i].append(box[0])
        else:
            isi[i].append(box[1])
            
for i in range(5):
    for j in range(5):
        table[i].append(box[4])
        
        
#board
def board():
    print(f"    K1   K2   K3   K4   K5", end="\n")
    for i in range(5):
        for j in range(5):
            if j == 0:
                print(f"B{i+1}",end="")
            print(f"|{table[i][j]:^4}" ,end="")
        print(f"|\n{line:^20}")
        
def check(baris,kolom):
    display = 0

    for dx, dy in dirs:
        nx = baris + dx
        ny = kolom + dy

        if 0 <= nx < 5 and 0 <= ny < 5:
            if isi[nx][ny] == box[0]:
                display += 1

    table[baris][kolom] = f" {numbers[display]} "
    
def win():
    iswinning = True
    
    for i in range(5):
        for j in range(5):
            if isi[i][j] != box[3] and table[i][j] == box[4]:
                iswinning = False
                
    return iswinning
    
def boom():
    for i in range(5):
        for j in range(5):
            if isi[i][j] == box[0]:
                table[i][j] = box[0]
            # PSEUDOCODE
            # KALAU isi(indeks saat ini) == bomb:
            #       table(indeks saat ini) => bomb
            
        
#loop
while True:
    try:
        board()
        print("1.open a box\n2.flag a box")
        choice = int(input("pick:"))
        if choice == 1:
            print("pilih 0 untuk cancel")
            baris = int(input("pilih baris ke:"))-1
            kolom = int(input("pilih kolom ke:"))-1
            
            if baris == -1 or kolom == -1:
                raise ValueError
            
            if table[baris][kolom] != box[4]:
                input("harus pilih kotak kosong!")
                os.system("cls")
                continue
            
            elif isi[baris][kolom] == box[0]:
                for i in range (len(table)):
                    for j in range (len(table[i])):
                        if isi[i][j] == box[0]:
                            table[i][j] = box[0]
                table[baris][kolom] = box[2]
                os.system("cls")
                board()
                print("Game Over! It's a mine. 💣 ")
                break
                
            elif isi[baris][kolom] == box[1]:
                check(baris,kolom)
                input("bukan bomb!")
                os.system("cls")
            
         #flag
        elif choice == 2:
            baris = int(input("pilih baris ke:"))-1
            kolom = int(input("pilih kolom ke:"))-1
            if table[baris][kolom] == box[4]:
                table[baris][kolom] = box[3]
            os.system("cls")
        
        if win():
            board()
            boom()
            print("You win")
            break
        
    except ValueError:
        os.system("cls")
    except:
        input("invalid input")
        os.system("cls")
        
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    