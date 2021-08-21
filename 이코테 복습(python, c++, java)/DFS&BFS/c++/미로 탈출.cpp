#include<iostream>
#include<queue>
using namespace std;

int n, m;
int graph[201][201];

int dr[] = { -1, 1, 0, 0 };
int dc[] = { 0, 0, -1, 1 };

int bfs(int r, int c) {
	queue<pair<int, int>>q;
	q.push({ r, c });

	while (!q.empty()) {
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];

			if (nr >= 0 && nc >= 0 && nr < n && nc < m) {
				if (graph[nr][nc] == 0) {
					continue;
				}

				if (graph[nr][nc] == 1) {
					graph[nr][nc] = graph[r][c] + 1;
					q.push({ nr, nc });
				}
			}
		}
	}
	return graph[n - 1][m - 1];
}

int main(void) {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf_s("%1d", &graph[i][j]);
		}
	}

	cout << bfs(0, 0) << endl;
	return 0;
}