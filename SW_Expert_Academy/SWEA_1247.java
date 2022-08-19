package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// [S/W 문제해결 응용] 3일차 - 최적 경로
public class SWEA_1247 {

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static int t, n, answer;

	static int[] cards;
	static int[] result;
	static boolean[] used;

	static Point office, home;
	static Point[] points;

	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			cards = new int[n];
			result = new int[n];
			used = new boolean[n];
			for (int i = 0; i < n; i++) {
				cards[i] = i;
			}

			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			office = new Point(y, x);
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			home = new Point(y, x);

			points = new Point[n];
			for (int i = 0; i < n; i++) {
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				points[i] = new Point(y, x);
			}
			answer = Integer.MAX_VALUE;

			perm(0);

			sb.append("#").append(tc + " ").append(answer).append('\n');
		}
		System.out.println(sb.toString());
	}

	static void perm(int idx) {

		if (idx == n) {
			calc(result);
			return;
		}

		for (int i = 0; i < n; i++) {
			if (used[i])
				continue;

			result[idx] = cards[i];
			used[i] = true;
			perm(idx + 1);
			used[i] = false;
		}
	}

	static void calc(int[] result) {
		int dist = calcDist(office, points[result[0]]);
		for (int i = 1; i < n; i++) {
			dist += calcDist(points[result[i - 1]], points[result[i]]);
		}
		dist += calcDist(points[result[n - 1]], home);

		answer = Math.min(answer, dist);
	}

	static int calcDist(Point p1, Point p2) {
		return Math.abs(p1.r - p2.r) + Math.abs(p1.c - p2.c);
	}
}
