from datetime import date

class Rendeles:
    def __init__(self, arucikkek):
        self._datum = date.today()
        self._reszletek = ''
        self.arucikkek = arucikkek

    def osszegez(self):
        return sum([arucikk.ar + arucikk.szallitasi_koltseg for arucikk in self.arucikkek])

    def kifizet(self, vevo, kartyaszam = None, lejarati_datum = None):
        pass