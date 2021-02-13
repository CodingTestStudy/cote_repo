#include<bits/stdc++.h>
using namespace std;

int N, M;
int graph[201][201];
//bool visited[201][201];

// »óÇÏÁÂ¿ì
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int bfs(int x, int y){
	queue<pair<int, int> > q;
//	visited[x][y] = true;
	q.push({x, y});
	while(!q.empty()){
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for(int i=0; i<4; i++){
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(nx < 1 || nx > N || ny < 1 || ny > M) continue;
			if(graph[nx][ny] == 0) continue;
			if(graph[nx][ny] == 1){
				graph[nx][ny] = graph[x][y] + 1;
				q.push({nx, ny});
			}
		}
	}
	return graph[N][M];
}

int main(void){
	cin >> N >> M;
	for(int i=1; i<=N; i++){
		for(int j=1; j<=M; j++){
			scanf("%1d", &graph[i][j]);
		}
	}
	cout << bfs(1, 1) << endl;
	return 0;
}
