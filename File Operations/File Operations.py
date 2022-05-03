## Dosya a�mak ve olu�turmak i�in open() fonksiyonu kullan�l�r.
## Kullan�m� : open(dosya_adi,dosya_eri�me_modu)
## dosya_eri�me_modu => dosyay� hangi ama�la a�t���m�z� belirtir.








# 'w' : (Write) Yazma Modu.

#           ** Dosyay� konumda olu�turur.
#           ** Dosya i�eri�ini Siler ve Yeniden Ekler.

#file = open("PythonNewFile.txt","w")
#file.close()
#file = open("C:/Users/Yakup/Desktop/PythonNewFile.txt","w")
#file = open("PythonNewFile.txt","w",encoding = "utf-8")
#file.write("Yakup Acis")
#file.close()








# 'a' : (Append) Ekleme. 

#                       **Dosya Konumda Yoksa Olu�turur. 
#                       **Daha �nce Bir Verinin �zerine Ekleme Yapar.
#file = open("PythonNewFile.txt","a",encoding = "utf-8")
#file.write("Yakup Acis\n")
#file.close()










# 'x' : (Create) Olu�turma. 

#                           **Dosya Zaten Varsa Hata Verir.
#file = open("PythonNewFile2.txt","x",encoding='utf-8')










## 'r' : (Read) Okuma. Varsay�lan. Dosya Konumda Yoksa Hata Verir.

#try:
#    file = open("PythonNewFile.txt","r")
#    print(file)
#except Exception as x:
#    print(x)
##finally:
##    print("dosya basariyla kapandi.")
##    file.close()



#file = open("PythonNewFile.txt","r",encoding = "utf-8")
#for i in file:
#    print(i, end="")
#file.close()




#file = open("PythonNewFile.txt","r",encoding = "utf-8")
#content1 = file.read()
#print("icerik 1: ")
#print(content1)
#content2 = file.read()
#print("icerik 2: ")
#print(content2)
#file.close()



#file = open("PythonNewFile.txt","r",encoding = "utf-8")
#bes = file.read(5)
#dort = file.read(4)
#onbes = file.read(5)
#print(bes)
#print(dort)
#print(onbes)
#file.close()







#file = open("PythonNewFile.txt","r",encoding = "utf-8")

##readline bir sat�r okur
#print(file.readline(),end = "")
#print(file.readline(),end = "")
#print(file.readline(),end = "")




#file = open("PythonNewFile.txt","r",encoding = "utf-8")
#liste = file.readlines()
#print(liste[0],end="")
#print(liste[1],end="")
#print(liste[2])
#file.close()






#with open("PythonNewFile.txt","r",encoding="utf-8") as file:
#    print(file.tell()) ## TEEL cursor'un nerede oldu�unu s�yler.

#    print(file.read()) 

#    print(file.seek(0)) ## SEEK cursor'u 0 konumuna g�nderdik.

#    print(file.tell())

#    print(file.read())

#    print(file.tell())
#    ##with ile birlikte otomatik close �al���r.









#with open("PythonNewFile.txt","r+", encoding = "utf-8") as file:
#    file.seek(26)
#    file.write("deneme")
#with open("PythonNewFile.txt","r+", encoding = "utf-8") as file: ## r+ hem okuma hem yazma! utf-8 t�rk�e karakterler i�in.
#    print(file.read())




## Sayfa Sonunda G�ncelleme
#with open("PythonNewFile.txt","a", encoding="utf-8") as file:
#     file.write("\nAbdulkadir Acis")



## Sayfa Basinda Guncelleme
#with open("PythonNewFile.txt","r+", encoding="utf-8") as file:
#    content = file.read()
#    content = "Efe Turan\n" +  content
#    file.seek(0)
#    file.write(content)
#    print(content) 



###Sayfa Ortas�nda G�ncelleme
#with open("PythonNewFile.txt","r+", encoding="utf-8") as file:
#    list = file.readlines()
#    list.insert(6,"yeni\n") 
#    file.seek(0)
#    file.writelines(list)

#with open("PythonNewFile.txt","r",encoding="utf-8") as file:
# #   print(file.read())