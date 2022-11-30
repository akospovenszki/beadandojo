def kifizet(self, vevo, kartyaszam=None, lejarati_datum=None):

    if kartyaszam is None or lejarati_datum is None:
        self._reszletek += f'{vevo.nev} készpénzzel kíván fizetni.\n'
        fizetes = Kp(osszeg)
    else:
        self._reszletek += f'{vevo.nev} kártyával ({kartyaszam, lejarati_datum}) kíván fizetni.\n'
        fizetes = Kartya(osszeg, kartyaszam, lejarati_datum)

    tranzakc = fizetes.fizet(vevo.penz)

    if tranzakc:
        self._reszletek += f'Sikeres fizetés!\n'
        self._reszletek += f'A megvásárolt árucikkek: {", ".join([arucikk.__str__() for arucikk in self.arucikkek])}\n'
        vevo.penz -= osszeg
    else:
        self._reszletek += f'Sikertelen fizetés! :(\n'
