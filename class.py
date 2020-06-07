# CLASS (OBJECT ORIENTED PROGRAMMING/OOP)

# Class = cetakan

# Contoh 'Cetakan Hewan'
# class hewan:

#     # class attribute
#     spesies = 'kambing'

#     # instance attribute
#     def __init__(self, asal, bobot, usia): #self supaya bisa mengisi sendiri
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia

# # mengisi class hewan
# gaga = hewan('Garut', 40, 8)
# tutul = hewan('Tulungagung', 45, 7)

# # mengakses 'class attribute'
# print(f'gaga adalah seekor {gaga.__class__.spesies}')
# print(f'tutul adalah seekor {tutul.__class__.spesies}')

# Cerita
# print('Gaga adalah seekor {g.spesies}. Tutul juga seekor {t.spesies}. Gagal berasal dari {g.asal}.Sedangkan Tutul berasal dari {t.asal}.'.format(g=gaga, t=tutul))
# print('Tahun ini, Tutul menginjak usia {t.usia} tahun. Lebih muda setahun dari usia Gaga ({g.usia} tahun)'.format(g=gaga, t=tutul))
# print('Meskipun lebih muda, Tutul memiliki bobot lebih tinggi ({t.bobot} kg) daripada Gaga ({g.bobot} kg).'.format(g=gaga, t=tutul))
# ==========================================================================================================================================================================

# METHOD = function in class

# class hewan:
#     # class attribute
#     spesies = 'kambing'

#     # instance attribute
#     def __init__(self, nama, asal, bobot, usia):
#         self.nama = nama
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia
    
#     # instance METHOD/function
#     def makan(self, makanan):
#         return f'{self.nama} sedang menikmati {makanan}.'
    
#     def sate(self):
#         tusuk_sate = self.bobot * 20 
#         return f'{self.nama} bisa diolah menjadi {tusuk_sate} tusuk sate'

# # mengisi cetakan 'class'
# kambing_baru = hewan('Etawa', 'Garut', 45, 9)

# # uji coba methods
# print(kambing_baru.makan('Daun Pisang'))
# print(kambing_baru.sate()) 
# =================================================================================================
# LATIHAN MEMBUAT CLASS CALCULTATOR
# class calculator:
#     def tambah(self, x, y):
#         return x + y
#     def kurang(self, x, y):
#         return x - y
#     def kali(self, x, y):
#         return x * y
#     def bagi(self, x, y):
#         return x / y
#     def pangkat(self, x, y):
#         return x ** y

# print(calculator().tambah(4, 5))
# print(calculator().kurang(40, 5))
# print(calculator().kali(2, 7))
# print(calculator().bagi(40, 8))
# print(calculator().pangkat(4, 3))
# =======================================================================================
# LATIHAN MEMBUAT CALCULATOR STATISTIK
# Buatlah class yang berisi method dengan fitur:
# 1. Menghitung nilai minimum dalam list (tidak boleh pake built in function min())
# 2. Menghitung nilai maksimum dalam list (tidak boleh pake built in function min())
# 3. Menghitung panjang anggota dalam list (tidak boleh pakai built in function len())
# 4. Mean
# 5. Standar deviasi

data = [2, 3, 4, 5, 6, 7, 8, 8, 9, 21, 3, 2, 5, 4, 1, 5, 12]
import math

class statistic:
    # def minimum(self, yourList):
    #     min = yourList[0]
    #     for i in yourList:
    #         if i < min:
    #             min = i
    #     return min
    # def maksimum(self, yourList):
    #     maks = yourList[0]
    #     for i in yourList:
    #         if i > maks:
    #             maks = i
    #     return maks
    # def panjangList(self, yourList):
    #     hitung = 0
    #     for i in yourList:
    #         if i in yourList:
    #             hitung += 1
    #     return hitung
    def Mean(self, yourList) :
        sum = 0
        for i in yourList:
            sum += i
            Mean = sum / len(yourList)
        return Mean
    def stDev(self, yourList):
        hitung = 0
        jumlah = 0
        for i in yourList:
            hitung += i
            jumlah += 1
        mean = hitung/jumlah
        
        total = 0
        for i in yourList:
            total += (i - mean)**2
        return (total/jumlah)**0.5

# print(statistic().minimum(data))
# print(statistic().maksimum(data))
# print(statistic().panjangList(data))
print(statistic().Mean(data))
print(statistic().stDev(data))