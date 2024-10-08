row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

print (row1, row2, row3, sep="\n")

def restart():
    global turns
    for i in range(3):
        row1[i] = "0"
    for i in range(3):
        row2[i] = "0"
    for i in range(3):
        row3[i] = "0"
    turns = 0

def replaceItem(typed, replacer):

    n = int(typed)
    if n < 3 and row1[n] == "0":
        row1[n] = replacer
    if 3 <= n < 6 and row2[n - 3] == "0":
        row2[n - 3] = replacer
    if 6 <= n < 9 and row3[n - 6] == "0":
        row3[n - 6] = replacer

    
    return row1, row2, row3
    


typed = input("Start with the number of the column: " )
replaceItem(typed, "x")
turns = 0
while turns < 5:
    replaceItem(typed, "x")
    turns += 1
    print (row1, row2, row3, sep="\n")
    typed = input("Start with the number of the column: " )
    replaceItem(typed, "y")
    print (row1, row2, row3, sep="\n")
    typed = input("Start with the number of the column: " )
    if typed == "done":
        restart()
    place = int(typed)

    rows = [row1, row2, row3]
    for player in "xy":
        for i in rows:
            if i[0] == player == i[1] == i[2]:
                print (f"{player.upper()} wins! rows")
    
    for i in range(3):
        if (row1[i] == row2[i] == row3[i]) and row3[i] != "0":
            print (row1[i], "wins! column")

        
        

