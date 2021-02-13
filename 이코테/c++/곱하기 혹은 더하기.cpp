#include<bits/stdc++.h>
#include<string>
using namespace std;

string str;

int main(void){
	cin >> str;
	// 첫 번째 문자를 숫자로 변경한 값을 대입 
	long long result = str[0] - '0';
	
	for(int i=1; i<str.size(); i++) {
		int num = str[i] - '0';
		if(num <= 1 || result <= 1) result += num;
		else result *= num;
	}
	cout << result << endl;
}
