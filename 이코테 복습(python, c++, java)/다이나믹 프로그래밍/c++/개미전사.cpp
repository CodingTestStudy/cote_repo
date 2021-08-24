#include<iostream>
#include<vector>
using namespace std;

int dp[100];
int n;
vector<int> arr;

int main(void) {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		arr.push_back(x);
	}

	dp[0] = arr[0];
	dp[1] = max(arr[0], arr[1]);

	for (int i = 2; i < n; i++) {
		dp[i] = max(dp[i - 1], dp[i - 2] + arr[i]);
	}
	cout << dp[n - 1] << endl;
	return 0;
}