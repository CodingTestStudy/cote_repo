#include<bits/stdc++.h>
#define INF 1e9
using namespace std;

int n, m, start;
vector<pair<int, int> > graph[100001];
int dp[100001];

// c++에서는 우선순위큐가 최대힙이 default이다.
// 최소힙으로 구현하기 위해서는 -를 붙여준다. 
void dijkstra(int start){
	priority_queue<pair<int, int> > pq;
	pq.push({0, start});
	dp[start] = 0;
	while(!pq.empty()){
		int dist = -pq.top().first;
		int now = pq.top().second;
		pq.pop();
		
		if(dp[now] < dist) continue;
		for(int i=0; i<graph[now].size(); i++){
			int cost = dist + graph[now][i].second;
			if(cost < dp[graph[now][i].first]){
				dp[graph[now][i].first] = cost;
				pq.push(make_pair(-cost, graph[now][i].first));
			}
		} 
		
	}
}

int main(void){
	cin >> n >> m >> start;
	for(int i=0; i<m; i++){
		int a, b, c;
		graph[a].push_back({b, c});
	}
	fill(dp, dp + 100001, INF);
	dijkstra(start);
	for(int i=1; i<=n; i++){
		if(dp[i]==INF){
			cout << "INFINITY" << endl;
		}
		else{
			cout << dp[i] << endl;
		}
	}
}
