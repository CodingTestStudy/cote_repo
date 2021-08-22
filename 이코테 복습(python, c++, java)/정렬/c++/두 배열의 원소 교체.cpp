#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n, k;
vector<int> a, b;

bool compare(int x, int y) {
	return x > y;
}

int main(void) {
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		a.push_back(x);
	}
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		b.push_back(x);
	}

	sort(a.begin(), a.end());
	sort(b.begin(), b.end(), compare);

	int result = 0;
	for (int i = 0; i < k; i++) {
		if (a[i] < b[i]) {
			swap(a[i], b[i]);
		}
		else {
			break;
		}
	}

	for (int i = 0; i < n; i++) {
		result += a[i];
	}
	cout << result << endl;
	return 0;
}