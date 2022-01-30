vize1 = int(input("1. Vize puanınızı yazınız.."))
kısasınav1 = int(input("1. Kısa Sınav puanınızı yazınız.."))
final = int(input("Final puanınızı yazınız.."))
kısasınav2 = int(input("2. Kısa sınavınızı giriniz.."))
performans = int(input("Performans  Sınavınızı Giriniz.."))
Toplam_Not = final * 50 / 100 + vize1 * 25 / 100 + kısasınav1 * 5 / 100 + kısasınav2 * 5 / 100 + performans * 15/100


if(Toplam_Not >= 90):
    print("AA")
elif(Toplam_Not >= 85):
    print("BA")
elif (Toplam_Not >= 80):
    print("BB")
elif(Toplam_Not >= 75):
    print("CB")
elif (Toplam_Not >= 70):
    print("CC")
elif(Toplam_Not >= 65):
    print("DC")
elif (Toplam_Not >= 60):
    print("DD")
elif(Toplam_Not >=45):
    print("Geçtiniz")

else:
    print("ZORTLADINIZ..")


