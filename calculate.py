def topla(x , y):
    return(x + y)

def cikar(x , y):
    return(x - y)

def carp(x , y):
    return(x * y)

def bol(x , y):
    return(x / y)

print("Islemler:"+"\nToplama = 1\nCikarma = 2\nCarpma = 3\nBolme = 4")

while True:

    islem = input("Yapmak istediginiz islemi seciniz:")

    if islem in("1","2","3","4"):
    
        sayi_1 = float(input("Birinci sayiyi giriniz:"))
    
        sayi_2 = float(input("Ikinci sayiyi giriniz:"))
    
        if islem == "1":
        
            print(sayi_1, "+", sayi_2, "=" ,topla(sayi_1,sayi_2))
        
        elif islem == "2":
        
            print(sayi_1, "-", sayi_2, "=" ,cikar(sayi_1,sayi_2))
        
        elif islem == "3":
        
            print(sayi_1, "*", sayi_2, "=" ,carp(sayi_1,sayi_2))
        
        elif islem == "4":
        
            print(sayi_1, "/", sayi_2, "=" ,bol(sayi_1,sayi_2)) 
        
        break
        
    else:
        print("Gecersiz girdi!")
    