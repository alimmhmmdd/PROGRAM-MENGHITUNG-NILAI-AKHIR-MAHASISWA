

from ast import If

print("Authorized By : M. Khoirul Alim")

print("PROGRAM MENGHITUNG NILAI AKHIR MAHASISWA")


nama = input("Masukan Nama: ")
nim = input("Masukan nim: ")
matkul = input("Masukan Mata Kuliah: ")
partisipasi = int(input("masukan nilai partisipasi: "))
tugas = int(input("masukan nilai tugas: "))
uts = int(input("masukan nilai uts: "))
uas = int(input("masukan nilai uas: "))

nilai_akhir = (partisipasi + tugas + uts + uas) / 4



def cetakHasil():
    print("-------------HASIL PERHITUNGAN------------")
    print("Nama: ",nama)
    print("NIM: ",nim)
    print("Mata Kuliah: ",matkul)

    print("Nilai Partisipasi:",partisipasi)
    print("Nilai Tugas:",tugas)
    print("Nilai UTS:",uts)
    print("Nilai UAS:",uas)
    print("Nilai Akhir:",nilai_akhir)


def hitungNilai():
    if nilai_akhir >= 85 and nilai_akhir <= 100:
        print("Grade: A")
    elif nilai_akhir >= 80 and nilai_akhir <= 85:
        print("Grade: A-")
    elif nilai_akhir >= 75 and nilai_akhir <= 80:
        print("Grade: B+")
    elif nilai_akhir >= 70 and nilai_akhir <= 75:
        print("Grade: B")
    elif nilai_akhir >= 65 and nilai_akhir <= 70:
        print("Grade: B-")
    elif nilai_akhir >= 60 and nilai_akhir <= 65:
        print("Grade: C+")
    elif nilai_akhir >= 55 and nilai_akhir <= 60:
        print("Grade: C")
    elif nilai_akhir >= 40 and nilai_akhir < 55:
        print("Grade: D")
    elif nilai_akhir < 40:
        print("Grade: E")

    if nilai_akhir < 55:
        print("Anda Tidak Lulus Mata Kuliah Ini, Tetap Semangat :))")
    else:
        print("Selamat Anda Lulus Mata Kuliah Ini")



if (partisipasi < 0 or partisipasi > 100) or (tugas < 0 or tugas > 100) or (uts < 0 or uts > 100) or (uas < 0 or uas > 100): 
    print("Input nilai melebihi 100 atau kurang dari 0, silahkan mengulang kembali")
else:
    cetakHasil()
    hitungNilai()

