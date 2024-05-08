#Kullanıcı'ya 10 Adet Rasgele Soru Sorar Bu Sorulara verdiği Her Doğru Cevap +5 Puan İken 
#Yanlış Verdiği Cevaplar İçin -2 Puan Krılmaktadır
# Soruları Src Klasörünün İçindeki soru.py Dosyasından Almaktadır

#kütüphaneler
import time
import random
from src.soru import *

# sayac
soru_sayac = 0
puan = 0

while soru_sayac < 10:
#rasgele soru 
    rasgele_soru = random.choice(soru_listesi)
    print(rasgele_soru)
#soru vevaplama 
    c = input("İşlem Seçin: ")
# Soru Doğrulama
    if rasgele_soru == soru1 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru2 and c == "D":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru3 and c == "E":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru4 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru5 and c == "D":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru6 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru7 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru8 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru9 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru10 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru11 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru12 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru13 and c == "D":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru14 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru15 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru16 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru17 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru18 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru19 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru20 and c == "D":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru21 and c == "D":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru22 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru23 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru24 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru25 and c == "D":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru26 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru27 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru28 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru29 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru30 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru31 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru32 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru33 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru34 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru35 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru36 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru37 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru38 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru39 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru40 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru41 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru42 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru43 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru44 and c == "A":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru45 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru46 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru47 and c == "D":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru48 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru49 and c == "B":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    elif rasgele_soru == soru50 and c == "C":
        print("Verdiğiniz Cevap Doğru")
        time.sleep(0.5)
        puan += 5
    else:
        print("Yanlış Cevap Verdiniz")
        puan -= 2
        
    soru_sayac += 1
#bitiş
print(f"\n\nTebrikler! Sorular Bitti. Toplam Puanınız: {puan}")