package week12;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

// 새로운 게임 2
public class BOJ_17837 {
	static int N, K, ans;
	static int[] dr = { 0, 0, 0, -1, 1 };
	static int[] dc = { 0, 1, -1, 0, 0 };

	static int[][] map;
	static Deque<Integer>[][] qMap;

	static class Point {
		int r, c, d;

		Point(int r, int c, int d) {
			this.r = r;
			this.c = c;
			this.d = d;
		}
	}

	static Point[] horses;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		map = new int[N][N];
		horses = new Point[K];
		qMap = new ArrayDeque[N][N];

		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < N; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			horses[i] = new Point(r, c, d);
			qMap[r][c].add(i);
		}

		for (int x = 0; x < 10001; x++) {
			ans++;
			for (int i = 0; i < K; i++) {
				move(i);
				if (isSuccess(horses[i].r, horses[i].c)) {
					System.out.println(ans);
					return;
				}
			}
		}
		System.out.println(-1);
	}

	static void move(int idx) {
		int r = horses[idx].r;
		int c = horses[idx].c;
		Deque<Integer> q = qMap[r][c];
		Deque<Integer> remainQ = new ArrayDeque<>();
		Deque<Integer> moveQ = new ArrayDeque<>();

		boolean flag = false;
		while (!q.isEmpty()) {
			int target = q.poll();
			if (target == idx) {
				flag = true;
			}

			if (!flag) {
				remainQ.add(target);
			} else {
				moveQ.add(target);
			}
		}
		qMap[r][c] = remainQ;

		int nr = r + horses[idx].d;
		int nc = c + horses[idx].d;

		// blue
		if (!checkRange(nr, nc) || map[nr][nc] == 2) {

		}
		// red
		else if (map[nr][nc] == 1) {
			while (!moveQ.isEmpty()) {
				int target = moveQ.pollLast();
				qMap[nr][nc].add(target);
			}
		}
		// white
		else {
			while (!moveQ.isEmpty()) {
				int target = moveQ.pollFirst();
				qMap[nr][nc].add(target);
			}
		}

	}

	static boolean isSuccess(int r, int c) {
		if (qMap[r][c].size() == 4) {
			return true;
		}
		return false;
	}

	static boolean checkRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}

}
