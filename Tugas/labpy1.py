#!/usr/bin/python3
a = input ("Masukan Nilai A :")
b = input ("Masukan Nilai B :")
c = input ("Masukan Nilai C :")

if a > b:
    if a > c:
     print ("Nilai Terbesar :",a)
elif b > a:
    if b > c:
     print ( "Nilai Terbesar :",b)
     
else:
    print ("Nilai Terbesar :",c)

