from random import *
sonastik = {}
def openv(file1:str):
    file=open(file1,"r", encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-') #соединяет 2 строки в одну
        sonastik[k.strip()]=v.strip()
    print(sonastik)
    return sonastik

def lisa(file1:str):
    file=open(file1,"r", encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        sonastik[k.strip()]=v.strip()
    riik=input("Lisa riik: ")
    pealinn=input("Tema pealinn: ")
    sonastik.update({riik:pealinn})
    file.close()
    print(sonastik)
    return sonastik

def näita(fail:str):   #poisk
    file=open(fail,'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sonastik[k.strip()] = v.strip() #соединяет 2 строки в одну
    file.close()
    Riigid = list(sonastik.keys())
    Pealinnad = list(sonastik.values()) #возварщение значения
    peremennaya=input("Otsime riigi või pealinna: ")
    while peremennaya not in ["riik","pealinn"]:
        peremennaya=input("riik või pealinn: ")
    if peremennaya == "riik":
        OtsimeR=input("Kirjuta riigi nimi: ")
        while OtsimeR not in Riigid:
            OtsimeR=input("Kirjuta riigi õigesti: ")
        num1=Riigid.index(OtsimeR) #поиск в словаре
        if OtsimeR == Riigid[num1]:
            print(OtsimeR,Pealinnad[num1])
    else:
        OtsimeP=input("Kirjuta pealinna nimi: ")
        while OtsimeP not in Pealinnad:
            OtsimeP=input("Kirjuta riigi õigesti: ")
        num1=Pealinnad.index(OtsimeP) #поиск в словаре
        if OtsimeP == Pealinnad[num1]:
            print(Riigid[num1],OtsimeP)
    return sonastik

def game(fail:str): #game
    a=[]
    võit=kaotus=0
    test=[]
    file=open(fail,'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sonastik[k.strip()] = v.strip()
    file.close()
    Riigid = list(sonastik.keys())
    Pealinnad = list(sonastik.values()) #возварщение значения
    x=int(input("palju korda mängime: "))
    for i in range (x):
        num=randint(0,(len(Riigid)-1))
        while num in a:
            num=randint(0,(len(Riigid)-1))
        valik=input("Kas võtame riigi või pealinna? (riik või pealinn) ").lower()
        while valik not in ["riik","pealinn"]:
            valik=input("Kirjuta riik või pealinn: ")
        if valik=="riik":
            rana=Riigid[num]
            tematähendus=input(f"Mis on riigi {rana} pealinn: ")
            if tematähendus==Pealinnad[num]:
                test.append(f"{i+1} {valik} mäng - võit")
                print("Võit")
                võit+=1
            else:
                test.append(f"{i+1}, {valik} mäng - kaotus") 
                print("Kaotus")
                kaotus+=1
        else:
            rana=Pealinnad[num]
            tematähendus=input(f"Mis on riigi {rana} pealinn: ") 
            if tematähendus==Pealinnad[num]:
                test.append(f"{i+1} {valik} mäng - võit")
                print("Võit")
                võit+=1
            else:
                test.append(f"{i+1}, {valik} mäng - kaotus") 
                print("Kaotus")
                kaotus+=1       
        a.append(num)
    return sonastik

def paranda(fail: str): #izmenit
    file=open(fail,'r',encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')
        sonastik[k.strip()] = v.strip() #соединяет 2 строки в одну
    while True:
        riik_või_pealinn = input('Kas soovite muuta riigi nime või pealinna nime? riik või pealinn (r/p): ').lower()
        if riik_või_pealinn not in ['r', 'p']:
            print('Palun sisestage "r" või "p".')
        else:
            break   
    if riik_või_pealinn == 'r':
        print(sonastik)
        Rparanda = input('Millist riigi soovite parandada? ')
        while Rparanda not in sonastik:
            Rparanda = input('Kirjutage õige riigi nimi: ')
        Rparandatud = input('Kirjutage parandatud riigi nimi: ')
        while not Rparandatud.isalpha(): #проверка
            Rparandatud = input('Kirjutage riigi nimi: ')
        sonastik[Rparandatud] = sonastik.pop(Rparanda)
    else:
        print(sonastik)
        Pparanda = input('Millist pealinna soovite parandada? ')
        while Pparanda not in sonastik.values():
            Pparanda = input('Kirjutage õige pealinna nimi: ')
        Pparandatud = input('Kirjutage parandatud pealinna nimi: ')
        while not Pparandatud.isalpha(): #проверка
            Pparandatud = input('Kirjutage pealinna nimi: ')
        for key, value in sonastik.items():
            if value == Pparanda:
                sonastik[key] = Pparandatud
                break   
    with open(fail, 'w', encoding='utf-8-sig') as f:
        for key, value in sonastik.items():
            f.write(f'{key}-{value}\n')
        print(sonastik)
    return sonastik