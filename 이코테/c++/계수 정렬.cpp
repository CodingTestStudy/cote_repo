#include<bits/stdc++.h>
#define MAX_VALUE 9
using namespace std;

int n = 15;
int arr[15] = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
int cnt[MAX_VALUE + 1];

int main(void){
	for(int i=0; i<n; i++){
		cnt[arr[i]] += 1;
	}
	for(int i=0; i<=MAX_VALUE; i++){
		for(int j=0; j<cnt[i]; j++){
			cout << i << ' ';
		}
	}
}
