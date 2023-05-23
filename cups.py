class Cups:
    def __init__(self, cups, subsistema):
        self.cups = cups
        self.subsistema = subsistema

    def getPais(self):
        if self.cups.startswith("ES"):
            return "España"
        elif self.cups.startswith("PT"):
            return "Portugal"
        raise Exception("Cups no válido")
