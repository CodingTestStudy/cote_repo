import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

// 치즈
public class BOJ_2636 {

	static int R, C, ans;
	static int[][] board;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

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
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new int[R][C];
		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < C; c++) {
				board[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		if (calc() == R * C) {
			System.out.println(0);
			System.out.println(R * C);
			return;
		}

		int time = 0;
		while (true) {
			int result = calc();
			if (result == 0) {
				break;
			}
			
			ans = result;

			bfs();
			time++;

		}

		System.out.println(time);
		System.out.println(ans);

	}

	static void bfs() {
		Queue<Point> q = new ArrayDeque<>();
		q.add(new Point(0, 0));
		boolean[][] visited = new boolean[R][C];
		visited[0][0] = true;

		while (!q.isEmpty()) {
			Point now = q.poll();

			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc) && !visited[nr][nc]) {
					visited[nr][nc] = true;

					if (board[nr][nc] == 1) {
						board[nr][nc] = 9;
					} else {
						q.add(new Point(nr, nc));
					}
				}
			}
		}
	}

	static int calc() {
		int cnt = 0;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (board[r][c] == 9) {
					board[r][c] = 0;
				}

				if (board[r][c] == 1) {
					cnt++;
				}
			}
		}
		return cnt;
	}

	static boolean checkRange(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}
}
