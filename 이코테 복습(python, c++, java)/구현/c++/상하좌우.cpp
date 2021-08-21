#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int n;
string plan;
int x = 1, y = 1;

int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };
char moveTypes[4] = { 'L','R','U','D' };

int main() {
	cin >> n;
	cin.ignore(); //버퍼 비우기
	getline(cin, plan);

	for (int i = 0; i < plan.size(); i++) {
		char p = plan[i];
		int nx = -1, ny = -1;

		for (int j = 0; j < 4; j++) {
			if (p == moveTypes[j]) {
				nx = x + dx[j];
				ny = y + dy[j];
				break;
			}
		}

		if (nx < 1 || ny < 1 || nx > n || ny > n) continue;
		x = nx;
		y = ny;
	}
	cout << x << " " << y << endl;
	return 0;
}