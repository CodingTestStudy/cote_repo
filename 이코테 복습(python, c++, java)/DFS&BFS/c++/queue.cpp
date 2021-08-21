#include<iostream>
#include<queue>
using namespace std;

queue<int> q;

int main(void) {
	q.push(5);
	q.push(2);
	q.push(3);
	q.push(7);
	q.pop();
	q.push(1);
	q.push(4);
	q.pop();

	while (!q.empty()) {
		cout << q.front() << ' ';
		q.pop();
	}
}
