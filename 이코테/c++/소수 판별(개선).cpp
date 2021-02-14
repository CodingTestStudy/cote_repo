#include<bits/stdc++.h> 
using namespace std;

bool isPrimeNumber(int x){
	for(int i=2; i<=(int)sqrt(x); i++){
		if(x % i == 0) return false;
	}
	return true;
}

int main(void){
	cout << isPrimeNumber(4) << endl;
	cout << isPrimeNumber(7) << endl;
}
