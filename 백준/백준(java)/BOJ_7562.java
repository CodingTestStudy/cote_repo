package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 나이트의 이동
public class BOJ_7562 {

	static int l, answer;
	static int[][] map;
	static int[] dr = { -1, -2, -2, -1, 1, 2, 2, 1 };
	static int[] dc = { -2, -1, 1, 2, -2, -1, 1, 2 };

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine());

		for (int tc = 0; tc < t; tc++) {
			l = Integer.parseInt(br.readLine());
			map = new int[l][l];
			StringTokenizer st = new StringTokenizer(br.readLine());
			Point start = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			st = new StringTokenizer(br.readLine());
			Point end = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

			if (start.r == end.r && start.c == end.c) {
				sb.append(0).append('\n');
			} else {
				bfs(start, end);
				sb.append(answer).append('\n');
			}
		}
		System.out.println(sb.toString());
	}

	static void bfs(Point start, Point end) {
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(start.r, start.c));
		map[start.r][start.c] = 1;
		int cnt = 0;

		while (!q.isEmpty()) {
			cnt++;
			int qSize = q.size();
			for (int x = 0; x < qSize; x++) {

				Point target = q.poll();

				for (int i = 0; i < 8; i++) {
					int nr = target.r + dr[i];
					int nc = target.c + dc[i];

					if (checkRange(nr, nc) && map[nr][nc] == 0) {
						map[nr][nc] = cnt;
						q.add(new Point(nr, nc));

						if (nr == end.r && nc == end.c) {
							answer = cnt;
							return;
						}
					}
				}
			}
		}
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < l) && (c >= 0) && (c < l);
	}
}
