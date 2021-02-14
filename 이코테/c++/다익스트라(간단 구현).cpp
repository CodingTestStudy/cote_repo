#include<bits/stdc++.h>
#define INF 1e9
using namespace std;

int n, m, start;
vector<pair<int, int> > graph[100001];
bool visited[100001];
int dp[100010];

int getSmallestNode(){
	int min_value = INF;
	int index = 0;
	for(int i=1; i<=n; i++){
		if(dp[i] < min_value && !visited[i]){
			min_value = dp[i];
			index = i;
		}
	}
	return index;
}

void dijkstra(int start){
	dp[start] = 0;
	visited[start] = true;
	for(int j=0; j<graph[start].size(); j++){
		dp[graph[start][j].first] = graph[start][j].second;
	}
	// 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복 
	for(int i=0; i<n-1; i++){
		int now = getSmallestNode();
		visited[now] = true;
		for(int j=0; j<graph[now].size(); j++){
			int cost = dp[now] + graph[now][j].second;
			if(cost < dp[graph[now][j].first]){
				dp[graph[now][j].first] = cost;
			}
		}
	}
}

int main(void){
	cin >> n >> m >> start;
	for(int i=0; i<n; i++){
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back({b, c});
	}
	fill_n(dp, 100001, INF);
	dijkstra(start);
	for(int i=1; i<=n; i++){
		if(dp[i] == INF){
			cout << "INFINITY" << endl;
		}
		else{
			cout << dp[i] << endl;
		}
	}
}
