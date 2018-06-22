#-*- encoding: cp1254 -*-
#��renci NO: 14253607
#SADIK �ZG�

#test dosyas�ndan okuma ve split ile par�alama i�lemi
dosya = open("test1.txt", "r")
dizi = dosya.readlines()
dizi0 = dizi[0].split(',')
dizi1 = dizi[1]
dizi2 = dizi[2]
dizi3 = dizi[3].split(',')
dizi4 = dizi[4]
dizi5 = dizi[5]
dizi6 = dizi[6].split(',')
dizi7 = dizi[7].split(',')

#split edilenleri kullan�m amac�na g�re belirlemek
rastgele_sayisi = len(dizi0)
populasyon_boyut =int(dizi1)
secilen_beveyin_sayisi = int(dizi2)
mustasyon_olasiligi = len(dizi3)
iterasyon =int(dizi4)
canta_boyutu =int (dizi5)
eleman_agirlik = len(dizi6)
eleman_degerleri = len(dizi7)


#Ebeveyinler olu�turuluyor
aklinda_tut = 0
rastgele_sayaci = 0
ebeveyin_list = []                                     #olu�an ebeveyinlerimi list ler de tutmam gerek
mutasyon_list = []
for d in range(iterasyon):

     for i in range(populasyon_boyut):                 #istenilen pop�lasyon boyutu kadar ebeveyin olu�ucak
          sayac = 0                                    #�anta boyutunu a�mamas� i�in sayac kullan�ld�
          agirlik_sayaci = 0                           #elemanlar�n a��rl�klar�n�n indisini verir
          agirlik = 0                                  #�antan�n a��rl���n� hesap ediyor
          str = ''                                     #ebeveyinleri diziye atmak i�in
          deger = 0
          while sayac < eleman_agirlik:                #�anta boyutu kadar ebeveyinin boyutu olucak

               aklinda_tut = aklinda_tut + 1           #rastgele indisini belirleyebilmek i�in
               if rastgele_sayaci >= rastgele_sayisi:  #rastgele listesindeki de�er bitince tekrar etmesi i�in
                    rastgele_sayaci = 0
               if float(dizi0[rastgele_sayaci]) >= 0.5:

                    str=str+'1'
                    agirlik = agirlik + int(dizi6[agirlik_sayaci])
                    deger = deger + int(dizi7[agirlik_sayaci])
               else:
                    str=str+'0'

               if agirlik_sayaci <= eleman_agirlik:  #elemanlar�n a��rl�klar�nda geziyoruz
                    agirlik_sayaci = agirlik_sayaci + 1
               else:
                    agirlik_sayaci = 0

               sayac = sayac + 1
               rastgele_sayaci = rastgele_sayaci + 1

          # a��rl�k �anta boyutunu a�arsa s�f�r olcak.a�massa a��rl��� yaz�cak
          if (agirlik < canta_boyutu):
               ebeveyin_list.append((str,deger))
               str = ''
          else:
               ebeveyin_list.append((str,0))
               str = ''

          #rastgele degerin ka��nc� s�rada oldu�unu  g�terir. G�sterdi�i kullan�lacak olan sayidir.�r = 5 ise 5.indisdeki
          indisi = 0
          for j in range(aklinda_tut):
               if indisi >= rastgele_sayisi-1:
                    indisi = 0
               else:
                    indisi = indisi +1
     print("Generation:", d)
     print("Population=" ,ebeveyin_list)

     for u in range(int(secilen_beveyin_sayisi/2)):       #Secilecek ebeveyin say�s�(test1 i�in 15)
          print("Applying Crossover")
          ebeveyin_secme_degeri = 1 / populasyon_boyut  #burda populasyon boyutu 50 art�� miktar� 0.02 olucak
          topla = 0
          ebeveyin_sayac = -1                            #Hangi ebeveyini se�ice�imi g�steiri bana
          ebeveyin_sayac2 = -1

          for m in range(populasyon_boyut):             #s�radaki random say�ya g�re hangi ebeveyini se�ice�imi g�sterir 1.Se�im
               if float(topla) < float(dizi0[indisi]):
                    topla = topla + ebeveyin_secme_degeri
                    ebeveyin_sayac = ebeveyin_sayac + 1

          indisi = indisi + 1
          indisi = indisi%11

          #Ebeveyinlerin Se�ilmesi
          topla2 = 0
          for n in range(populasyon_boyut):            #s�radaki random say�ya g�re hangi ebeveyini se�ice�imi g�sterir 2.Se�im
               if float(topla2) < float(dizi0[indisi]):
                    topla2 = topla2 + ebeveyin_secme_degeri
                    ebeveyin_sayac2 = ebeveyin_sayac2 +1

          indisi = indisi + 1
          indisi = indisi%11

          #Se�ilen ebeveyinleri listeye al�nmas�
          secilen_ebeveyinler = []
          ebeveyin1 =''
          ebeveyin2 =''
          caprazlama_noktasi = int(float(dizi0[indisi])*eleman_agirlik)
          indisi = indisi + 1
          indisi = indisi%11

          ebeveyin1 = ebeveyin1 + ebeveyin_list[ebeveyin_sayac][0]
          ebeveyin2 = ebeveyin2 + ebeveyin_list[ebeveyin_sayac2][0]
          secilen_ebeveyinler.append((ebeveyin1))
          secilen_ebeveyinler.append((ebeveyin2))

          #secilen_ebeveyinler.append((ebeveyin_list[ebeveyin_sayac][0],ebeveyin_list[ebeveyin_sayac2][0]))
          print("Parents:",secilen_ebeveyinler , "at point:",caprazlama_noktasi)

          #�ocuklar�n olu�umu ve listeye al�nmas�
          olusan_cocuklar_listesi = []
          cocuk1 =''
          cocuk2 =''
          cocuk1 = cocuk1 + ebeveyin1[0:caprazlama_noktasi]
          cocuk1 = cocuk1 + ebeveyin2[caprazlama_noktasi:(canta_boyutu-1)]
          cocuk2 = cocuk2 + ebeveyin2[0:caprazlama_noktasi]
          cocuk2 = cocuk2 + ebeveyin1[caprazlama_noktasi:(canta_boyutu-1)]
          olusan_cocuklar_listesi.append((cocuk1))
          olusan_cocuklar_listesi.append((cocuk2))
          print("Offspring:",olusan_cocuklar_listesi)
          print("Applying mutation to:",(olusan_cocuklar_listesi[0],olusan_cocuklar_listesi[1]))

          mutasyonlu_cocuklar = []

          #Cocuk 1'i  mutasyona u�rat�caz
          for x in range(eleman_agirlik):
               cocuk1_listesi = list(cocuk1)

               if float(dizi0[indisi]) < 0.15:
                    if cocuk1[x] == "0":
                         cocuk1_listesi[x]='1'

                    else:
                         cocuk1_listesi[x] = '0'


          indisi = indisi +1
          indisi=indisi%11

          cocuk1=''.join(cocuk1_listesi)


          mutasyonlu_cocuklar.append(cocuk1) #cocuk 1 yeni mustasyon listesine al�nd�


          #Cocuk 2'i  mutasyona u�rat�caz
          for x in range(eleman_agirlik):
               cocuk2_listesi = list(cocuk2)

               if float(dizi0[indisi]) < mustasyon_olasiligi:
                    if cocuk2[x] == "0":
                         cocuk2_listesi[x]='1'

                    else:
                         cocuk2_listesi[x] = '0'


          indisi = indisi +1
          indisi=indisi%11

          cocuk2=''.join(cocuk2_listesi)

          mutasyonlu_cocuklar.append(cocuk2)  #cocuk 2 yeni mutasyon listesine al�nd�
          print("Mutated offspring:",mutasyonlu_cocuklar)
          cocuk2_deger = 0
          cocuk1_deger = 0
          cocuk1_agirlik=0
          cocuk2_agirlik=0
          for o in range(len(cocuk1)):

               if cocuk1[o] == "1":
                    cocuk1_deger = cocuk1_deger + int(dizi7[o])
                    cocuk1_agirlik = cocuk1_agirlik + int(dizi6[o])

               if cocuk2[o] == "1":
                    cocuk2_deger = cocuk2_deger + int(dizi7[o])
                    cocuk2_agirlik = cocuk2_agirlik + int(dizi6[o])

          if cocuk1_agirlik < canta_boyutu:
                mutasyon_list.append((cocuk1, cocuk1_deger))
          else:
               mutasyon_list.append((cocuk1,0))
          if cocuk2_agirlik < canta_boyutu:
               mutasyon_list.append((cocuk2, cocuk2_deger))
          else:
               mutasyon_list.append((cocuk2,0))

     #iki liste birle�tirldi ve sonra degerlere g�re yeni liste elde edildi
     yeni_list = []
     yeni_list = mutasyon_list + ebeveyin_list
     yeni_ebeveyin_list = []
     for v in range(len(yeni_list)):
          if int(yeni_list[v][1]) > 0:
               yeni_ebeveyin_list.append(yeni_list[v])

     for w in range(len(ebeveyin_list)):
          if int(yeni_list[w][1]) == 0:
               yeni_ebeveyin_list.append(yeni_list[w])

     ebeveyin_list = yeni_ebeveyin_list


final_list = []
for h in range(populasyon_boyut):
     final_list.append(ebeveyin_list[h])

#B�TT�

print("Final Population: ",final_list)

