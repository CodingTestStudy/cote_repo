 #include<bits/stdc++.h>
 using namespace std;
 
 int N, M;
 int arr[1000001];
 vector<int> target;
 
 int main(void){
 	cin >> N;
 	for(int i=0; i<N; i++){
 		int x;
 		cin >> x;
 		arr[x] = 1;
	 }
	 cin >> M;
	 for(int i=0; i<M; i++){
	 	int x;
	 	cin >> x;
	 	target.push_back(x);
	 }
	 for(int i=0; i<M; i++){
	 	if(arr[target[i]] == 1) cout << "yes" << ' ';
	 	else cout << "no" << ' ';
	 }
	 cout << endl;
	 return 0;
 }
