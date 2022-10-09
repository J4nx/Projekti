from luokat import Menu

ruoka = Menu()










print("Hei, saisinko tilauksenne?")
print("Numeroilla 1-5 saat ruokalistat sekä hinnat näkyviin")
print("Numerolla 0 saat tilauksesi yhteenvedon ja hinnan, voit vielä muokata tilaustasi tai siirtyä maksamaan")


while valinta != 0:
    print("1. Ateriat")
    print("2. Juomat")
    print("3. Hampurilaiset")
    print("4. Lisukkeet")
    print("5. Jälkiruuat")
    print("0. Valmis, siirry maksamaan")

    valinta = int(input())
    if valinta == 1:
        ruoka = Menu(ruoka)
        print(ruoka)

    elif valinta == 2:
        x = 
    elif valinta == 3:
        y = 
    elif valinta == 4:
        z = 
    elif valinta == 5:
        f = 
    elif valinta == 0: #Breakin the loop when 0
        break
    else:
        print("Tarkasta valintasi")

#Tilauksen esikatselu ja hinta



