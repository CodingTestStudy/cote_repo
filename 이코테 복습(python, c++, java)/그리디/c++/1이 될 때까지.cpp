#include<iostream>
using namespace std;

int n, k;
int cnt;

int main() {
	cin >> n >> k;
	while (true) {
		int target = (n / k) * k;
		cnt += n - target;
		n = target;

		if (n < k) {
			cnt += (n - 1);
			break;
		}

		n /= k;
		cnt++;
	}
	cout << cnt << endl;
}