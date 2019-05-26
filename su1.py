import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
import csv
class par:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x
def udaljenost(a,b):
                    sol=0
                    for i in range(0,27):
                        sol=sol+((K[b][i]-K[a][i])**2)
                        #print(K[b][i])
                        #print(K[a][i])
                        #print(sol)
                    return sol**(1/float(2))


DATA_LOCATION = "data/main_players.csv"
FIRST_ATTRIBUTE = "LS"
SECOND_ATTRIBUTE = "ST"
treci="RS"
cetvrti="LW"
peti="LF"
sest="CF"
sedam="RF"
osam="RW"
devet="LAM"
deset="CAM"
jed="RAM"
dva="LM"
tri="CM"
cet="RCM"
pet="RM"
ses="LWB"
sed="LDM"
osa="CDM"
dev="RDM"
dvades="RWB"
djed="LB"
ddva="LCB"
dtri="CB"
dcet="RCB"
dpet="RB"
dses="LCM"
dsed="Position"
dosa="Name"
datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE, treci,cetvrti,peti,peti,sest,sedam,osam,devet,deset,jed,dva,tri,cet,pet,ses,sed,osa,dev,dvades,djed,ddva,dtri,dcet,dpet,dses,dsed,dosa]]

K = data1.values
#plt.scatter(K[:,0], K[:,1], K[:,2],color = 'g')
#plt.show()
min=9999999
sol1=0
k=0
sol3=0
postotak=0;
niz=[]
x=0
y=0
z=0
x1=0
y1=0
z1=0
#print(udaljenost(0,1))
#print(K[broj][28])
for i in range(0,12700):
    if(K[i][27] == "GK"): K[i][27]="G"
    if(K[i][27] == "CB") or (K[i][27] == "LCB") or (K[i][27] == "RCB") or (K[i][27] == "LB") or (K[i][27] == "RB") or (K[i][27] == "LWB") or (K[i][27] == "RWB") : K[i][27]="B"
    if(K[i][27] == "CM") or (K[i][27] == "LDM") or (K[i][27] == "LAM") or (K[i][27] == "RDM") or (K[i][27] == "RAM") or (K[i][27]=="CDM") or(K[i][27]=="CAM") or(K[i][27]=="LM")or(K[i][27]=="RM") or (K[i][27] == "RCM") or (K[i][27] == "LCM") : K[i][27]="V"
    if(K[i][27] == "ST") or (K[i][27] == "CF") or (K[i][27] == "LW") or (K[i][27] == "RW") or (K[i][27] == "LF") or (K[i][27] == "RF") or (K[i][27] == "LS") or (K[i][27] == "RS") : K[i][27]="N"

#print("Prije for petlje")
#print(x)
#print(y) 
#print(z)   
for broj in range(0,12700):
        polje = [];         
        for i in range(0,12700):
            sol1=udaljenost(i,broj)
            if(sol1==0): sol1=999999
            if(K[i][27]!="G" and K[i][27]!="B" and K[i][27]!="V" and K[i][27]!="N"): print(K[i][27]);
            polje.append(par(sol1,i))    
            polje.sort()
        #print(polje[0].x, polje[0].y)
        print(K[broj][27])    
        #print(K[polje[0].y])
        a=0
        b=0
        c=0
        d=0
        e=0
        for i in range(1,10):            
                    if(K[polje[i].y][27]=="N"): a=a+1    
                    if(K[polje[i].y][27]=="V"): b=b+1    
                    if(K[polje[i].y][27]=="B"): c=c+1  
                    if(K[polje[i].y][27]=="G"): d=d+1
                      
                                  
        print(a,b,c)
        d=0        
        if(d>0): print("G i gotovo")
        if(a>b and a>c): 
                                #print("N")
                                if(K[broj][27]=="N"):
                                                      sol3=sol3+1
                                                      postotak=sol3/(broj+1)
                                                      print("{:.6f}".format(postotak))      
                                                      x=x+1
                                                              
        if(b>c and b>a): 
                                #print("V")
                                if(K[broj][27]=="V"):
                                                      sol3=sol3+1
                                                      postotak=sol3/(broj+1)
                                                      print("{:.6f}".format(postotak))
                                                      y=y+1    
        if(c>a and c>b): 
                                #print("B")
                                if(K[broj][27]=="B"):
                                                      sol3=sol3+1
                                                      postotak=sol3/(broj+1)  
                                                      print("{:.6f}".format(postotak))
                                                      z=z+1
        print("Trenutačno obradio broj:", broj, ".")
        niz.append(postotak)
        if(K[broj][27]=="N"): x1=x1+1;
        if(K[broj][27]=="V"): y1=y1+1;
        if(K[broj][27]=="B"): z1=z1+1;
                
print("{:.6f}".format(postotak))
with open('k-vrijednost.csv', 'w', newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow([str(x/x1),str(y/y1),str(z/z1)])
    writer.writerow(['broj','postotak'])
    for i in range (1,12700):
        writer.writerow([str(i+1),str(niz[i])])    
        
