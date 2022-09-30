import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

// 보급로
public class SWEA_1249 {

	static int T, N, answer;
	static int[][] map;
	static int[][] visited;
	static int INF = Integer.MAX_VALUE;

	static StringBuilder sb = new StringBuilder();
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Point implements Comparable<Point> {
		int r, c, cost;

		Point(int r, int c, int cost) {
			this.r = r;
			this.c = c;
			this.cost = cost;
		}

		@Override
		public int compareTo(Point o) {
			return this.cost - o.cost;
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			visited = new int[N][N];
			for (int i = 0; i < N; i++) {
				Arrays.fill(visited[i], INF);
			}

			for (int r = 0; r < N; r++) {
				char[] cArr = br.readLine().toCharArray();
				for (int c = 0; c < N; c++) {
					map[r][c] = cArr[c] - '0';
				}
			}

			dijkstra();

			sb.append("#" + tc + " " + answer + "\n");
		}
		System.out.println(sb.toString());
	}

	static void dijkstra() {
		visited[0][0] = map[0][0];
		PriorityQueue<Point> pq = new PriorityQueue<>();
		pq.add(new Point(0, 0, map[0][0]));

		while (!pq.isEmpty()) {
			Point now = pq.poll();

			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];
				
				if (checkRange(nr, nc)) {
					if (visited[nr][nc] > visited[now.r][now.c] + map[nr][nc]) {
						visited[nr][nc] = visited[now.r][now.c] + map[nr][nc];
						pq.add(new Point(nr, nc, visited[nr][nc]));
					}
				}
			}
		}

		answer = visited[N - 1][N - 1];
	}

	static void print() {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				System.out.print(visited[r][c] + " ");
			}
			System.out.println();
		}
	}

	static boolean checkRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}
}
