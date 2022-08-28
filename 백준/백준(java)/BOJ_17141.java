package day0828;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

// 연구소2
public class BOJ_17141 {

	static int N, M, answer;
	static int[][] map;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static int zeroCnt;

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static int[] cards;
	static boolean[] selected;
	static ArrayList<Point> virusList;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		cards = new int[M];
		for (int i = 0; i < M; i++) {
			cards[i] = i;
		}
		virusList = new ArrayList<>();
		map = new int[N][N];
		answer = Integer.MAX_VALUE;
		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < N; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
				if (map[r][c] == 0) {
					zeroCnt++;
				} else if (map[r][c] == 2) {
					virusList.add(new Point(r, c));
				}
			}
		}

		selected = new boolean[virusList.size()];
		comb(0, 0);
		if (answer == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(answer);
		}
	}

	static void bfs() {
		Queue<Point> q = new ArrayDeque<>();
		boolean[][] visited = new boolean[N][N];
		int zero = zeroCnt;
		int[][] temp = deepcopy(map);
		for (int i = 0; i < virusList.size(); i++) {
			Point p = virusList.get(i);
			if (selected[i]) {
				q.add(p);
				visited[p.r][p.c] = true;
				temp[p.r][p.c] = 0;
			}
			temp[p.r][p.c] = 0;
		}

		int result = -1;
		while (!q.isEmpty()) {
			Point now = q.poll();
			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc) && !visited[nr][nc] && temp[nr][nc] == 0) {
					temp[nr][nc] = temp[now.r][now.c] + 1;
					visited[nr][nc] = true;
					result = Math.max(result, temp[nr][nc]);
					q.add(new Point(nr, nc));
					zero--;
				}
			}
		}

		if (zero <= 0) {
			print(temp);
			System.out.println(result);
			System.out.println();
			answer = Math.min(answer, result);
		}
	}

	static void print(int[][] temp) {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				System.out.print(temp[r][c] + " ");
			}
			System.out.println();
		}
	}

	static void comb(int idx, int cnt) {
		if (cnt == M) {
			bfs();
			return;
		}

		if (idx == virusList.size()) {
			return;
		}

		selected[idx] = true;
		comb(idx + 1, cnt + 1);
		selected[idx] = false;
		comb(idx + 1, cnt);
	}

	static int[][] deepcopy(int[][] origin) {
		int[][] copy = new int[N][N];
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				copy[r][c] = origin[r][c];
			}
		}
		return copy;
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < N) && (c >= 0) && (c < N);
	}
}
