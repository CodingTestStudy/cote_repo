#include<bits/stdc++.h>
using namespace std;

int n; // ���� ���� 
string target; // ã���� �ϴ� ���ڿ� 
vector<string> arr;

int sequantialSearch(int n, string target, vector<string> arr){
	for(int i=0; i<n; i++){
		if(arr[i] == target){
			return i + 1;
		}
	}
	return -1;
}

int main(void){
	cout << "������ ���� ������ �Է��� ���� �� ĭ ��� ã�� ���ڿ��� �Է�" << endl;
	cin >> n >> target;
	
	cout << "�ռ� ���� ���� ������ŭ ���ڿ��� �Է��ϼ���. ������ ���� �� ĭ���� " << endl;
	for(int i=0; i<n; i++){
		string x;
		cin >> x;
		arr.push_back(x);
	}
	cout << sequantialSearch(n, target, arr) << endl;
}
