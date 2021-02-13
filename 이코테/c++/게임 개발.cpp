#include<bits/stdc++.h>
using namespace std;

int n, m, x, y, direction;
bool visited[50][50] = {false};
int arr[50][50];
// 북동남서 
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

void turn_left(){
	direction -= 1;
	if(direction == -1) direction = 3;
}

int main(void){
	cin >> n >> m;
	cin >> x >> y >> direction;
	visited[x][y] = true; // 현재 좌표 방문 처리
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
		// 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동 
		if(visited[nx][ny] == false && arr[nx][ny] == 0){
			x = nx;
			y = ny;
			visited[nx][ny] = true;			
			cnt += 1;
			turn_time = 0;
			continue;
		}
		// 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 
		else{
			turn_time += 1;
		}
		// 네 방향 모두 갈 수 없는 경우
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
