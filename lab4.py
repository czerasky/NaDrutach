# zad 1
# import random
# lista = []
# mn = 2
# for x in range(10):
#     lista2 = random.randint(0, 30)
#     mn *= lista2
#     lista.append(lista2)
# lista3 = [x * 2 for x in lista]
# print(lista3)
# plik = open('plik.txt','w')
# plik.writelines(str(lista3))
# plik.close()
#
# # zad 2
# plik = open("plik.txt").read()
# print(plik)

# zad3
# with open('plik.txt','r') as plik2:
#     for tekst in plik2:
#         print(tekst,'dzien dobry\n nowy tony hawk\n tylko ze pythonowy\n')

# zad4
# class Nazakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
# 
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
# 
#     def ile_produkt(self):
#         return (str(self.ilosc) + " "  + self.jednostka_miary)
# 
#     def ile_kosztuje(self):
#         return int(self.ilosc * self.cena_jed)
# 
# truskawki = Nazakupy("truskawki", 3, "kg", 2)
# print(truskawki.ile_produkt())
# print(truskawki.ile_kosztuje())
