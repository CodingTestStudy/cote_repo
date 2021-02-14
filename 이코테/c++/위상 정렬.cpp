// 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것을 의미 
#include<bits/stdc++.h>
using namespace std;

int v, e;
int indegree[100001]; 
vector<int> graph[100001];

void topology(){
	vector<int> result;
	queue<int> q;
	
	for(int i=1; i<=v; i++){
		if(indegree[i] == 0){
			q.push(i);
		}
	}
	
	while(!q.empty()){
		int now = q.front();
		q.pop();
		result.push_back(now);
		
		for(int i=0; i<graph[now].size(); i++){
			indegree[graph[now][i]] -= 1;
			if(indegree[graph[now][i]] == 0){
				q.push(graph[now][i]);				
			}
		}
	}
	for(int i=0; i<result.size(); i++){
		cout << result[i] << ' ';
	}
}

int main(void){
	cin >> v >> e;
	for(int i=0; i<e; i++){
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		indegree[b] += 1;
	}
	topology_sort();
}
