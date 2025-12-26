""MINION GAME""

def minion_game(string):
    k=0
    s=0
    v="AEIOU"
    for i in range(len(string)):
        if string[i] in v:
            k+=len(string)-i
        else:
            s+=len(string)-i
        
    if k>s:
            print("kelvin",k)
    elif s>k:
            print("stuart",s)
    else:
            print("Draw")
if__name__="__main__"           
s=input()
minion_game(s)
