import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

// 다리 만들기 2
public class BOJ_17472 {
	static int N, M, num;
	static int[][] map;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static boolean[][] visited;
	static ArrayList<ArrayList<Point>> list = new ArrayList<>();

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static class Data implements Comparable<Data> {

		int from, to, dist;

		Data(int from, int to, int dist) {
			this.from = from;
			this.to = to;
			this.dist = dist;
		}

		@Override
		public int compareTo(Data o) {
			return this.dist - o.dist;
		}
	}

	static class Node {
		Set<Integer> set = new HashSet<>();
	}

	static Node[] nodeList;

	static PriorityQueue<Data> pq = new PriorityQueue<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		map = new int[N][M];
		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < M; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		list.add(new ArrayList<>());
		num = 0;
		visited = new boolean[N][M];
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (!visited[r][c] && map[r][c] == 1) {
					insertNumber(r, c, ++num);
				}
			}
		}

		nodeList = new Node[num + 1];

		for (int i = 1; i <= num; i++) {
			nodeList[i] = new Node();
			insertDistance(i);
		}

		int ans = 0;
		while (!pq.isEmpty()) {
			// 모두 연결되어 있는지 확인
			if (isConnected()) {
				break;
			}

			Data data = pq.poll();
			int f = data.from;
			int t = data.to;

			if (!isConnected(f, t)) {
				ans += data.dist;
				nodeList[f].set.add(t);
				nodeList[t].set.add(f);
			}

		}
//		print();

		if (!isConnected() || ans == 0) {
			System.out.println(-1);
		} else {
			System.out.println(ans);
		}
	}

	static boolean isConnected(int f, int t) {
		Queue<Integer> q = new ArrayDeque<>();
		q.add(f);
		boolean[] v = new boolean[num + 1];
		v[f] = true;
		while (!q.isEmpty()) {
			int now = q.poll();
			for (int target : nodeList[now].set) {
				if (target == t) {
					return true;
				}

				if (!v[target]) {
					q.add(target);
					v[target] = true;
				}
			}
		}

		return false;

	}

	static boolean isConnected() {
		Queue<Integer> q = new ArrayDeque<>();
		q.add(1);
		boolean[] v = new boolean[num + 1];
		v[1] = true;
		while (!q.isEmpty()) {
			int now = q.poll();
			for (int target : nodeList[now].set) {
				if (!v[target]) {
					q.add(target);
					v[target] = true;
				}
			}
		}

		for (int i = 1; i <= num; i++) {
			if (!v[i]) {
				return false;
			}
		}
		return true;
	}

	static void insertDistance(int from) {
		List<Point> temp = list.get(from);
		for (Point p : temp) {
			int nr = p.r, nc = p.c;
			for (int i = 0; i < 4; i++) {
				int dist = 0;
				int to = -1;
				nr += dr[i];
				nc += dc[i];

				while (true) {
					if (!checkRange(nr, nc) || map[nr][nc] == from) {
						break;
					}
					if (map[nr][nc] != 0) {
						to = map[nr][nc];
						break;
					}
					nr += dr[i];
					nc += dc[i];
					dist++;
				}

				if (dist != 1 && to != -1) {
					pq.add(new Data(Math.min(from, to), Math.max(from, to), dist));
				}

			}
		}
	}

	static void insertNumber(int startR, int startC, int num) {
		Queue<Point> q = new ArrayDeque<>();
		q.add(new Point(startR, startC));
		visited[startR][startC] = true;
		map[startR][startC] = num;
		list.add(new ArrayList<>());
		list.get(list.size() - 1).add(new Point(startR, startC));
		while (!q.isEmpty()) {
			Point now = q.poll();

			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (checkRange(nr, nc) && !visited[nr][nc]) {
					visited[nr][nc] = true;
					if (map[nr][nc] == 1) {
						map[nr][nc] = num;
						q.add(new Point(nr, nc));
						list.get(list.size() - 1).add(new Point(nr, nc));

					}
				}
			}
		}

	}

	static boolean checkRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M;
	}

	static void print() {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				System.out.print(map[r][c] + " ");
			}
			System.out.println();
		}
	}
}
