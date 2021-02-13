#include<bits/stdc++.h>
using namespace std;

int n;
string plans;
int x = 1, y = 1;
// L, R, U, D
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char moveTypes[4] = {'L', 'R', 'U', 'D'};

int main(void){
	cin >> n;
	cin.ignore(); // 버퍼 비우기
	getline(cin, plans); 
	
	for(int i=0; i<plans.size(); i++){
		char plan = plans[i];
		int nx = -1, ny = -1;
		for(int j=0; j<4; j++){
			if(plan == moveTypes[j]){
				nx = x + dx[j];
				ny = y + dy[j];
			}
		}
		
		if(nx < 1 || nx > n || ny < 1 || ny > n) continue;
		x = nx;
		y = ny;
	}
	cout << x << ' ' << y << endl;
	return 0;
} 
