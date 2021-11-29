import time
import random
from multiprocessing import pool
from playsound import playsound
from threading import Thread

i = -1
l = 0

count = 0




class loops:
    def loop(self):
        print("   ", end="")

    def A(self):
        global i
        global l
        global i

        for j in range(i, 5):
            for k in range(4, i, -1):
                print(" ", end="")
            print("*", end="")
            if i != 0:
                l = 1
            for q in range(0, l):
                if (i == 3):
                    print(" *" * 3, end="")
                else:
                    print(" " * (i + (i - 1)), end="*")

            for k in range(4, i, -1):
                print(" ", end="")

            x.loop()
            return

    def B(self):
        global i

        for j in range(i, 6):
            print("*", end="")
            if (i == 0 or i == 2 or i == 4):
                print(" *" * 3, end=" ")
            else:
                print(" " * 6, end="*")

            x.loop()
            return

    def C(self):
        global i
        for i in range(i, 5):
            if (i == 0 or i == 4):
                print(" " * 2, end=" *" * 3)

            elif (i == 1 or i == 3):
                print(" " * 1, end="*")
                print(" " * 5, end=" ")
            else:
                print("*", end=" " *7)
            x.loop()
            return

    def D(self):
        global i
        for i in range(i, 5):
            print("*", end=" ")
            if (i == 0 or i == 4):
                print("* " * 2, end=" " * 1)
            elif (i == 1 or i == 3):
                print(" " * 4, end="*")
            else:
                print(" " * 3, end=" *")
            x.loop()
            return

    def E(self):
        global i
        for i in range(i, 5):
            if (i == 0 or i == 2 or i == 4):
                print("* " * 3, end="*")
            else:
                print("* ", end=" " * 5)

            x.loop()
            return

    def F(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print("* " * 3, end="*")
            elif (i == 2):
                print("* " * 3, end=" ")
            else:
                print("* ", end=" " * 5)
            x.loop()
            return

    def G(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print(" " * 2, end=" *" * 3)
                print(" ", end="")
            elif (i == 4):
                print(" " * 2, end=" * " * 2)
                print(" ", end="")
            elif (i == 1):
                print(" " * 1, end="*")
                print(" " * 7, end="")

            elif (i == 3):
                print(" " * 1, end="*")
                print(" " * 5, end=" *")

            else:
                print("*", end=" " * 2)
                print(" *" * 3, end="")
            x.loop()
            return

    def H(self):
        global i
        for i in range(i, 5):
            if (i == 2):
                print("* " * 3, end="*")
            else:
                print("*", end=" " * 5)
                print("*", end="")
            x.loop()
            return

    def I(self):
        global i
        for i in range(i, 5):
            if (i == 0 or i == 4):
                print("* " * 3, end="*")
            else:
                print(" " * 3, end="*")
                print(" " * 3, end="")
            x.loop()
            return

    def J(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print("* " * 3, end="*")
            elif (i == 3 or i == 2):
                print("* ", end=" *")
                print(" " * 3, end="")
            elif (i == 4):
                print("  ", end="*")
                print("  " * 2, end="")
            else:
                print(" " * 3, end="*")
                print(" " * 3, end="")
            x.loop()
            return

    def K(self):
        global i
        for i in range(i, 5):
            if i == 0 or i == 4:
                print("*", end="  " * 3)
                print("*", end="")
            elif i == 1 or i == 3:
                print("*", end="  " * 2)
                print("* ", end=" ")
            else:
                print("* ", end=" *")
                print("  ", end="  ")
            x.loop()
            return
    def L(self):
        global i
        for i in range(i,5):
            if(i==4):
                print("* "*3,end="*")
            else:
                print("* ",end=" "*5)
            x.loop()
            return
    def M(self):
        global i
        for i in range(i,5):
            print("* ",end="")
            if(i==1):
                print("*  ",end=" * ")
            elif(i==2):
                print(" "*2,end="*   ")
            else:
                print("  "*3,end="")
            print("*",end="")
            x.loop()
            return
    def N(self):
        global i
        for i in range(i,5):
            print("*",end="")
            if(i==0 ):
                print("  "*3,end="")
            else:
                print(" "*i,end="*")
                print(" "*(5-i),end="")
            print("*",end="")
            x.loop()
            return
    def O(self):
        global i
        for i in range(i,5):
            if(i==0 or i==4):
                print(" "*4,end="*")
                print(" "*3,end=" ")
            elif(i==2):
                print("*",end=" "*7)
                print("*",end="")
            else:
                print(" ",end="*")
                print("     ",end="* ")
            x.loop()
            return
    def P(self):
        global i
        for i in range(i,5):
            print("*",end="")
            if(i==0 or i==2):
                print(" *"*3,end=" ")
            elif(i==1):
                print(" "*6,end="*")
            else:
                print(" "*7,end="")
            x.loop()
            return
    def Q(self):
        global i
        for i in range(i,5):
            if(i==0):
                print(" "*4,end="*")
                print(" "*3,end=" ")
            elif(i==4):
                print(" "*4,end="*")
                print(" "*3,end="*")
            elif(i==2):
                print("*",end=" "*7)
                print("*",end="")
            elif(i==3):
                print(" ",end="*")
                print(" "*3,end="* * ")
            else:
                print(" ",end="*")
                print("     ",end="* ")
            x.loop()
            return
    def R(self):
        global i
        for i in range(i,5):
            print("*",end="")
            if(i==0 or i==2):
                print(" *"*3,end=" ")
            elif(i==1):
                print(" "*6,end="*")
            else:
                print(" "*i,end=" *")
                print(" ",end=" "*(4-i))
            x.loop()
            return

    def S(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print(" " * 2, end="* " * 3)
                print("", end="")
            elif (i == 4):
                print("  ", end="* " * 3)
                print("", end="")
            elif (i == 1):
                print("*", end=" " * 7)

            elif (i == 2):
                print("   ", end="*")
                print(" " * 4, end="")
            else:
                print("*", end=" " * 6)
                print("*", end="")
            x.loop()
            return

    def T(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print("* " * 3, end="*")
            else:
                print(" " * 2, end=" *")
                print(" " * 2, end=" ")
            x.loop()
            return

    def U(self):
        global i
        for i in range(i, 5):
            if (i == 4):
                print(" " * 2, end="* " * 2)
                print(" " * 2, end="")
            elif (i == 3):
                print(" ", end="*")
                print(" " * 4, end="*")
                print(" ", end="")
            else:
                print("* ", end=" " * 5)
                print("*", end="")
            x.loop()
            return

    def V(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print("*", end=" " * 7)
                print("*", end="")
            elif (i == 1):
                print(" *", end=" " * 5)
                print("*", end=" ")
            elif (i == 2):
                print("  *", end=" " * 3)
                print("*", end="  ")
            elif (i == 3):
                print("   *", end=" ")
                print("*", end="   ")
            else:
                print(" " * 4, end="*")
                print(" " * 4, end="")
            x.loop()
            return

    def W(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print("*", end=" " * 11)
                print("*", end="")
            elif i == 1:
                print(" *", end=" " * 9)
                print("", end="* ")
            elif (i == 2):
                print("  * ", end="      *")
                print(" ", end=" ")
            elif (i == 3):
                print(" " * 3, end="*")
                print("  *  * ", end=" " * 2)

            else:
                print(" " * 3, end=" *")
                print("   *", end=" " * 4)
            x.loop()
            return

    def X(self):
        global i
        for i in range(i, 5):
            if (i == 0 or i == 4):
                print("*", end=" " * 5)
                print("*", end="")
            elif (i == 1 or i == 3):
                print(" *", end=" " * 3)
                print("* ", end="")
            else:
                print(" " * 3, end="*")
                print(" " * 3, end="")
            x.loop()
            return

    def Y(self):
        global i
        for i in range(i, 5):
            if (i == 0):
                print("*", end=" " * 5)
                print("*", end="")
            elif (i == 1):
                print(" *", end=" " * 3)
                print("* ", end="")
            else:
                print(" " * 3, end="*")
                print(" " * 3, end="")
            x.loop()
            return

    def Z(self):
        global i
        for i in range(i, 5):
            if (i == 0 or i == 4):
                print("* " * 3, end="*")
            elif (i == 1):
                print(" " * 5, end="*")
                print(" ", end="")
            elif (i == 2):
                print(" " * 3, end="*")
                print(" " * 2, end=" ")
            else:
                print(" " * 1, end="*")
                print(" " * 3, end="  ")
            x.loop()
            return


print()

def play():
    soun = input("ENTER SOUND")
    time.sleep(1.8)
    print("\n"*30)
# CHANGE DIRECTORY HERE ................................................................
    playsound("C:\\Users\\chetan\\Desktop\\language\\playsound\\" + soun + ".mp3")
# CHANGE DIRECTORY HERE.................................................................
    time.sleep(1.1)




x = loops()
# DRIVER CODE
n = input("ENTER YOUR TEXT")
print("type any song name from here ...")
lis=["birth",'rider','standard','teri mitti me','chitrakaar']
print(lis)

#WE CAN ADD birthday and rider SONG HERE
thread=Thread(target=play)


thread.start()
time.sleep(7)




k = len(n)
aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
s=0.5
list=[30,31,32,33,34,35,36,37]
color=0
for o in range(5):
    i = i + 1
    for f in range(k):

        if (n[f] == "A" or n[f] == "a"):
            if(aa==0):
                aa=random.choice(list)
                aa=aa+1
            print("\033[1;{}m".format(aa),end="")
            time.sleep(s)
            x.A()
        elif (n[f] == "B" or n[f] == "b"):
            if(bb==0):
                bb=random.choice(list)
                bb=bb+1
            print("\033[1;{}m".format(bb),end="")
            time.sleep(s)
            x.B()
        elif (n[f] == "C" or n[f] == "c"):
            if(cc==0):
                cc=random.choice(list)
                cc=cc+1
            print("\033[1;{}m".format(cc),end="")

            time.sleep(s)
            x.C()
        elif (n[f] == "D" or n[f] == "d"):
            if(dd==0):
                dd=random.choice(list)
                dd=dd+1
            print("\033[1;{}m".format(dd),end="")

            time.sleep(s)
            x.D()
        elif (n[f] == "E" or n[f] == "e"):
            if(ee==0):
                ee=random.choice(list)
                ee=ee+1
            print("\033[1;{}m".format(ee),end="")

            time.sleep(s)
            x.E()
        elif (n[f] == "F" or n[f] == "f"):
            if(ff==0):
                ff=random.choice(list)
                ff=ff+1
            print("\033[1;{}m".format(ff),end="")

            time.sleep(s)
            x.F()
        elif (n[f] == "G" or n[f] == "g"):
            if(gg==0):
                gg=random.choice(list)
                gg=gg+1
            print("\033[1;{}m".format(gg),end="")

            time.sleep(s)
            x.G()
        elif (n[f] == "H" or n[f] == "h"):
            if(hh==0):
                hh=random.choice(list)
                hh=hh+1
            print("\033[1;{}m".format(hh),end="")

            time.sleep(s)
            x.H()
        elif (n[f] == "I" or n[f] == "i"):
            if(ii==0):
                ii=random.choice(list)
                ii=ii+1
            print("\033[1;{}m".format(ii),end="")

            time.sleep(s)
            x.I()
        elif (n[f] == "J" or n[f] == "j"):
            if(jj==0):
                jj=random.choice(list)
                jj=jj+1
            print("\033[1;{}m".format(jj),end="")

            time.sleep(s)
            x.J()
        elif (n[f] == "K" or  n[f] == "k"):
            if(kk==0):
                kk=random.choice(list)
                kk=kk+1
            print("\033[1;{}m".format(kk),end="")

            time.sleep(s)
            x.K()
        elif (n[f] == "L" or  n[f] == "l"):
            if(ll==0):
                ll=random.choice(list)
                ll=ll+1
            print("\033[1;{}m".format(ll),end="")

            time.sleep(s)
            x.L()
        elif (n[f] == "m" or  n[f] == "M"):
            if(mm==0):
                mm=random.choice(list)
                mm=mm+1
            print("\033[1;{}m".format(mm),end="")

            time.sleep(s)
            x.M()
        elif (n[f] == "N" or  n[f] == "n"):
            if(nn==0):
                nn=random.choice(list)
                nn=nn+1
            print("\033[1;{}m".format(nn),end="")

            time.sleep(s)
            x.N()
        elif (n[f] == "O" or  n[f] == "o"):
            if(oo==0):
                oo=random.choice(list)
                oo=oo+1
            print("\033[1;{}m".format(oo),end="")

            time.sleep(s)
            x.O()
        elif (n[f] == "P" or  n[f] == "p"):
            if(pp==0):
                pp=random.choice(list)
                pp=pp+1
            print("\033[1;{}m".format(pp),end="")

            time.sleep(s)
            x.P()
        elif (n[f] == "q" or  n[f] == "Q"):
            if(qq==0):
                qq=random.choice(list)
                qq=qq+1
            print("\033[1;{}m".format(qq),end="")

            time.sleep(s)
            x.Q()
        elif (n[f] == "R" or  n[f] == "r"):
            if(rr==0):
                rr=random.choice(list)
                rr=rr+1
            print("\033[1;{}m".format(rr),end="")

            time.sleep(s)
            x.R()
        elif (n[f] == "S" or n[f] == "s"):
            if(ss==0):
                ss=random.choice(list)
                ss=ss+1
            print("\033[1;{}m".format(ss),end="")

            time.sleep(s)
            x.S()
        elif (n[f] == "T" or n[f] == "t"):
            if(tt==0):
                tt=random.choice(list)
                tt=tt+1
            print("\033[1;{}m".format(tt),end="")

            time.sleep(s)
            x.T()
        elif (n[f] == "U" or n[f] == "u"):
            if(uu==0):
                uu=random.choice(list)
                uu=uu+1
            print("\033[1;{}m".format(uu),end="")

            time.sleep(s)
            x.U()
        elif (n[f] == "V" or n[f] == "v"):
            if(vv==0):
                vv=random.choice(list)
                vv=vv+1
            print("\033[1;{}m".format(vv),end="")

            time.sleep(s)
            x.V()
        elif (n[f] == "W" or n[f] == "w"):
            if(ww==0):
                ww=random.choice(list)
                ww=ww+1
            print("\033[1;{}m".format(ww),end="")

            time.sleep(s)
            x.W()
        elif (n[f] == "X" or n[f] == "x"):
            if(xx==0):
                xx=random.choice(list)
                xx=xx+1
            print("\033[1;{}m".format(xx),end="")

            time.sleep(s)
            x.X()
        elif (n[f] == "Y" or n[f] == "y"):
            if(yy==0):
                yy=random.choice(list)
                yy=yy+1
            print("\033[1;{}m".format(yy),end="")

            time.sleep(s)
            x.Y()
        elif (n[f] == "Z" or n[f] == "z"):
            if(zz==0):
                zz=random.choice(list)
                zz=zz+1
            print("\033[1;{}m".format(zz),end="")

            time.sleep(s)
            x.Z()
        elif(n[f]==" "):
            x.loop()
            x.loop()

    print()
time.sleep(6)
print("\n"*8)
print('THANK YOU         ', end='', flush=True)
for x in range(8):
    for frame in r'-\|/-\|/':

        print('\b', frame, sep='', end='', flush=True)
        time.sleep(0.2)

print('\b ')
thread.join()

