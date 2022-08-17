package day0817;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 쿼드트리
public class BOJ_1992 {

	static int n;
	static int white = 0;
	static int black = 1;
	static StringBuilder sb = new StringBuilder();
	static int[][] map;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];

		for (int r = 0; r < n; r++) {
			char[] cArr = br.readLine().toCharArray();
			for (int c = 0; c < n; c++) {
				map[r][c] = cArr[c] - '0';
			}
		}

		find(0, 0, n);
		System.out.println(sb.toString());
	}

	static void find(int r, int c, int len) {
		if (checkColor(r, c, r + len, c + len)) {
			sb.append((map[r][c] == 1) ? black : white);
			return;
		}
		len /= 2;
		sb.append("(");
		find(r, c, len);
		find(r, c + len, len);
		find(r + len, c, len);
		find(r + len, c + len, len);
		sb.append(")");
	}

	static boolean checkColor(int sr, int sc, int er, int ec) {
		int color = map[sr][sc];
		for (int r = sr; r < er; r++) {
			for (int c = sc; c < ec; c++) {
				if (map[r][c] != color) {
					return false;
				}
			}
		}
		return true;
	}
}
