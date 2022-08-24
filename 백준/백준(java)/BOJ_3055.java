package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

// 탈출
public class BOJ_3055 {

	static int R, C, answer;
	static char[][] map;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Point {
		int r, c, time;

		Point(int r, int c, int time) {
			this.r = r;
			this.c = c;
			this.time = time;
		}
	}

	static char ground = '.';
	static char water = '*';
	static char block = 'X';
	static Point start, end;
	static Queue<Point> waterQ = new ArrayDeque<>();
	static Queue<Point> moveQ = new ArrayDeque<>();
	static boolean[][] visited;

	static ArrayList<char[][]> simulMap = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R][C];
		visited = new boolean[R][C];

		for (int r = 0; r < R; r++) {
			map[r] = br.readLine().toCharArray();
			for (int c = 0; c < C; c++) {
				if (map[r][c] == 'D') {
					end = new Point(r, c, 0);
				} else if (map[r][c] == 'S') {
					moveQ.add(new Point(r, c, 0));
					visited[r][c] = true;
				} else if (map[r][c] == water) {
					waterQ.add(new Point(r, c, 0));
					visited[r][c] = true;
				}
			}
		}

		while (!moveQ.isEmpty() && answer == 0) {
			bfs();
		}
		if (answer == 0) {
			System.out.println("KAKTUS");
		} else {
			System.out.println(answer);
		}

	}

	static void bfs() {
		int waterSize = waterQ.size();
		for (int x = 0; x < waterSize; x++) {
			Point now = waterQ.poll();
			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc)) {
					if (map[nr][nc] == '.' && !visited[nr][nc]) {
						map[nr][nc] = water;
						visited[nr][nc] = true;
						waterQ.add(new Point(nr, nc, 0));
					}
				}
			}
		}

		int moveSize = moveQ.size();
		for (int x = 0; x < moveSize; x++) {
			Point now = moveQ.poll();
			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc)) {
					if (nr == end.r && nc == end.c) {
						answer = now.time + 1;
						return;
					}

					if (map[nr][nc] == '.' && !visited[nr][nc]) {
						map[nr][nc] = '@';
						visited[nr][nc] = true;
						moveQ.add(new Point(nr, nc, now.time + 1));
					}
				}
			}
		}

	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < R) && (c >= 0) && (c < C);
	}

	static void print(char[][] map) {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				System.out.print(map[r][c]);
			}
			System.out.println();
		}
		System.out.println();
	}
}
