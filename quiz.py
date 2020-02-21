import random, os, time, datetime
from datetime import timedelta
waktuawal = time.time()
soal = 2
a = 0
score = 0
benar = 0
salah = 0
scoreadd = 1
for i in range(int(soal)):
	while (int(soal)) < 1:
	 waktuakhir = time.time()
	 lamawaktu = waktuakhir - waktuawal
	 print 'lama waktu anda mengerjakan ini ' + (str(lamawaktu)) + ' detik'
	 print '\x1b[1;36mSoal Sudah Selesai\n'
	 print '\x1b[1;33mJumlah Score anda = ',score
	 print '\x1b[1;32mJumlah Benar anda = ',benar
	 print '\x1b[1;35mJumlah Salah anda = ',salah
	 print '\x1b[1;33mJumlah Soal = ',soal
	 os.sys.exit()
       	while (int(soal)) > 0:
         a += 1
	 soal -= 1
	 os.system("clear")
	 ops = [" + ", " - "]
	 rand = random.randint(60,90)
	 rand2 = random.randint(30,60)
	 operation = random.choice(ops)
	 maths = eval(str(rand) + operation + str(rand2))
	 print '\x1b[1;32mScore Saat Ini = ' + (str(score))
	 print 'Soal Ke : ' + (str(a))
	 print '\x1b[1;33mHasil Dari ' + (str(rand)) + operation + (str(rand2))

	 ans = raw_input("\x1b[1;36mJawab = ")

	 if ans == maths:
	      scoreadd += 1
	      os.system("clear")
	      score += scoreadd
	      benar += 1
	      print '\x1b[1;32mJawaban anda benar'
	      time.sleep(2)
	 else:
	     scoreadd = 0
	     score -= 1
	     salah += 1
	     os.system("clear")
	     print 'jawaban anda salah \njawaban yang sebenarnya adalah : ' + (str(maths))
	     print '\x1b[1;35mScore Dikurangi 1'
	     time.sleep(2)
