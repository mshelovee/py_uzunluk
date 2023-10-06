sifre=input("Şifreyi giriniz: ")
uzunluk=len(sifre)
if uzunluk<4 :
   print("BASİT")
elif uzunluk<6 :
     print("ORTA")
elif uzunluk<8 :
     print("ZOR")
elif uzunluk<12 :
     print("ÇOK ZOR")
else :
     print("KOLAYSA HACKLE BAKALIM :)")

