package day0826;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 미세먼지 안녕
public class BOJ_17144 {

	static int R, C, T;
	static int[][] map;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static Point[] cleaner = new Point[2];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());

		map = new int[R][C];
		int idx = 0;
		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < C; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
				if (map[r][c] == -1) {
					cleaner[idx++] = new Point(r, c);
				}
			}
		}

		while (T-- != 0) {
			spread();
			cleaner();
		}

		System.out.println(calc());
	}

	static void spread() {
		int[][] temp = new int[R][C];

		Queue<Point> dust = new ArrayDeque<>();
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (map[r][c] > 0) {
					dust.add(new Point(r, c));
				}
			}
		}

		while (!dust.isEmpty()) {
			Point now = dust.poll();
			int cnt = 0;

			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc) && map[nr][nc] != -1) {
					cnt++;
					temp[nr][nc] += map[now.r][now.c] / 5;
				}
			}
			temp[now.r][now.c] -= map[now.r][now.c] / 5 * cnt;
		}

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				map[r][c] += temp[r][c];
			}
		}

	}

	static void cleaner() {
		// up
		Point up = cleaner[0];
		for (int r = up.r; r > 0; r--) {
			map[r][up.c] = map[r - 1][up.c];
		}
		for (int c = 0; c < C - 1; c++) {
			map[0][c] = map[0][c + 1];
		}
		for (int r = 0; r < up.r; r++) {
			map[r][C - 1] = map[r + 1][C - 1];
		}
		for (int c = C - 1; c > 0; c--) {
			map[up.r][c] = map[up.r][c - 1];
		}
		map[up.r][up.c + 1] = 0;
		map[up.r][up.c] = -1;

		// down
		Point down = cleaner[1];
		for (int r = down.r; r < R - 1; r++) {
			map[r][0] = map[r + 1][0];
		}
		for (int c = 0; c < C - 1; c++) {
			map[R - 1][c] = map[R - 1][c + 1];
		}
		for (int r = R - 1; r > down.r; r--) {
			map[r][C - 1] = map[r - 1][C - 1];
		}
		for (int c = C - 1; c > 0; c--) {
			map[down.r][c] = map[down.r][c - 1];
		}

		map[down.r][down.c + 1] = 0;
		map[down.r][down.c] = -1;
	}

	static int calc() {
		int answer = 0;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (map[r][c] != -1) {
					answer += map[r][c];
				}
			}
		}
		return answer;
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < R) && (c >= 0) && (c < C);
	}

	static void print() {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				System.out.print(map[r][c] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
}
