package day0803;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 오목 판정
public class SWEA_11315 {

	static int t, n;
	static char[][] board;
	static int[] dr = { -1, 1, 0, 0, -1, -1, 1, 1 };
	static int[] dc = { 0, 0, -1, 1, -1, 1, -1, 1 };

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (c >= 0) && (r < n) && (c < n);
	}

	static boolean check(int r, int c) {
		for (int i = 0; i < 8; i++) {
			int result = 1;
			int rr = r;
			int cc = c;
			while (checkRange(rr + dr[i], cc + dc[i])) {
				if (board[rr + dr[i]][cc + dc[i]] == 'o') {
					rr += dr[i];
					cc += dc[i];
					result++;
				}else {
					break;
				}
			}
			if (result >= 5) {				
				return true;
			}
		}

		return false;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			board = new char[n][n];

			for (int r = 0; r < n; r++) {
				String str = br.readLine();
				for (int c = 0; c < n; c++) {
					board[r][c] = str.charAt(c);
				}
			}
			String answer = "NO";
			for (int r = 0; r < n; r++) {
				for (int c = 0; c < n; c++) {
					if (board[r][c] == 'o') {
						if (check(r, c)) {
							answer = "YES";
							break;
						}
					}
				}
			}

			System.out.println("#" + tc + " " + answer);
		}

	}

}

