#include<bits/stdc++.h>
#define INF 1e9
using namespace std;

int N, M, C;
vector<pair<int, int> > graph[30001];
int dp[30001];

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
			int cost = graph[now][i].second + dist;
			if(cost < dp[graph[now][i].first]){
				dp[graph[now][i].first] = cost;
				pq.push(make_pair(-cost, graph[now][i].first));
			}
		}
	}
}

int main(void){
	cin >> N >> M >> C;
	for(int i=0; i<M; i++){
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back({b, c});
	}
	fill(dp, dp + 30001, INF);
	dijkstra(C);
	int count = 0;
	int max_dp = 0;
	for(int i=1; i<=N; i++){
		if(dp[i] != INF){
			count++;
			max_dp = max(max_dp, dp[i]);
		}
	}
	cout << count - 1 <<' ' << max_dp << endl;
}
