#include<iostream>
#include<vector>
using namespace std;

int n, m;
vector<int> coins;

int main(void) {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		coins.push_back(x);
	}

	vector<int>dp(m + 1, 100001);

	dp[0] = 0;
	for (int i = 0; i < n; i++) {
		for (int j = coins[i]; j < m + 1; j++) {
			if (dp[j - coins[i]] != 10001) {
				dp[j] = min(dp[j], dp[j - coins[i]] + 1);
			}
		}
	}
	if (dp[m] == 100001) {
		cout << -1 << endl;
	}
	else {
		cout << dp[m] << endl;
	}
}