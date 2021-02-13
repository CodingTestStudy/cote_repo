#include<bits/stdc++.h>
using namespace std;

int N, M;
set<int> s;
vector<int> target;

int main(void){
	cin >> N;
	for(int i=0; i<N; i++){
		int x;
		cin >> x;
		s.insert(x);
	}
	cin >> M;
	for(int i=0; i<M; i++){
		int x;
		cin >> x;
		target.push_back(x);
	}
	for(int i=0; i<M; i++){
		if(s.find(target[i]) != s.end()) cout << "yes" << ' ';
		else cout << "no" << ' ';		
	}
	cout << endl;
	return 0;
}
