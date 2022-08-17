package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

// 감시
public class BOJ_15683 {

	static int n, m;
	static int[][] map;
	static List<Point> pointList = new ArrayList<>();
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int[][] dir = { { 0, 1, 2, 3 }, {}, {}, {}, {} };
	static int answer;

	static class Point {
		int r, c, num;

		Point(int r, int c, int num) {
			this.r = r;
			this.c = c;
			this.num = num;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		answer = Integer.MAX_VALUE;

		for (int r = 0; r < n; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < m; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());

				if (map[r][c] > 0 && map[r][c] < 6) {
					pointList.add(new Point(r, c, map[r][c]));
				}
			}
		}

		dfs(0, map);
		System.out.println(answer);
	}

	static void dfs(int start, int[][] temp) {
		if (start == pointList.size()) {
			int value = calc(temp);
			answer = Math.min(answer, value);
			return;
		}

		int r = pointList.get(start).r;
		int c = pointList.get(start).c;
		int num = pointList.get(start).num;

		// 복사 배열
		int[][] newTemp;
		switch (num) {
		case 1:
			for (int i = 0; i < 4; i++) {
				newTemp = deepcopy(temp);
				int nr = r + dr[i];
				int nc = c + dc[i];
				while (checkRange(nr, nc) && newTemp[nr][nc] != 6) {
					newTemp[nr][nc] = -1;
					nr += dr[i];
					nc += dc[i];

				}
				dfs(start + 1, newTemp);
			}
			break;
		case 2:
			newTemp = deepcopy(temp);
			for (int i = 0; i < 2; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				while (checkRange(nr, nc) && newTemp[nr][nc] != 6) {
					newTemp[nr][nc] = -1;
					nr += dr[i];
					nc += dc[i];
				}
			}
			dfs(start + 1, newTemp);
			newTemp = deepcopy(temp);
			for (int i = 2; i < 4; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				while (checkRange(nr, nc) && newTemp[nr][nc] != 6) {
					newTemp[nr][nc] = -1;
					nr += dr[i];
					nc += dc[i];
				}
			}
			dfs(start + 1, newTemp);
			break;
		case 3:
			int[][] test = { { 0, 3 }, { 3, 1 }, { 1, 2 }, { 2, 0 } };

			for (int[] t : test) {
				newTemp = deepcopy(temp);
				for (int i : t) {
					int nr = r + dr[i];
					int nc = c + dc[i];
					while (checkRange(nr, nc) && newTemp[nr][nc] != 6) {
						newTemp[nr][nc] = -1;
						nr += dr[i];
						nc += dc[i];
					}
				}
				dfs(start + 1, newTemp);
			}

			break;
		case 4:
			for (int i = 0; i < 4; i++) {
				newTemp = deepcopy(temp);
				for (int j = 0; j < 4; j++) {
					if (i == j) {
						continue;
					}
					int nr = r + dr[j];
					int nc = c + dc[j];
					while (checkRange(nr, nc) && newTemp[nr][nc] != 6) {
						newTemp[nr][nc] = -1;
						nr += dr[j];
						nc += dc[j];
					}
				}
				dfs(start + 1, newTemp);
			}
			break;
		case 5:
			newTemp = deepcopy(temp);
			for (int i = 0; i < 4; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				while (checkRange(nr, nc) && newTemp[nr][nc] != 6) {
					newTemp[nr][nc] = -1;
					nr += dr[i];
					nc += dc[i];
				}
			}
			dfs(start + 1, newTemp);
			break;

		}

	}

	static void print(int[][] temp) {
		for (int i = 0; i < temp.length; i++) {
			for (int j = 0; j < temp[0].length; j++) {
				System.out.print(temp[i][j] + " ");
			}
			System.out.println();
		}
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < n) && (c >= 0) && (c < m);
	}

	static int calc(int[][] temp) {
		int cnt = 0;
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < m; c++) {
				if (temp[r][c] == 0) {
					cnt++;
				}
			}
		}
		return cnt;
	}

	static int[][] deepcopy(int[][] temp) {
		int[][] newTemp = new int[temp.length][temp[0].length];
		for (int r = 0; r < temp.length; r++) {
			for (int c = 0; c < temp[0].length; c++) {
				newTemp[r][c] = temp[r][c];
			}
		}
		return newTemp;
	}
}
