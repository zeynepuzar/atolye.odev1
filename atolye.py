x = 3
x = float(x)
print(x)
print(type(x))

y = 4.5
y = int(y)
print(y)
print(type(y))

z = "8"
z = int(z)
print(z)
print(type(z))

a = "12"
a = float(a)
print(a)
print(type(a))

'''
b = "46.8"
b = int(b)
print(b)
print(type(b))
'''


ahmet = 29
zeynep = 21
ali = 41
dicle = 21

print(ahmet > zeynep)
print(ali < zeynep)
print(dicle == zeynep)

#and
print(ali > zeynep and ahmet <= ali)
print(dicle > ali and zeynep == ahmet)
#or
print(ali >= ahmet or zeynep != ali)
print(zeynep != dicle or ahmet >= zeynep)
print(ali <= dicle or zeynep >= ahmet)
#not
print(not(ahmet > 30))
print(not(zeynep > 18 and zeynep < 62))

x = int(input( "Lütfen bir sayı giriniz: "))
y = int(input( "Lütfen bir sayı daha giriniz: "))
print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x // y)
print(y ** x)

isim = input("Lütfen isminizi giriniz: ")
yas = input("Lütfen yaşınızı giriniz: ")
sehir = input("Lütfen nerede yaşadığınızı yazınız: ")
meslek = input("Lütfen yaptığınız mesleği giriniz: ")
print("Merhaba " + isim + ". "  + yas + " yaşındasın" + ". " + sehir + " şehrinde yaşıyorsun" + ". " +  meslek + " olarak görev yapıyorsun" + ". ")

atolye = "Hi-Kod Veri Bilimi Atölyesi"

print(atolye.split())
print(atolye.upper())
print(atolye.lower())

sayilar = "0123456789"
cift_sayi = sayilar[::2]
tek_sayi = sayilar[1::2]
print(cift_sayi)
print(tek_sayi)
