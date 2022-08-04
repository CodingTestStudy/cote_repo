package day0802;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 달팽이 숫자
public class SWEA_1954 {
	static int[] dr = { 0, -1, 0, 1 };
	static int[] dc = { 1, 0, -1, 0 };

	static int n;
	static int[][] snail;
	static boolean[][] visited;

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < n) && (c >= 0) && (c < n);
	}

	static int[] move(int r, int c, int dr, int dc, int value) {
		while (checkRange(r + dr, c + dc) && !visited[r + dr][c + dc]) {
			r += dr;
			c += dc;
			++value;
			visited[r][c] = true;
			snail[r][c] = value;
		}
		return new int[] { r, c, value };
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {
			n = Integer.parseInt(br.readLine());
			snail = new int[n][n];
			visited = new boolean[n][n];

			int[] now = new int[2];
			now[0] = 0;
			now[1] = -1;
			int value = 0;

			while (true) {
				int failCnt = 0;
				for (int i = 0; i < 4; i++) {
					int temp = value;
					int[] nxt = move(now[0], now[1], dr[i], dc[i], value);
					now[0] = nxt[0];
					now[1] = nxt[1];
					value = nxt[2];
					if (temp == value) {
						failCnt++;
					}
				}
				if (failCnt == 4) {
					break;
				}
			}

			System.out.println("#" + tc);
			for (int r = 0; r < n; r++) {
				for (int c = 0; c < n; c++) {
					System.out.print(snail[r][c] + " ");
				}
				System.out.println();
			}
		}

	}
}
