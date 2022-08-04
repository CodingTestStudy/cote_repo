package day0802;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//[S/W 문제해결 기본] 2일차 - Ladder1
public class SWEA_1210 {
	// 좌우
	static int[] dc = { -1, 1 };
	static String[][] board = new String[100][100];
	static boolean[][] visited = new boolean[100][100];

	static boolean checkRange(int c) {
		return c >= 0 && c < 100;
	}

	static int goToNxt(int r, int c, int nxt) {
		while (checkRange(c + nxt) && board[r][c + nxt].equals("1") && visited[r][c + nxt] == false) {
			c += nxt;
			visited[r][c] = true;
		}
		return c;
	}

	public static void main(String[] args) throws IOException, NumberFormatException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int tc = 1; tc <= 10; tc++) {

			int tt = Integer.parseInt(br.readLine());
			visited = new boolean[100][100];
			for (int r = 0; r < 100; r++) {
				String str = br.readLine();
				StringTokenizer st = new StringTokenizer(str, " ");
				for (int c = 0; c < 100; c++) {
					board[r][c] = st.nextToken();
				}
			}

			// 출발 지점 찾기
			int nr = 99;
			int nc = -1;
			for (int c = 0; c < 100; c++) {
				if (board[nr][c].equals("2")) {
					nc = c;
					break;
				}
			}

			while (nr > 0) {
				for (int i = 0; i < 2; i++) {
					visited[nr][nc] = true;
					nc = goToNxt(nr, nc, dc[i]);
				}
				nr -= 1;
			}

			int answer = nc;
			System.out.println("#" + tc + " " + answer);
		}
	}
}
