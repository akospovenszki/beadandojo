class Arucikk:
    def __init__(self, ar, tomeg):
        self.ar = ar
        self._tomeg = tomeg
        self._szallitasi_koltseg = self.szallitas(tomeg)
        self._nev = ""


    @tomeg.setter
    def tomeg(self, ertek):
        self._tomeg = ertek
        self._szallitasi_koltseg = self.szallitas(ertek)


    def szallitas(self, tomeg):
        return tomeg + (tomeg / 100)


    @property
    def szallitasi_koltseg(self):
        return self._szallitasi_koltseg

    @property
    def tomeg(self):
        return self._tomeg
