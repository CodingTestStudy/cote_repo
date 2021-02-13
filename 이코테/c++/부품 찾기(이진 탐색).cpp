#include<bits/stdc++.h> 
using namespace std;

int N;
vector<int> store;
int M;
vector<int> customer;

int binarySearch(vector<int>& store, int target, int start, int end){
	while(start <= end){
		int mid = (start + end) / 2;
		if(store[mid] == target) return mid;
		else if(store[mid] > target) end = mid - 1;
		else start = mid + 1;
	}
	return -1;
}

int main(void){
	cin >> N;
	for(int i=0; i<N; i++){
		int x;
		cin >> x;
		store.push_back(x);
	}
	sort(store.begin(), store.end());	
	cin >> M;
	for(int i=0; i<M; i++){
		int x;
		cin >> x;
		customer.push_back(x);
	}
	for(int i=0; i<M; i++){				
		int result = binarySearch(store, customer[i], 0, N - 1);		
		if(result == -1) cout << "no" << ' ';
		else cout << "yes" << ' ';		
	}	
	cout << endl;
	return 0;
}
