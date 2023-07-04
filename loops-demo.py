import random
sayi=random.randint(1,10)
hak=4
sayac=0
puan=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahmin:'))
    puan=(hak+1)*20

    if sayi==tahmin:
        print(f'Tebrikler {sayac}. Defada Bilginiz.Puanınız:{puan}')
        break
    # elif tahmin<sayi:
    #     print('Lütfen Daha Yüksek Bir Sayı Giriniz.')
    # elif tahmin>sayi:
    #     print('lütfen Daha Küçük Bir Sayı Giriniz.')  
    
    if hak==0:
        print(f'Hakkınız Bitti.Tutulan Sayi:{sayi}')      





