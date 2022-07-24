package week3;

import java.util.Scanner;

public class _2567 {

	static int[] dr = new int[] { -1, 1, 0, 0 };
	static int[] dc = new int[] { 0, 0, -1, 1 };

	// 색종이2
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		boolean[][] board = new boolean[101][101];
		for (int t = 0; t < n; t++) {
			int x = sc.nextInt();
			int y = sc.nextInt();

			for (int i = x; i < x + 10; i++) {
				for (int j = y; j < y + 10; j++) {
					board[i][j] = true;
				}
			}
		}

		int answer = 0;
		for (int r = 0; r < 100; r++) {
			for (int c = 0; c < 100; c++) {
				if (board[r][c]) {
					for (int i = 0; i < 4; i++) {
						int nr = r + dr[i];
						int nc = c + dc[i];

						// 범위 이탈
						if (nr < 0 || nr > 100 || nc < 0 || nc > 100) {
							continue;
						}

						if (!board[nr][nc]) {
							answer += 1;
						}
					}
				}
			}
		}

		System.out.println(answer);
	}

}
