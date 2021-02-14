#include<bits/stdc++.h>
using namespace std;

int v, e;
int parent[100001];
vector<pair<int, pair<int, int> > > edges;
int result = 0;

int findParent(int x){
	if(parent[x] == x) return x;
	return parent[x] = findParent(parent[x]);
}

void unionParent(int a, int b){
	a = findParent(a);
	b = findParent(b);
	if(a < b) parent[b] = a;
	else parent[a] = b;
}

int main(void){
	cin >> v >> e;
	for(int i=1; i<=v; i++){
		parent[i] = i;
	}	
	for(int i=0; i<e; i++){
		int a, b, cost;
		cin >> a >> b >> cost;
		edges.push_back({cost, {a, b}});
	}
	sort(edges.begin(), edges.end());
	
	for(int i=0; i<edges.size(); i++){
		int cost = edges[i].first;
		int a = edges[i].second.first;
		int b = edges[i].second.second;
		if(findParent[a] != findParent[b]){
			unionParent(a, b);
			result += cost;
		}
	}	
	cout << result << endl;
}
