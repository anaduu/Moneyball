#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int broj=0;
map <string,double> mapa1;
map <string,double> mapa2;
set <string> s;
int main()
{
	ifstream myfile;
	myfile.open("dr.csv");

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
		mapa2[line]+=b; 
   	}

	myfile.close();
set <string>::iterator si;
printf("U setu se nalazi:\n");
double rezultat;
int imam_ukupno=0;
ofstream novifile;
novifile.open("dr1.csv");
for(si=s.begin();si!=s.end();++si)
{
 	if(mapa1[*si]>20) {
				rezultat=mapa2[*si]/mapa1[*si];
				cout << *si <<" "<<mapa1[*si]<<" " <<mapa2[*si];
				printf(" %lf\n",rezultat);
				++imam_ukupno;
				novifile << *si<< ","<< rezultat << endl;	
			  }
}
//printf("Duljina seta je: %d\n",s.size());
printf("Na kraju imam ukupno %d država\n",imam_ukupno);

return 0;
}

