'''keyfile: notes
    this is the keyfile for decoding encryption
___________________________________________________________________________________________________________________'''

def caesarkey(og):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result=""
    n=int(input("Enter shift distance: "))
    for i in og:
        result+=alpha[alpha.index(i)-n]
    print(result)
'''
I think i can diagnose the problem above. set shift to 3, no matter the input it always goes 789ABCDEF...,
set shift to 5 and you will always get 56789ABCDEF... and it DOES NOT MATTER what input you give for decoding.
adding n-=2*n to make the index [i+n] didnt work.
Solved ↓
changed it completely, now checks every character in input, and replaces it with the index 3 spaces behind,
or forward when the encode shift was negative (moves it backwards for encryption).
___________________________________________________________________________________________________________________'''

def hexkey(og):
    wk=og.split(" ")
    _list=[]
    result=""
    for i in wk:
        if i=="":
            continue
        else:
            _list.append(chr(int(i,16)))
    for i in _list:
        result+=str(i)
    print(result)
    #pass
'''
___________________________________________________________________________________________________________________'''

def chesskey(og):
    result=""
    ind=0
    rows=[1,2,3,4,5,6,7,8]
    columns=["A","B","C","D","E","F","G","H"]
    table=[]
    for col in columns:
        for row in rows:
            table.append(col+str(row))
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. "
    grid={table[i]:alpha[i] for i in range(len(alpha))}
    j=0
    while j<len(og):
        if j+1<len(og):
            pair=og[j:j+2]
            if pair in grid:
                result+=grid[pair]
                j+=2
    print(result)

def hcubekey(og):
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
    grid={table[i]:alpha[i] for i in range(len(alpha))}
    j=0
    while j<len(og):
        if j+1<len(og):
            pair=og[j:j+4]
            if pair in grid:
                result+=grid[pair]
                j+=4
    print(result)
        
def decychoice(og):
    keys={"Rome":caesarkey,"16":hexkey,"Gambit":chesskey,"4D":hcubekey}
    choice=input("Enter key: ").strip()
    if choice in keys:
        return keys[choice](og)
    else:
        print("Invalid.")
    
