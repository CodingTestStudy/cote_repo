package day0812;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 치킨 배달
public class BOJ_15686 {
	static int n, m;
	static int[][] map;

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static int home = 1;
	static int chicken = 2;

	static boolean[] select;
	static ArrayList<Point> homeList = new ArrayList<>(); // 집 좌표 저장 리스트
	static ArrayList<Point> chickenList = new ArrayList<>(); // 치킨 좌표 저장 리스트

	static ArrayList<Point[]> list = new ArrayList<>(); // 조합 리스트

	// 좌표 클래스
	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(st.nextToken()); // 배열 크기
		m = Integer.parseInt(st.nextToken()); // 치킨집 뽑는 개수
		map = new int[n][n];

		for (int r = 0; r < n; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < n; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
				if (map[r][c] == home) {
					homeList.add(new Point(r, c));
				}
				if (map[r][c] == chicken) {
					chickenList.add(new Point(r, c));
				}
			}
		}

		select = new boolean[chickenList.size()];
		comb(0, 0); // m개의 치킨집 좌표 조합
		int answer = Integer.MAX_VALUE;
		// 치킨 집 m개 경우의 수
		for (int i = 0; i < list.size(); i++) {
			// i 번째 경우의 수
			Point[] temp = list.get(i);
			answer = Math.min(answer, mCalc(temp));

		}

		System.out.println(answer);
	}

	// 해당 m개의 조합 좌표에서 치킨거리 계산
	static int mCalc(Point[] chikens) {

		int result = 0;
		// 모든 집에서 치킨거리 계산
		for (int i = 0; i < homeList.size(); i++) {
			Point home = homeList.get(i);
			int temp = Integer.MAX_VALUE;
			for (Point chicken : chikens) {
				temp = Math.min(calcDistance(home.r, home.c, chicken.r, chicken.c), temp);
			}
			result += temp;
		}

		return result;
	}

	static void comb(int idx, int cnt) {
		if (cnt == m) {
			Point[] points = new Point[m];
			int pIdx = 0;
			for (int i = 0; i < chickenList.size(); i++) {
				if (select[i]) {
					points[pIdx++] = chickenList.get(i);
				}
			}
			list.add(points);
			return;
		}

		if (idx == chickenList.size()) {
			return;
		}

		select[idx] = true;
		comb(idx + 1, cnt + 1);
		select[idx] = false;
		comb(idx + 1, cnt);
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < n) && (c >= 0) && (c < n);
	}

	static int calcDistance(int r1, int c1, int r2, int c2) {
		return Math.abs(r1 - r2) + Math.abs(c1 - c2);
	}

}
