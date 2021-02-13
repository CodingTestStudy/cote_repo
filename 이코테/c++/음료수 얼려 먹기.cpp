#include<bits/stdc++.h>
using namespace std;

int N, M;
int graph[1001][1001];

bool dfs(int x, int y){
	if(x < 0 || x >= N || y < 0 || y >= M) return false;
	if(graph[x][y] == 0){
		graph[x][y] = 1;
		dfs(x - 1, y);
		dfs(x, y - 1);
		dfs(x + 1, y);
		dfs(x, y + 1);
		return true;
	}
	return false;
}

int main(void){
	cin >> N >> M;
	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			scanf("%1d", &graph[i][j]);
		}
	}
	int result = 0;
	for(int i=0; i<N; i++){  
		for(int j=0; j<M; j++){
			if(dfs(i, j)){
				result += 1;
			}
		}
	}
	cout << result << endl;
}
