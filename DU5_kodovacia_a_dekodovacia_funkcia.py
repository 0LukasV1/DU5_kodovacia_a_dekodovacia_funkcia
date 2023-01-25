def sif(txt,posun):
    a=""
    for i in range(0,len(txt)):
        if txt[i] != " ":
            b=ord(txt[i])
            c=((((b-97)+posun)%26)+97)
            a+=chr(c)
        else:
            a+=" "
    return a

print(sif("lukas vojtek",2))

#dešifrovanie
def desifrovanie(txt):
    a=""
    for i in range(1,26):
        for h in range(0,len(txt)):
            if txt[h] != " ":
                b = ord(txt[h])
                c = ((((b - 97) + i) % 26) + 97)
                a += chr(c)
            else:
                a+=" "
        print(a,end="\n")
        a=""

print(desifrovanie(sif("lukas vojtek",4)))