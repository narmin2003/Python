while True:
    try:
        a=(float)(input("Birinci ededi daxil edin:"))
        b=(float)(input("Ikinci ededi daxil edin:"))
    except ValueError:
        print("yalniz eded daxil edin!")   
    else:
        break    
print("Edeceyiniz emeliyyatin nomresini daxil edin:")
print("1-toplama;\n2-cixma;\n3-vurma;\n4-bolme.")
x=(int)(input())
try:
    if x==1:
       print(a+b)
    elif x==2:
       print(a-b)
    elif x==3:
       print(a*b)
    elif x==4:
       print(a/b)
    else:
       print("bele bir emeliyyat yoxdur!") 
except ZeroDivisionError:
    print("Sifra bolmek olmaz!")       
print("Tesekkurler..")       