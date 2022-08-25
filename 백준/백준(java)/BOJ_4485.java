package day0825;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

// 녹색 옷 입은 애가 젤다지?
public class BOJ_4485 {

	static int N, answer;
	static int[][] map;
	static int[][] D;
	static StringBuilder sb = new StringBuilder();

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Point {
		int r, c, value;

		Point(int r, int c, int value) {
			this.r = r;
			this.c = c;
			this.value = value;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int tc = 1;
		while (true) {
			N = Integer.parseInt(br.readLine());
			if (N == 0) {
				break;
			}

			answer = 0;
			map = new int[N][N];
			D = new int[N][N];
			for (int r = 0; r < N; r++) {
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				for (int c = 0; c < N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}

			for (int i = 0; i < N; i++) {
				Arrays.fill(D[i], Integer.MAX_VALUE);
			}

			dijkstra();
			sb.append("Problem " + tc++ + ": " + answer).append('\n');

		}

		System.out.println(sb.toString());
	}

	static void dijkstra() {
		D[0][0] = map[0][0];

		PriorityQueue<Point> pq = new PriorityQueue<>((o1, o2) -> o1.value - o2.value);
		pq.add(new Point(0, 0, map[0][0]));

		while (!pq.isEmpty()) {
			Point now = pq.poll();

			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc)) {
					if (D[nr][nc] > D[now.r][now.c] + map[nr][nc]) {
						D[nr][nc] = D[now.r][now.c] + map[nr][nc];
						pq.add(new Point(nr, nc, D[nr][nc]));
					}
				}
			}
		}
		answer = D[N - 1][N - 1];
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < N) && (c >= 0) && (c < N);
	}
}
