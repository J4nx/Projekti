class Tuote:
    tuote = ""
    hinta = 0.00

    def __init__(self, t, h):
        self.tuote = t
        self.hinta = h
    
    def Tulostin(self):
        print(self.tuote, self.hinta, "€")
        print("")
