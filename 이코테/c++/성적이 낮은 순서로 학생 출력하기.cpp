#include<bits/stdc++.h>
using namespace std;

int N;
vector<pair<string, int> > data;

bool compare(const pair<string, int> &a, const pair<string, int> &b){
	return a.first > b.first;
}

int main(void){
	cin >> N;
	for(int i=0; i<N; i++){
		string name;
		int score;
		cin >> name >> score;
		data.push_back({name, score});
	}
	
	sort(data.begin(), data.end(), compare);
	for(int i=0; i<N; i++){
		cout << data[i].first << ' ';
	}
	return 0;	
}
