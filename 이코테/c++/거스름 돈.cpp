#include<bits/stdc++.h> 
using namespace std;

int coinList[4] = {500, 100, 50, 10};
int money = 1260;
int cnt = 0;

int main(){	
	for(int i=0; i<4; i++){
		cnt += money / coinList[i];
		money %= coinList[i];
	}
	cout << cnt;
}
