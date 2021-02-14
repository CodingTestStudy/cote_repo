#include<bits/stdc++.h>
#define INF 1e9
using namespace std;

int N, M;
int graph[101][101];

int main(void){
	for(int i=0; i<101; i++){
		fill(graph[i], graph[i] + 101, INF);
	}
	
	for(int i=1; i<=N; i++){
		for(int j=1; j<=N; j++){
			if(i==j){
				graph[i][j] = 0;
			}
		}
	}
	
	cin >> N >> M;
	for(int i=0; i<M; i++){
		int a, b;
		cin >> a >> b;
		graph[a][b] = 1;
		graph[b][a] = 1;
	}
	int X, K;
	cin >> X >> K;
	
	for(int k=1; k<=N; k++){
		for(int a=1; a<=N; a++){
			for(int b=1; b<=N; b++){
				graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]);
			}
		}
	}
	int min_dist = graph[1][K] + graph[K][X];
	if(min_dist == INF){
		cout << "-1" << endl;
	}
	else{
		cout << min_dist << endl;
	}
}
