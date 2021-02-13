#include<bits/stdc++.h>
using namespace std;

long long dp[100];

int main(void){
	dp[1] = 1;
	dp[2] = 1;
	int n = 50;
	for(int i=3; i<=n; i++){
		dp[i] = dp[i - 1] + dp[i - 2];
	}
	cout << dp[50] << endl;
	return 0;
}
