#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n;
vector<int>arr;

int main(void) {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		arr.push_back(x);
	}
	sort(arr.begin(), arr.end());

	int group = 0;
	int total = 0;

	for (int i = 0; i < arr.size(); i++) {
		total += 1;
		if (total >= arr[i]) {
			group++;
			total = 0;
		}
	}
	cout << group << endl;

}