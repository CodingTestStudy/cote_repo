#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

string str;
vector<char>result;
int num = 0;

int main() {
	cin >> str;
	for (int i = 0; i < str.size(); i++) {
		if (isalpha(str[i])) {
			result.push_back(str[i]);
		}
		else {
			num += str[i] - '0';
		}
	}
	sort(result.begin(), result.end());
	for (int i = 0; i < result.size(); i++) {
		cout << result[i];
	}
	if (num != 0) {
		cout << num;
	}
	cout << endl;

}