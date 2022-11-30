from Fizetes import Fizetes

class Kp(Fizetes):
    def __init__(self, osszeg):
        super().__init__(osszeg)

    def fizet(self, penz):
        return penz > self.osszeg
