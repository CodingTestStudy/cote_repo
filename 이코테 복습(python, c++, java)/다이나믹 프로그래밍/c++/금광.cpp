#include<iostream>
using namespace std;

int testCase, n, m;
int arr[20][20];
int dp[20][20];

int main(void) {
	cin >> testCase;
	for (int tc = 0; tc < testCase; tc++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> arr[i][j];
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				dp[i][j] = arr[i][j];
			}
		}

		for (int j = 1; j < m; j++) {
			for (int i = 0; i < n; i++) {
				int leftUp, leftDown, left;

				if (i == 0) {
					leftUp = 0;
				}
				else {
					leftUp = dp[i - 1][j - 1];
				}
				if (i == n - 1) {
					leftDown = 0;
				}
				else {
					leftDown = dp[i + 1][j - 1];
				}

				left = dp[i][j - 1];
				dp[i][j] = dp[i][j] + max(leftUp, max(left, leftDown));
			}
		}

		int result = 0;
		for (int i = 0; i < n; i++) {
			result = max(result, dp[i][m - 1]);
		}
		cout << result << endl;
	}

}