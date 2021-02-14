#include<bits/stdc++.h>
using namespace std;

int n = 1000;
vector<int> arr(n + 1, true);

int main(void){
	for(int i=2; i<=(int)sqrt(n); i++){
		if(arr[i]){
			int j=2;
			while(i * j <= n){
				arr[i* j] = false;
				j += 1;
			}
		}
	}
	for(int i=2; i<=n; i++){
		if(arr[i]){
			cout << i << ' ';
		}		
	}
	cout << endl;
}
