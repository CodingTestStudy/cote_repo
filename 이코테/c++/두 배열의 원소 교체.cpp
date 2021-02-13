#include<bits/stdc++.h>
using namespace std;

int N, K;
vector<int> A;
vector<int> B;

int main(void){
	cin >> N >> K;
	for(int i=0; i<N; i++){
		int x;
		cin >> x;
		A.push_back(x);
	}
	for(int i=0; i<N; i++){
		int x;
		cin >> x;
		B.push_back(x);
	}
	sort(A.begin(), A.end());
	sort(B.rbegin(), B.rend());
	for(int i=0; i<K; i++){
		if(A[i] < B[i]) swap(A[i], B[i]);
		else break;		
	}
	int sum_value = 0;
	for(int i=0; i<N; i++) sum_value += A[i];
	
	cout << sum_value << endl;
}
