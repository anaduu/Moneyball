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
	string ime;
	int broj;
};
int broj=0;
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
	myfile.open("vrijednost_overall.csv");

	while(myfile.good())
	{
		string line;
		string line1;

		getline(myfile, line, ',');
    		// cout << "Nat: " << line << " " ; 
	
		s.insert(line);
		mapa1[line]++;
    		getline(myfile, line1 );
   		int b = atoi(line1.c_str());
		//  printf("broj je %d\n",b);
		par.ime=line;
		par.broj=b;
		polje[brojac]=par;
		++brojac; 
   	}

	myfile.close();
set <string>::iterator si;
printf("U setu se nalazi:\n");
/*double rezultat;
int imam_ukupno=0;
ofstream novifile;
cout << "Duljina set je" << s.size() << endl;
novifile.open("dr1.csv");
cout << "poslije kreirananja" << endl;
novifile << "drzava" <<","<< "overall"<<","<<"koef"<<endl;
printf("Tu sam ;I - prije for petlje\n");
for(si=s.begin();si!=s.end();++si)
{
	cout << mapa1[*si]<<endl;
 	if(mapa1[*si]>23) {
				for(int i =0;i<brojac;++i)
				{
					if(polje[i].ime==*si) v.push_back(polje[i].broj);
				}			
			  
				sort(v.begin(),v.end());
				reverse(v.begin(),v.end());
				for(int j=0;j<=24;++j)
				{
					mapa2[*si]+=v[j];
				}
				v.clear();
			//	cout << *si <<" "<<mapa1[*si]<<" " <<mapa2[*si];
				
				rezultat=mapa2[*si]/24;
				novifile << *si<< ","<< rezultat  << endl;	
			}
}
			 

//printf("Duljina seta je: %d\n",s.size());
//printf("Na kraju imam ukupno %d država\n",imam_ukupno);
*/
return 0;

}

