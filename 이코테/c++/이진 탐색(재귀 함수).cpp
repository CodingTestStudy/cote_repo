#include<bits/stdc++.h>
using namespace std;

int n, target;
vector<int> arr;

int binarySearch(vector<int>& arr, int target, int start, int end){
	if(start > end) return -1;
	int mid = (start + end) / 2;
	if(arr[mid] == target) return mid;
	else if(arr[mid] > target) binarySearch(arr, target, start, mid - 1);
	else binarySearch(arr, target, mid + 1, end);			
}

int main(void){
	cin >> n >> target;
	for(int i=0; i<n; i++){
		int x;
		cin >> x;
		arr.push_back(x);
	}
	int result = binarySearch(arr, target, 0, n - 1);
	if(result == -1) cout <<"원소가 존재하지 않습니다." << endl; 
	else cout << result + 1 << endl;
}
