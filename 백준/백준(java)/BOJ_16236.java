package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

// 아기 상어
public class BOJ_16236 {

	static int N, answer;
	static int[][] map;
	// 상좌우하
	static int[] dr = { -1, 0, 0, 1 };
	static int[] dc = { 0, -1, 1, 0 };

	static class Point {
		int r, c, size;

		Point(int r, int c, int size) {
			this.r = r;
			this.c = c;
			this.size = size;
		}
	}

	static class Fish implements Comparable<Fish> {
		int r, c;

		Fish(int r, int c) {
			this.r = r;
			this.c = c;
		}

		@Override
		public int compareTo(Fish o) {

			return this.r != o.r ? this.r - o.r : this.c - o.c;
		}
	}


	static Point shark;
	static int eat;
	static Queue<Point> fishQ = new ArrayDeque<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		for (int r = 0; r < N; r++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < N; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());

				if (map[r][c] == 9) {
					shark = new Point(r, c, 2);
				}

				if (map[r][c] != 0 && map[r][c] != 9) {
					fishQ.add(new Point(r, c, map[r][c]));
				}
			}
		}

		while (findFish()) {
		}
		System.out.println(answer);

	}

	// BFS
	static boolean findFish() {
		boolean[][] visited = new boolean[N][N];
		Queue<Point> q = new ArrayDeque<>();
		q.add(new Point(shark.r, shark.c, shark.size));

		PriorityQueue<Fish> pq = new PriorityQueue<>();

		int dist = 0;
		while (!q.isEmpty()) {
			int qSize = q.size();
			dist++;
			for (int x = 0; x < qSize; x++) {
				Point now = q.poll();
				for (int i = 0; i < 4; i++) {
					int nr = now.r + dr[i];
					int nc = now.c + dc[i];

					if (checkRange(nr, nc)) {
						// 물고기 찾은 경우
						if (map[nr][nc] != 0 && map[nr][nc] < shark.size) {
							pq.add(new Fish(nr, nc));
						} else if ((map[nr][nc] == 0 || map[nr][nc] == shark.size) && !visited[nr][nc]) {

							visited[nr][nc] = true;
							q.add(new Point(nr, nc, now.size));
						}

					}
				}

			}
			if (!pq.isEmpty()) {
				Fish fish = pq.poll();
				eatFish(new Point(fish.r, fish.c, map[fish.r][fish.c]));
				answer += dist;
				return true;
			}
		}

		return false;
	}

	static void eatFish(Point fish) {
		map[shark.r][shark.c] = 0;
		shark.r = fish.r;
		shark.c = fish.c;
		map[fish.r][fish.c] = 0;
		eat += 1;
		if (eat == shark.size) {
			eat = 0;
			shark.size += 1;
		}
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < N) && (c >= 0) && (c < N);
	}

	static void print() {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (r == shark.r && c == shark.c) {
					System.out.print("X ");
				} else {

					System.out.print(map[r][c] + " ");
				}
			}
			System.out.println();
		}
	}
}
