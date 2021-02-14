// 접두사 합 : 배열의맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
#include<bits/stdc++.h> 
using namespace std;

int n = 5;
int arr[] = {10, 20, 30, 40, 50};
int prefixSum[6];

int main(void){
	int sumValue = 0;
	for(int i=0; i<n; i++){
		sumValue += arr[i];
		prefixSum[i + 1] = sumValue; 
	}
	int left = 3;
	int right = 4;
	cout << prefixSum[right] - prefixSum[left - 1] << endl;
}
