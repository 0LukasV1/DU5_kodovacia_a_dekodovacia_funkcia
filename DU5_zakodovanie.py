def zak(kod,veta):
    vet = ""
    a=0
    for o in range(0, len(veta)):
        for i in kod:
            if a> len(veta)-1:
                a = a - len(veta)
                b = ord(veta[a])
                c = ord(i)
                vet += chr(((((c + b) - 97) % 26) + 97))
            else:
                b = ord(veta[a])
                a += 1
                c = ord(i)
                vet += chr(((((c+b) - 97) % 26) + 97))
        return vet

print(zak("kocur","macka"))

print(zak("aabaabaab","aabaz"))
