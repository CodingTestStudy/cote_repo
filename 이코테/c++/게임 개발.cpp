#include<bits/stdc++.h>
using namespace std;

int n, m, x, y, direction;
bool visited[50][50] = {false};
int arr[50][50];
// �ϵ����� 
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

void turn_left(){
	direction -= 1;
	if(direction == -1) direction = 3;
}

int main(void){
	cin >> n >> m;
	cin >> x >> y >> direction;
	visited[x][y] = true; // ���� ��ǥ �湮 ó��
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			int x;
			cin >> x;
			arr[i][j] = x;
		}
	}
	
	int cnt = 1;
	int turn_time = 0;
	while(true){
		turn_left();
		int nx = x + dx[direction];
		int ny = y + dy[direction];
		// ȸ���� ���� ���鿡 ������ ���� ĭ�� �����ϴ� ��� �̵� 
		if(visited[nx][ny] == false && arr[nx][ny] == 0){
			x = nx;
			y = ny;
			visited[nx][ny] = true;			
			cnt += 1;
			turn_time = 0;
			continue;
		}
		// ȸ���� ���� ���鿡 ������ ���� ĭ�� ���ų� �ٴ��� ��� 
		else{
			turn_time += 1;
		}
		// �� ���� ��� �� �� ���� ���
		if(turn_time == 4){
			nx = x - dx[direction];
			ny = y - dy[direction];
			if(arr[nx][ny] == 0){
				x = nx;
				y = ny;
			}
			else{
				break;
			}
			turn_time = 0;
		} 
	}
	cout << cnt << endl;
}
