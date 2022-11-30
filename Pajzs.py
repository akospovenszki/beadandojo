from Arucikk import Arucikk

class Pajzs(Arucikk):
    def __init__(self, ar, tomeg, atmero):
        super().__init__(ar, tomeg)
        self.atmero = atmero
        self._nev = "Pajzs"
