#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
struct par
{
	int uk;
	double koef;
};
int broj=0,b,c,a;
map <string,double> mapa1;
map <string,double> mapa2;
set <string> s;
vector <int> v;
par polje [20000];
int brojac=0;
par par;
int main()
{
	ifstream myfile;
	myfile.open("vratari-tezina-visina.csv");

	while(myfile.good())
	{
		string line1;
		string line2;
		string line3;

		getline(myfile, line1, ',');
    		a=atoi(line1.c_str());	
		getline(myfile, line2,',');
		b=atoi(line2.c_str());
    		getline(myfile, line3 );
   		
		//Funkcija koja ince pretvara u cm
		string  s1=line3.substr(0,1);
		//cout << line1 <<" "<<line2<<" "<<line3 << endl;
		int x=atoi(s1.c_str());
        //cout <<"s1 je"<<s1<<" ,a X je "<<x <<endl;
        line3.erase(0,2);
        //cout << "Line3 nakon brisanja je"<<line3 << endl;
		int y=atoi(line3.c_str());
        ///cout <<"Y je "<<y <<endl;		
        double uk=(x*12 + y)*2.54;
		printf("%lf\n",uk);
		par.uk=a;
		par.koef=b/uk;
		
		polje[brojac]=par;
		++brojac; 
   	}

	myfile.close();
ofstream novifile;
novifile.open("koef.csv");
novifile << "overall" <<","<< "koef"<<endl;
    for(int i=0;i<brojac;++i)
    {
        novifile << polje[i].uk <<","<<polje[i].koef<<endl;    
    }
return 0;
}

