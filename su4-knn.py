import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
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
                    for i in range(27,56):
                        sol=sol+((K[b][i]-K[a][i])**2)
                    return sol**(1/float(2))


DATA_LOCATION = "data1.csv"
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
dsed="Crossing"
dosa="Finishing"
ddev="HeadingAccuracy"
trides="ShortPassing"
trijed="Volleys"
tridva="Dribbling"
tritri="Curve"
tricet="FKAccuracy"
tripet="LongPassing"
trises="BallControl"
trised="Acceleration"
triosa="SprintSpeed"
tridev="Agility"
cetdes="Reactions"
cetjed="Balance"
cetdva="ShotPower"
cettri="Jumping"
cetcet="Stamina"
cetpet="Strength"
cetses="LongShots"   
cetsed="Aggression"
cetosa="Interceptions"
cetdev="Positioning"
petdes="Vision"
petjed="Penalties"
petdva="Composure"
pettri="Marking"
petcet="StandingTackle"
petpet="SlidingTackle"
petses="Potential"
petsed="Overall"
petosa="Name"
petdev="Position"
datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE, treci,cetvrti,peti,peti,sest,sedam,osam,devet,deset,jed,dva,tri,cet,pet,ses,sed,osa,dev,dvades,djed,ddva,dtri,dcet,dpet,dses,dsed,dosa,ddev,trides,trijed,tridva,tritri,tricet,tripet,trises,trised,triosa,tridev,cetdes,cetjed,cetdva,cettri,cetcet,cetpet,cetses,cetsed,cetosa,cetdev,petdes,petjed,petdva,pettri,petcet,petpet,petses,petsed,petosa,petdev]]

K = data1.values
#plt.scatter(K[:,0], K[:,1], K[:,2],color = 'g')
#plt.show()
min=9999999
sol1=0
k=0
broj = int(input())
print("Ime igarača je:", K[broj][58])
print("Njegov overall je", K[broj][57])
print("Njegova pozicija je", K[broj][59])
for i in range(0,5000):
    if(K[i][59] == "GK"): K[i][59]="G"
    if(K[i][59] == "CB") or (K[i][59] == "LCB") or (K[i][59] == "RCB") or (K[i][59] == "LB") or (K[i][59] == "RB") or (K[i][59] == "LWB") or (K[i][59] == "RWB") : K[i][59]="B"
    if(K[i][59] == "CM") or (K[i][59] == "LDM") or (K[i][59] == "LAM") or (K[i][59] == "RDM") or (K[i][59] == "RAM") or (K[i][59]=="CDM") or(K[i][59]=="CAM") or(K[i][59]=="LM")or(K[i][59]=="RM") or (K[i][59] == "RCM") or (K[i][59] == "LCM") : K[i][59]="V"
if(K[i][59] == "ST") or (K[i][59] == "CF") or (K[i][59] == "LW") or (K[i][59] == "RW") or (K[i][59] == "LF") or (K[i][59] == "RF") or (K[i][59] == "LS") or (K[i][59] == "RS") : K[i][59]="N"
polje = [];
if(K[broj][59]=="G"): exit(-1);
for i in range(0,2000):
    sol1=udaljenost(i,broj)
    if(sol1==0): sol1=99999
    if(K[i][59]==K[broj][59]): polje.append(par(sol1,i))    
    polje.sort()
a=0
b=0
c=0
for i in range(0,4):            
           a+=polje[i].x;
           print(polje[i].x,K[polje[i].y][57])
            
for i in range(0,4):            
          polje[i].x=polje[i].x/a;
          
for i in range(0,4):            
         b+=polje[i].x*K[polje[i].y][57];
print(b)
