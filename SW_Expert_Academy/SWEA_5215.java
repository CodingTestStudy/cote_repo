package day0811;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//햄버거 다이어트
public class SWEA_5215 {

	static int n, l;
	static int[] scores, calories;
	static int answer;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int tt = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= tt; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			n = Integer.parseInt(st.nextToken()); // 재료 개수
			l = Integer.parseInt(st.nextToken()); // 제한 칼로리

			scores = new int[n];
			calories = new int[n];
			answer = 0;

			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int t = Integer.parseInt(st.nextToken());
				int k = Integer.parseInt(st.nextToken());
				scores[i] = t;
				calories[i] = k;
			}

			calc(0, 0, 0);
			System.out.println("#" + tc + " " + answer);
		}
	}

	static void calc(int idx, int sumT, int sumK) {
		if (sumK > l) {
			return;
		}
		if (idx == n) {
			answer = Math.max(answer, sumT);
			return;
		}

		calc(idx + 1, sumT + scores[idx], sumK + calories[idx]); // idx 햄버거 포함 ver
		calc(idx + 1, sumT, sumK); // idx 햄버거 미포함 ver
	}
}
