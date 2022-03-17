# tapsiriq 2:8-13 simvol uzunlugunda parol teyin etmeyi teleb etmek

while True:
    print("Parolunuzu teyin edin\n!!! Parolun uzunlugu ancaq 8-13 simvol arasi ola biler !!!") 
    a=input()
    if len(a)>=8 and len(a)<=13:
        print("Parol ugurla teyin edildi...")
        i=0
        print("Parolunuzu yeniden daxil edin.\nSizin 3 sansiniz var")
        while i<3:
            b=input()
            if b==a:
                print("Sizin girisiniz tesdiqlendi...")
            else:
                print("Yanlis parol!!")
                if i==2:
                    print("Siz daxil ola bilmediniz!!")
            i+=1  
        break   
                   
    else:
       print("Parolun uzunlugu serte uygun deyil!") 