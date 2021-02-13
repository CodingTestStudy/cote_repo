#include<bits/stdc++.h>
using namespace std;

string inputData;
int dx[] = {-2, -1, -2, -1, 1, 2, 1, 2};
int dy[] = {-1, -2, 1, 2, -2, -1, 2, 1};

int main(void){
	cin >> inputData;
	int row = inputData[1] - '0';
	int column = inputData[0] - 'a' + 1;
	
	int cnt = 0;
	for(int i=0; i<8; i++){
		int nr = row + dx[i];
		int nc = column + dy[i];
		if(nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) cnt += 1;
	}
	cout << cnt << endl;
	return 0;	
}
