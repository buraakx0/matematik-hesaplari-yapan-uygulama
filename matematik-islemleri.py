print("-" * 40)
print("Matematik işlemleri yapan uygulamaya hoşgeldiniz!")
print("-" * 40)
print("1 - Üs hesaplama")
print("2 - Karenin kenarlarını hesaplama")
print("3 - Dikdörtgen kenarlarını hesaplama\n")
yapilacak = int(input("Yapılacak işlemi belirtiniz: "))

if yapilacak == 1:
    usAlt = int(input("Sayıyı giriniz: "))
    usUs = int(input("Sayının üst kuvventini giriniz: "))
    usHesap = usAlt ** usUs
    print("İşleminizin sonucu: {}".format(usHesap))

if yapilacak == 2:
    kareUzun = int(input("Karenin kenarının uzunluğunu giriniz: "))
    kareSonuc = kareUzun * 4
    print("İşleminizin sonucu: ",kareSonuc)

if yapilacak == 3:
    dikKısa = int(input("Dikdörtgenin kısa kenarının uzunluğunu giriniz: "))
    dikUzun = int(input("Dikdörtgenin uzun kenarının uzunluğunu giriniz: "))
    dikKısaHesap = dikKısa * 2
    dikuzunHesap = dikUzun * 2
    dikToplam = dikKısaHesap + dikuzunHesap
    print("İşleminizin sonucu: ",dikToplam)

# python matematik-islemleri.py