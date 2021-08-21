#include<iostream>
using namespace std;

int cnt = 0;
string str;
int dr[] = { -2, -1, 1, 2, 2, 1, -1, -2 };
int dc[] = { -1, -2, -2, -1, 1, 2, 2, 1 };

int main() {
	cin >> str;
	int r = str[1] - '0';
	int c = str[0] - 'a' + 1;
	
	int nr = -1, nc = -1;
	
	for (int i = 0; i < 8; i++) {
		nr = r + dr[i];
		nc = c + dc[i];

		if (nr < 1 || nc < 1 || nr > 8 || nc > 8) {
			continue;
		}
		cnt++;
	}
	cout << cnt << endl;
	return 0;
}