def caesar(og):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result=""
    n=int(input("Enter shift distance: "))
    for i in range(len(og)):
        result+=alpha[i+n]
    print(result)

def hexcode(og):
    result=""
    for i in og:
        result+=str(hex(ord(i)))
    result=result.replace("0x"," ")
    print(result)

def chesslock(og):
    result=""
    rows=[1,2,3,4,5,6,7,8]
    columns=["A","B","C","D","E","F","G","H"]
    table=[]
    for col in columns:
        for row in rows:
            table.append(col+str(row))
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. "
    grid={alpha[i]:table[i] for i in range(len(alpha))}
    for i in og:
        if i in grid:
            result+=grid[i]
        else:
            result+=i
    print(result)

def hypercube(og):
    W=["A","B","C"]
    X=["Q","R","S"]
    Y=["x","y","z"]
    Z=["1","2","3"]
    table=[]
    result=""
    for i in W:
        for j in X:
            for k in Y:
                for l in Z:
                    table.append(i+j+k+l)
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,?!:'()[]{}-+*/=_ "
    grid={alpha[i]:table[i] for i in range(len(alpha))}
    for i in og:
        if i in grid:
            result+=grid[i]
        else:
            result+=i
    print(result)    

def LexGunn(og):
    #I have no idea what this will do, but it came together beatifully;
    #Lex luthor from James Gunn's Superman and The Lex, a pistol in Warframe
    pass

def encychoice(og):
    keys={"Rome":caesar,"16":hexcode,"Gambit":chesslock,"4D":hypercube}
    choice=input("Enter key: ").strip()
    if choice in keys:
        return keys[choice](og)
    else:
        print("Invalid.")
    
