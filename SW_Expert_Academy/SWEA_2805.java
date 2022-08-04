package day0802;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 농작물 수확하기
public class SWEA_2805 {

	static int t;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {
			int answer = 0;
			int n = Integer.parseInt(br.readLine());
			int[][] board = new int[n][n];
			for (int r = 0; r < n; r++) {
				char[] ch = br.readLine().toCharArray();

				for (int c = 0; c < n; c++) {
					board[r][c] = ch[c] - '0';
				}
			}

			int idx = n / 2;
			for (int r = 0; r < n; r++) {
				answer += board[r][idx];
			}

			int nxt = 1;
			while (idx + nxt < n) {
				for (int r = nxt; r < n - nxt; r++) {
					answer += board[r][idx - nxt] + board[r][idx + nxt];
				}
				nxt++;
			}

			System.out.println("#" + tc + " " + answer);
		}

	}
}
