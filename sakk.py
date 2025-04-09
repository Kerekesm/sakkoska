tabla = [["" for _ in range(8)] for _ in range(8)]
felso = ["b","l","f","kn","k","f","l","b"]
also = ["B","L","F","KN","K","F","L","B"]

# Inicializáljuk a táblát
tabla[0] = felso
tabla[1] = ["p"]*8
tabla[6] = ["P"]*8
tabla[7] = also

def kirajzol():
    print("   A  B  C  D  E  F  G  H")
    for r in range(8):
        print(f"{8 - r} ", end=" ")
        for c in range(8):
            m = tabla[r][c]
            if m:
                print(f"{m:<3}", end="")
            else:
                print(".  " if (r+c)%2==0 else ",  ", end="")
        print()

def lepes(parancs):
    try:
        innen, oda = parancs.split()
        c1, r1 = ord(innen[0].upper()) - 65, 8 - int(innen[1])
        c2, r2 = ord(oda[0].upper()) - 65, 8 - int(oda[1])
        b = tabla[r1][c1]
        if b == "P" and c1 == c2 and r2 == r1 - 1 and not tabla[r2][c2]:
            tabla[r2][c2], tabla[r1][c1] = b, ""
        elif b == "p" and c1 == c2 and r2 == r1 + 1 and not tabla[r2][c2]:
            tabla[r2][c2], tabla[r1][c1] = b, ""
        else:
            print("Érvénytelen lépés!")
    except:
        print("Hibás formátum! Használat: pl. E2 E3")

# Fő ciklus
while True:
    kirajzol()
    cmd = input("Lépés (pl. E2 E3, vagy 'kilep'): ")
    if cmd.lower() == "kilep":
        break
    lepes(cmd)
