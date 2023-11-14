# 1. Programı başlat.
# 2. Bir sayaç (Sayac) değerini 0 olarak başlat.
sayac = 0

# 3. S değerini kullanıcıdan al.
S = int(input("Bölmek istediğiniz sayıyı girin: "))

# 4. B değerini kullanıcıdan al.
B = int(input("Bölen değerini giriniz: "))

# 5. S değerini B değerinden çıkar.
# 6. Sayacı bir arttır.
while S > B:
    S = S - B
    sayac += 1

# 9. BM (Bölme Sonucu) değerini Sayac olarak al.
BM = sayac

# 10. BM ve S değerlerini yazdır.
print("BM:", BM)
print("S:", S)

# 11. Programı bitir.
cikis=input("Çıkmak için herhangibir tuşa basınız")