from Arucikk.Pajzs import Pajzs
from Arucikk.Kalapacs import Kalapacs
from Rendeles import Rendeles
from Vevo import Vevo

thor = Vevo("Thor - Isten", 350)
vasember = Vevo("Vasember - Szuperhős", 500)

fizet1 = Rendeles([Kalapacs(30, 10, 60), Pajzs(150, "Metál")])
fizet2 = Rendeles([Pajzs(200, "Vörös-Szükre")])

fizet1.kifizet(thor, "4152-1261-7231-3616", "04/24")
fizet2.kifizet(vasember)

print(fizet1)
print(fizet2)
