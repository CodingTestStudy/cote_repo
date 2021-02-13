#include<bits/stdc++.h>
using namespace std;

long long dp[100];

long long fibo(int x){
	if(x == 1 or x== 2){
		return 1;
	}
	if(dp[x] != 0){
		return dp[x];
	}
	dp[x] = fibo(x - 1) + fibo(x - 2);
	return dp[x];
}

int main(void){
	cout << fibo(50) << endl;
	return 0;
}


