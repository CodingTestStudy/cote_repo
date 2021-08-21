#include<iostream>
#include<stdio.h>
using namespace std;

int n, m;
int graph[1001][1001];

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

bool dfs(int r, int c) {
	
	if (r < 0 || c < 0 || r >= n || c >= m) {
		return false;
	}

	if (graph[r][c] == 0) {
		graph[r][c] = 1;
		for (int i = 0; i < 4; i++) {
			dfs(r + dr[i], c + dc[i]);
		}
		return true;
	}
	return false;
}

int main(void) {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf_s("%1d", &graph[i][j]);
		}
	}

	int result = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (dfs(i, j)) {
				result++;
			}
		}
	}
	cout << result << endl;
}