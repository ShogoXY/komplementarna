# print ("Program sprawdzający dane w dwóch listach")
#coding=utf8
from glowna import list_1, list_2, list_3, list_4
import re

for i in range(len(list_1)):
    list_1[i] = list_1[i].lower()

for i in range(len(list_2)):
    list_2[i] = list_2[i].lower()

for i in range(len(list_3)):
    list_3[i] = list_3[i].lower()
for i in range(len(list_4)):
    list_4[i] = list_4[i].lower()




def wybrana_lista() :
    interupt_glowny="coś czego nie ma"
    # nr_listy=str(input("podaj cos z listy: "))

    while interupt_glowny != "":
        try:
            print("podaj glowny")
            interupt_glowny=str(input().lower())
            lista_nowa=list((list_1,list_3))
            lista_nowa2=list((list_2,list_4))
            i=0
            l=0

            if interupt_glowny != "" :
                while l == 0:
                
                    szukaj=lista_nowa[i]
                    szukaj2=lista_nowa2[i]
                    r = re.compile(".*"+interupt_glowny)
            
                    new = list(filter(r.match, szukaj)) # Read Note belo
                    l = len(new)
                    i=i+1
                    
                
                print("\n")
                # print(szukaj)
                newlist = list(filter(r.match, szukaj)) # Read Note below
                print(*newlist,sep='\n')
                print ("\n")
                if newlist:  
                    interupt="coś czego nie ma"

                    while interupt != "":
                        print("podaj komplementarna")
                        interupt=input().lower()
                        r = re.compile(".*"+interupt)
                        if interupt != "":
                            print("\n")
                            newlist2 = list(filter(r.match, szukaj2)) # Read Note below
                            print(*newlist2,sep='\n')
                            print ("\n")
                            if not newlist2:
                                print("Brak,podaj poprawną warotść")
        except:
            print("Brak, podaj podaj poprawną wartość")
    print("KONIEC")


wybrana_lista()