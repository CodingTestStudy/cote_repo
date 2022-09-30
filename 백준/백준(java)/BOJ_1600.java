import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

//말이 되고픈 원숭이
public class BOJ_1600 {

	static int K, R, C;
	static int answer = Integer.MAX_VALUE;
	static int[][] board;
	static boolean[][][] visited;

	static int[] mr = { -1, 1, 0, 0 };
	static int[] mc = { 0, 0, -1, 1 };
	static int[] hr = { -1, -2, -2, -1, 1, 2, 2, 1 };
	static int[] hc = { -2, -1, 1, 2, -2, -1, 1, 2 };

	static class Point {
		int r, c, k;

		Point(int r, int c, int k) {
			this.r = r;
			this.c = c;
			this.k = k;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		C = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		board = new int[R][C];
		visited = new boolean[R][C][K + 1];

		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < C; c++) {
				board[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		bfs();
		if (answer == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(answer);
		}
	}

	static void bfs() {
		Queue<Point> q = new ArrayDeque<>();
		q.add(new Point(0, 0, K));
		visited[0][0][K] = true;
		int cnt = 0;

		while (!q.isEmpty()) {
			int size = q.size();
			for (int x = 0; x < size; x++) {
				Point now = q.poll();
				int r = now.r;
				int c = now.c;
				int k = now.k;

				if (r == R - 1 && c == C - 1) {
					answer = cnt;
					return;
				}

				// 원숭이
				for (int i = 0; i < 4; i++) {
					int nr = r + mr[i];
					int nc = c + mc[i];

					if (checkRange(nr, nc) && board[nr][nc] == 0 && !visited[nr][nc][k]) {
						visited[nr][nc][k] = true;
						q.add(new Point(nr, nc, k));
					}
				}

				// 말
				if (k > 0) {
					for (int i = 0; i < 8; i++) {
						int nr = r + hr[i];
						int nc = c + hc[i];

						if (checkRange(nr, nc) && board[nr][nc] == 0 && !visited[nr][nc][k - 1]) {
							visited[nr][nc][k - 1] = true;
							q.add(new Point(nr, nc, k - 1));
						}
					}
				}

			}
			cnt++;
		}
	}

	static boolean checkRange(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}
}
