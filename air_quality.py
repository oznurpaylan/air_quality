


so=float(input("so2 degerini girin= "))
no=float(input("no2 degerini girin= "))
co=float(input("co degerini girin= "))
o=float(input("o degerini girin= "))
pm=float(input("pm10 degerini girin= "))

if so>=0 and so<=100 and  no>=0 and no<=100 and co>=0 and co<=5500 and o>=0 and o<=120 and pm>=0 and pm<=50:
    print("İyi")
    print("Hava Kalitesi İndexi 0-50 arasinda")
elif so>=101 and so<=250 and  no>=101 and no<=200 and co>=5501 and co<=10000 and o>=121 and o<=160 and pm>=51 and pm<=100:
    print("Orta")
    print("Hava Kalitesi İndexi 51-100 arasinda")
elif so>=251 and so<=500 and  no>=201 and no<=500 and co>=10001 and co<=16000 and o>=161 and o<=180 and pm>=101 and pm<=260:
    print("Hassas")
    print("Hava Kalitesi İndexi 101-150 arasinda")
elif so>=501 and so<=850 and  no>=501 and no<=1000 and co>=16001 and co<=24000 and o>=181 and o<=240 and pm>=261 and pm<=400:
    print("Sagliksiz")
    print("Hava Kalitesi İndexi 151-200 arasinda")
elif so>=851 and so<=1100 and  no>=1001 and no<=2000 and co>=24001 and co<=32000 and o>=241 and o<=700 and pm>=401 and pm<=520:
    print("Kötü")
    print("Hava Kalitesi İndexi 201-300 arasinda")
else: 
    print("Tehlikeli")
    print("Hava Kalitesi İndexi 301-500 arasinda")


