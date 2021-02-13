#include<bits/stdc++.h>
using namespace std;

int main(){
	int N, K, cnt, target;
	cin >> N >> K;	
	
	while(true){		
		target = (N / K) * K;
		cnt += (N - target);
		N = target;
		if(N < K){
			break;
		}
		N /= K;
		cnt += 1;
	} 
	cnt += (N - 1);
	cout << cnt << endl;
}
