print("--------------------------------------------------------------\n")

namaprogram= "Deret Aritmatika Test Interview MSBU Tunas"
devby= "Ananda Rauf Maududi"
devdate= "01 Oktober 2024"
print(namaprogram)
print(devby)
print(devdate)
print("--------------------------------------------------------------\n")



def deret_aritmatika(n):
    suku_pertama = 2
    beda = 3
    deret = [suku_pertama + (i * beda) for i in range(n)]
    return deret

# Contoh penggunaan
n = int(input("Masukkan jumlah suku deret: "))
hasil = deret_aritmatika(n)
print(", ".join(map(str, hasil)))
