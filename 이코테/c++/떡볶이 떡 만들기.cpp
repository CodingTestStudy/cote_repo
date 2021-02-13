#include<bits/stdc++.h>
using namespace std;

int N, M;
vector<int> dduk;

int binarySearch(vector<int>& dduk, int start, int end){
	int result = 0;
	while(start <= end){
		long long int total = 0;
		int mid = (start + end) / 2;
		for(int i=0; i<N; i++){
			if(dduk[i] > mid) total += dduk[i] - mid;
		}
		if(total < M) end = mid - 1;
		else{
			result = mid;
			start = mid + 1;
		}
	}
	return result;
}


int main(void){
	cin >> N >> M;
	for(int i=0; i<N; i++){
		int x;
		cin >> x;
		dduk.push_back(x);
	}	
	sort(dduk.begin(), dduk.end());
	cout << binarySearch(dduk, 0, 1e9) << endl;
}
