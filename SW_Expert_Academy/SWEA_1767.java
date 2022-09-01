import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class SWEA_1767 {

	static int N, answer;
	static int[][] map;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static List<Point> list;
	static StringBuilder sb = new StringBuilder();

	static int[] cards;
	static boolean[] selected;
	static PriorityQueue<Core> pq;

	static class Core implements Comparable<Core> {
		int cnt, dist;

		Core(int cnt, int dist) {
			this.cnt = cnt;
			this.dist = dist;
		}

		@Override
		public int compareTo(Core o) {
			return (this.cnt != o.cnt) ? (o.cnt - this.cnt) : (this.dist - o.dist);
		}
	}

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			list = new ArrayList<>();
			answer = Integer.MAX_VALUE;
			pq = new PriorityQueue<>();
			for (int r = 0; r < N; r++) {
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				for (int c = 0; c < N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());

					if (map[r][c] == 1) {
						map[r][c] = 9;
						if (!isConnected(r, c)) {
							list.add(new Point(r, c));
						}
					}
				}
			}

			cards = new int[list.size()];
			for (int i = 0; i < list.size(); i++) {
				cards[i] = i + 1;
			}
			selected = new boolean[list.size()];
			subset(0);
			answer = pq.poll().dist;
			sb.append("#" + tc + " " + answer + '\n');
		}
		System.out.println(sb.toString());
	}

	static void dfs(int idx, int[] temp, boolean[][] visited) {
		if (idx == temp.length) {
			int dist = calc(visited);
			pq.add(new Core(idx, dist));
			return;
		}

		Point p = list.get(temp[idx]);
		int r = p.r;
		int c = p.c;
		for (int i = 0; i < 4; i++) {
			boolean flag = true;
			r = p.r;
			c = p.c;
			while (checkRange(r + dr[i], c + dc[i])) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				if (visited[nr][nc] || map[nr][nc] != 0) {
					flag = false;
					break;
				}
				r = nr;
				c = nc;
			}

			if (flag) {
				r = p.r;
				c = p.c;
				while (checkRange(r + dr[i], c + dc[i])) {
					int nr = r + dr[i];
					int nc = c + dc[i];
					visited[nr][nc] = true;
					r = nr;
					c = nc;
				}
				dfs(idx + 1, temp, visited);
				r = p.r;
				c = p.c;
				while (checkRange(r + dr[i], c + dc[i])) {
					int nr = r + dr[i];
					int nc = c + dc[i];
					visited[nr][nc] = false;
					r = nr;
					c = nc;
				}

			}
		}
	}

	static void subset(int idx) {
		if (idx == list.size()) {
			int cnt = 0;
			boolean[][] visited = new boolean[N][N];
			for (int i = 0; i < list.size(); i++) {
				if (selected[i]) {
					cnt++;
				}
			}

			int x = 0;
			int temp[] = new int[cnt];
			for (int i = 0; i < list.size(); i++) {
				if (selected[i]) {
					temp[x++] = i;
				}
			}
			dfs(0, temp, visited);
			return;
		}

		selected[idx] = true;
		subset(idx + 1);
		selected[idx] = false;
		subset(idx + 1);

	}	

	static int calc(boolean[][] visited) {
		int dist = 0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (visited[r][c]) {
					dist++;
				}
			}
		}
		return dist;
	}

	static boolean isConnected(int r, int c) {
		for (int i = 0; i < 4; i++) {
			if (!checkRange(r + dr[i], c + dc[i]))
				return true;
		}
		return false;
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < N) && (c >= 0) && (c < N);
	}
}
