row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

print (row1, row2, row3, sep="\n")

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
