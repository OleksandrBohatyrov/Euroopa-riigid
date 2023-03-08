from module import *

x={}
while True:
    menu=int(input("... "))
    if menu==0:
        pass
    elif menu==1:
        x=openv("riigid_pealinnad.txt")
        x=print(openv)
    elif menu==2:
        x=lisa("riigid_pealinnad.txt") 
        x=print(lisa)
    elif menu==3:
        x=näita("riigid_pealinnad.txt")
        x=print(näita)
    elif menu==4:
        x=game("riigid_pealinnad.txt")
        x=print(game)
    elif menu==5:
        x=paranda("riigid_pealinnad.txt")
        x=print(paranda)