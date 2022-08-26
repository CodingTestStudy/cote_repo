package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 봄버맨
public class BOJ_16918 {
	static int R, C, N;
	static char[][] map;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static Queue<Point> bombQ;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());

		map = new char[R][C];

		bombQ = new LinkedList<>();
		if (N % 2 == 0) {
			for (int r = 0; r < R; r++) {
				Arrays.fill(map[r], 'O');
			}
			print();
		} else {
			for (int r = 0; r < R; r++) {
				char[] cArr = br.readLine().toCharArray();
				for (int c = 0; c < C; c++) {
					map[r][c] = cArr[c];
					if (cArr[c] == 'O') {
						bombQ.add(new Point(r, c));
					}
				}
			}

			if (N == 1) {
				print();
			} else {
				
				bfs();
				if ((N - 3) % 4 == 0) {
					print();
				} else if ((N - 5) % 4 == 0) {
					for (int r = 0; r < R; r++) {
						for (int c = 0; c < C; c++) {
							if (map[r][c] == 'O') {
								bombQ.add(new Point(r, c));
							}
						}
					}

					bfs();
					print();
				}
			}
		}
	}

	static void bfs() {
		for (int r = 0; r < R; r++) {
			Arrays.fill(map[r], 'O');
		}
		while (!bombQ.isEmpty()) {
			Point now = bombQ.poll();
			map[now.r][now.c] = '.';

			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc)) {
					map[nr][nc] = '.';
				}
			}
		}
	}

	static void print() {
		StringBuilder sb = new StringBuilder();
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				sb.append(map[r][c]);
			}
			sb.append('\n');
		}
		System.out.println(sb.toString());
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < R) && (c >= 0) && (c < C);
	}
}
