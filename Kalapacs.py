from Arucikk import Arucikk

class Kalapacs(Arucikk):
    def __init__(self, ar, szin):
        super().__init__(ar, 1)
        self.szin = szin
        self._nev = "Kalapács"
