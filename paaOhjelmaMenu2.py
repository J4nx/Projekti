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

#Pääkoodi alkaa

tilaus = []

def LisaaListaan(til):
    tilausNumero = tempValinta - 1
    print(tilausNumero)
    tilaus.append(til[tilausNumero])  
    print("Tilaukseen lisätty: ", tilaus[-1].tuote)
    print("")

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

def TulostaTuotteet(menu):
    print("1.", menu[0].tuote, menu[0].hinta,"€")
    print("2.", menu[1].tuote, menu[1].hinta,"€")
    print("3.", menu[2].tuote, menu[2].hinta,"€")
    print("4.", menu[3].tuote, menu[3].hinta,"€")
    print("5.", menu[4].tuote, menu[4].hinta,"€")
    print("Lisää haluamasi tuote syöttämällä tuotenumero terminaaliin")
    print("Poistu valinnalla 0.") 
    print("")

def Ehto(toiminnot):
    if tempValinta == 0:
        return 0
    elif tempValinta < 6:
        LisaaListaan(toiminnot)        
    else:
        print("Tarkasta valintasi")
        print("\n"*2)

def Yhteenveto():
    tilausYhteen = 0
    print("\n"*10) 
    print("Tilauksesi sisältää seuraavat tuotteet: ")
    print("")
    for i in range(len(tilaus)):
        tilausYhteen += tilaus[i].hinta
        tilaus[i].Tulostin()
        i +=1
    print("Tilauksesi on yhteensä: ",tilausYhteen, "€")

print("Hei, saisinko tilauksenne?")

while True:
    ValikkoPrint()
    valinta = int(input())
    if valinta == 1:
        TulostaTuotteet(ateriat)
        
        tempValinta = int(input())
        Ehto(ateriat)
                       
    elif valinta == 2:
        TulostaTuotteet(juomat)

        tempValinta = int(input())
        Ehto(juomat)

    elif valinta == 3:
        TulostaTuotteet(hampurilaiset)

        tempValinta = int(input())
        Ehto(hampurilaiset)

    elif valinta == 4:
        TulostaTuotteet(lisukkeet)

        tempValinta = int(input())
        Ehto(lisukkeet) 

    elif valinta == 5:
        TulostaTuotteet(jalkiruuat)

        tempValinta = int(input())
        Ehto(jalkiruuat)

    elif valinta == 0: #Breakin the loop when 0
        break
    
    else:        
        print("Tarkasta valintasi")
        
#Tilauksen esikatselu ja hinta
Yhteenveto()
