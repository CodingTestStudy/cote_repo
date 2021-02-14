#include<bits/stdc++.h>
using namespace std;

int n = 5;
int m = 5;
int arr[] = {1, 2, 3, 2, 5};

int main(void){
	int cnt = 0, intervalSum = 0, end = 0;
	for(int start = 0; start < n; start++){
		while(intervalSum < m && end < n){
			intervalSum += arr[end];
			end += 1;
		}
		if(intervalSum == m){
			cnt += 1;
		}
		intervalSum -= arr[start];
	}
	cout << cnt << endl;
}
