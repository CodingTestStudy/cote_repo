#include<iostream>
#include<vector>
using namespace std;

int n, m;
vector<int> arr;

int main(void) {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		int x;
		arr.push_back(x);
	}

	int start = 0;
	int end = 1e9;

	int result = 0;

	while (start <= end) {
		long long int total = 0;
		int mid = (start + end) / 2;

		for (int i = 0; i < n; i++) {
			if (arr[i] > mid) {
				total += (arr[i] - mid);
			}
		}

		if (total < m) {
			end = mid - 1;
		}
		else {
			start = mid + 1;
			result = mid;
		}
	}

	cout << result << endl;
}