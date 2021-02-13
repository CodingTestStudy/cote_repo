#include<bits/stdc++.h>
using namespace std;

int N, M, K;
vector<int> nums;


int main(void){
	cin >> N >> M >> K;
	cin.ignore();
	for(int i=0; i<N; i++){
		int inputData;
		cin >> inputData;
		nums.push_back(inputData);
	}
	sort(nums.rbegin(), nums.rend());
	int multiply_cnt = M / (K + 1);
	int add_cnt = M - (multiply_cnt * (K + 1));				
	int result = multiply_cnt * (nums[0] * K + nums[1]) + add_cnt * (nums[0]);
	cout << result << endl;
}
