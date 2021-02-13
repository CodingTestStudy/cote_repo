#include<bits/stdc++.h>
using namespace std;

string inputData;
int num = 0; 
vector<char> str;

int main(void){
	cin >> inputData;
	for(int i=0; i<inputData.size(); i++){		
		if(isalpha(inputData[i])){
			str.push_back(inputData[i]);
		}
		else{
			num += inputData[i] - '0';
		}
	}
	sort(str.begin(), str.end());
	for(int i=0; i<str.size(); i++){
		cout << str[i];
	}	
	if(num != 0) cout << num;
}
