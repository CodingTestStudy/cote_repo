#include<bits/stdc++.h> 
using namespace std;

int N;
vector<int> data;

int main(void){
	cin >> N;
	for(int i=0; i<N; i++){
		int x;
		cin >> x;
		data.push_back(x);
	}
	sort(data.rbegin(), data.rend());
	for(int i=0; i<N; i++){
		cout << data[i] << ' ';
	}
	return 0;
}
