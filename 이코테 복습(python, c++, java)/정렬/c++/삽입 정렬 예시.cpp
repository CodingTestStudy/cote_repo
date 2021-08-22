#include<iostream>
using namespace std;

int n = 10;
int target[10] = { 7, 5, 9, 0, 3, 1, 6, 2, 4, 8 };

int main(void) {
	for (int i = 1; i < n; i++) {
		for (int j = i; j > 0; j--) {
			if (target[j] < target[j - 1]) {
				swap(target[j], target[j - 1]);
			}
			else {
				break;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		cout << target[i] << " ";
	}
	return 0;

}