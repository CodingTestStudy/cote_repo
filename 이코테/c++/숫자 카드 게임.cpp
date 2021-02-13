#include<bits/stdc++.h>
using namespace std;

int N, M;
int result;

int main(){
	cin >> N >> M;
	for(int i=0; i<N; i++){
		int min_value = 10001;
		for(int j=0; j<M; j++){
			int x;
			cin >> x;
			min_value = min(min_value, x);
		}
		result = max(result, min_value);
	}
	
	cout << result << endl;
}
