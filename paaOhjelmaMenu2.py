from luokat import Tuote

#Ateriat
juustoAteria = Tuote("Juustohampurilaisateria", 6.50)
tuplajuustoAteria = Tuote("Tuplajuustohampurilaisateria", 7.50)
kanaAteria = Tuote("Kanahampurilaisateria", 7.00)
vegeAteria = Tuote("Vegehampurilaisateria", 6.50)
pekoniAteria = Tuote("Pekonihampurilaisateria", 8.00)
#Hampurilaiset
juusto = Tuote("Juustohampurilainen", 3.00)
tuplajuusto = Tuote("Tuplajuustohampurilainen", 3.50)
kana = Tuote("Kanahampurilainen", 3.30)
vege = Tuote("Vegehampurilainen", 3.00)
pekoni = Tuote("Pekonihampurilainen", 4.00)
#Juomat
cola = Tuote("Coca-Cola", 2.50)
fanta = Tuote("Fanta", 2.50)
pepsi = Tuote("Pepsi", 2.50)
sprite = Tuote("Sprite", 2.50)
vesi = Tuote("Vesi", 1.00)
#Lisukkeet
ranskalaiset = Tuote("Ranskalaiset", 3.00)
bataatti = Tuote("Bataattiranskalaiset", 3.50)
nugetit = Tuote("Kananugetit", 4.50)
mozzarella = Tuote("Mozzarellatikut", 4.50)
miniporkkanat = Tuote("Miniporkkanat", 2.50)
#Jälkiruuat
pehmis = Tuote("Pehmis", 1.50)
jaatelo = Tuote("Jäätelö", 2.50)
pirtelo = Tuote("Pirtelö", 2.50)
muffinssi = Tuote("Muffinssi", 2.50)
keksi = Tuote("Keksi", 1.00)
#listat
ateriat = [juustoAteria, tuplajuustoAteria, kanaAteria, vegeAteria, pekoniAteria]
hampurilaiset = [juusto, tuplajuusto, kana, vege, pekoni]
juomat = [cola, fanta, pepsi, sprite, vesi]
lisukkeet = [ranskalaiset, bataatti, nugetit, mozzarella, miniporkkanat]
jalkiruuat = [pehmis, jaatelo, pirtelo, muffinssi, keksi]

def ValikkoPrint():
    
    print("Numeroilla 1-5 saat ruokalistat sekä hinnat näkyviin")
    print("Numerolla 0 saat tilauksesi yhteenvedon ja hinnan") #"voit vielä muokata tilaustasi tai siirtyä maksamaan")
    print("1. Ateriat")
    print("2. Juomat")
    print("3. Hampurilaiset")
    print("4. Lisukkeet")
    print("5. Jälkiruuat")
    print("0. Valmis, siirry maksamaan")
    return

#Pääkoodi alkaa
tilaus = []

print("Hei, saisinko tilauksenne?")

while True:
    ValikkoPrint()
    valinta = int(input())
    if valinta == 1:
        print("1.", ateriat[0].tuote, ateriat[0].hinta,"€")
        print("2.", ateriat[1].tuote, ateriat[1].hinta,"€")
        print("3.", ateriat[2].tuote, ateriat[2].hinta,"€")
        print("4.", ateriat[3].tuote, ateriat[3].hinta,"€")
        print("5.", ateriat[4].tuote, ateriat[4].hinta,"€")
        print("Lisää haluamasi tuote syöttämällä tuotenumero terminaaliin")
        #print("Poistu valinnalla 0.") 
        
        tempValinta = int(input())
        if tempValinta != 0:
            tilausNumero = tempValinta - 1
            print(tilausNumero)
            tilaus.append(ateriat[tilausNumero])   

        elif tempValinta == 0:
            break
        print("Tilaukseen lisätty: ", tilaus[-1].tuote)
        print("")
               
    elif valinta == 2:
        print("1.", juomat[0].tuote, juomat[0].hinta,"€")
        print("2.", juomat[1].tuote, juomat[1].hinta,"€")
        print("3.", juomat[2].tuote, juomat[2].hinta,"€")
        print("4.", juomat[3].tuote, juomat[3].hinta,"€")
        print("5.", juomat[4].tuote, juomat[4].hinta,"€")

        tempValinta = int(input())
        if tempValinta != 0:
            tilausNumero = tempValinta - 1
            print(tilausNumero)
            tilaus.append(juomat[tilausNumero])   

        elif tempValinta == 0:
            break
        print("Tilaukseen lisätty: ", tilaus[-1].tuote)
        print("")

    elif valinta == 3:
        print("1.", hampurilaiset[0].tuote, hampurilaiset[0].hinta,"€")
        print("2.", hampurilaiset[1].tuote, hampurilaiset[1].hinta,"€")
        print("3.", hampurilaiset[2].tuote, hampurilaiset[2].hinta,"€")
        print("4.", hampurilaiset[3].tuote, hampurilaiset[3].hinta,"€")
        print("5.", hampurilaiset[4].tuote, hampurilaiset[4].hinta,"€")

        tempValinta = int(input())
        if tempValinta != 0:
            tilausNumero = tempValinta - 1
            print(tilausNumero)
            tilaus.append(hampurilaiset[tilausNumero])   

        elif tempValinta == 0:
            break
        print("Tilaukseen lisätty: ", tilaus[-1].tuote)
        print("")

    elif valinta == 4:
        print("1.", lisukkeet[0].tuote, lisukkeet[0].hinta,"€")
        print("2.", lisukkeet[1].tuote, lisukkeet[1].hinta,"€")
        print("3.", lisukkeet[2].tuote, lisukkeet[2].hinta,"€")
        print("4.", lisukkeet[3].tuote, lisukkeet[3].hinta,"€")
        print("5.", lisukkeet[4].tuote, lisukkeet[4].hinta,"€")

        tempValinta = int(input())
        if tempValinta != 0:
            tilausNumero = tempValinta - 1
            print(tilausNumero)
            tilaus.append(lisukkeet[tilausNumero])   

        elif tempValinta == 0:
            break
        print("Tilaukseen lisätty: ", tilaus[-1].tuote)
        print("")

    elif valinta == 5:
        print("1.", jalkiruuat[0].tuote, jalkiruuat[0].hinta,"€")
        print("2.", jalkiruuat[1].tuote, jalkiruuat[1].hinta,"€")
        print("3.", jalkiruuat[2].tuote, jalkiruuat[2].hinta,"€")
        print("4.", jalkiruuat[3].tuote, jalkiruuat[3].hinta,"€")
        print("5.", jalkiruuat[4].tuote, jalkiruuat[4].hinta,"€")

        tempValinta = int(input())
        if tempValinta != 0:
            tilausNumero = tempValinta - 1
            print(tilausNumero)
            tilaus.append(jalkiruuat[tilausNumero])   

        elif tempValinta == 0:
            break
        print("Tilaukseen lisätty: ", tilaus[-1].tuote)
        print("")

    elif valinta == 0: #Breakin the loop when 0
        break
    
    else:        
        print("Tarkasta valintasi")
        
#Tilauksen esikatselu ja hinta

tilausYhteen = 0
print("\n"*10) 
print("Tilauksesi sisältää seuraavat tuotteet: ")
print("")
for i in range(len(tilaus)):
    tilausYhteen += tilaus[i].hinta
    tilaus[i].Tulostin()
    i +=1
print("Tilauksesi on yhteensä: ",tilausYhteen, "€")