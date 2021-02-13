#include<bits/stdc++.h>
using namespace std;

int N; 
vector<int> arr;

int main(){
	cin >> N;
	for(int i=0; i<N; i++){
		int x;
		cin >> x;
		arr.push_back(x);
	}  
	sort(arr.begin(), arr.end());
	
	int result = 0;
	int cnt = 0;
	for(int i=0; i<N; i++){
		cnt += 1;
		if(cnt >= arr[i]){
			result += 1;
			cnt = 0;
		}
	}
	cout << result << endl;
}
