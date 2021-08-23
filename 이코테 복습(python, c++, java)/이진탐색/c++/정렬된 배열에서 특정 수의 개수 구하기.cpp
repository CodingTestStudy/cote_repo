#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int countByRange(vector<int>& v, int leftValue, int rightValue) {
	vector<int>::iterator rightIndex = upper_bound(v.begin(), v.end(), rightValue);
	vector<int>::iterator leftIndex = upper_bound(v.begin(), v.end(), leftValue);
	return rightIndex - leftIndex;
}

int n, x;
vector<int> v;

int main(void) {
	cin >> n >> x;

	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		v.push_back(temp);
	}

	int cnt = countByRange(v, x, x);

	if (cnt == 0) {
		cout << -1 << endl;
	}
	else {
		cout << cnt << endl;
	}
}