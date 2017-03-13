a = 65;
b = 15;
c = 4;
d = 1;

e = a + b
f = c / d
g = e * f    

nama = "Nama : Rahmatul Ridha"
npm = "NPM : 1144124"
kelas = "Kelas : D4 TI 3A"

import time
start_time = time.time()
loop = 1
print ("Operasi Aritmatika Lebih dari 1 Operator dan Delta t")
print (nama)
print (npm)
print (kelas)
print ()
print ("Input - (Enam Lima + Lima Belas) x (Empat / Satu)")
print ("(", a, "+", b,")", "x", "(", c, "/", d,")")
print ("Hasil : ", g)
totalTime = format((time.time() - start_time), '.5f')
print("Delta t : ", totalTime)
print ("Output - Hasil : ", g, " | Delta t : ", totalTime)