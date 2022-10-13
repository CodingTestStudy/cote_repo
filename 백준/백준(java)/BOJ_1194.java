import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 달이 차오른다, 가자
public class BOJ_1194 {
	static int R, C;
	static char[][] map;
	static boolean[][][] visited;
	static Queue<Point> q;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Point {
		int r, c, key;

		public Point(int r, int c, int key) {
			super();
			this.r = r;
			this.c = c;
			this.key = key;
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R][];
		q = new LinkedList<>();
		visited = new boolean[R][C][1 << 6]; // 000000:0 ~ 111111:63 까지 사용 가능한 배열 크기

		for (int r = 0; r < R; r++) {
			map[r] = br.readLine().toCharArray();
			for (int c = 0; c < C; c++) {
				if (map[r][c] == '0') {
					map[r][c] = '.'; // 나중에 원숭이가 열쇠들고 출발점 다시 지나가는 경우 존재하므로
					visited[r][c][0] = true;
					q.add(new Point(r, c, 0)); // 출발점 좌표 큐에 추가
				}
			}
		}

		System.out.println(bfs());
	}

	static int bfs() {
		int dist = 0;
		while (!q.isEmpty()) {
			int size = q.size();

			for (int x = 0; x < size; x++) {
				Point now = q.poll();
				if (map[now.r][now.c] == '1') {
					return dist;
				}

				for (int i = 0; i < 4; i++) {
					int nr = now.r + dr[i];
					int nc = now.c + dc[i];

					// 범위 이탈 || 벽 || 해당 키로 방문 여부
					if (!checkRange(nr, nc) || map[nr][nc] == '#' || visited[nr][nc][now.key])
						continue;

					/**
					 * 열쇠(a~f), 문(A~F), 평지(.), 탈출구(1)
					 */

					if (map[nr][nc] >= 'a' && map[nr][nc] <= 'f') {
						int newKey = 1 << ((map[nr][nc]) - 'a');
						int addedKey = now.key | newKey;
						q.add(new Point(nr, nc, addedKey));
						visited[nr][nc][addedKey] = true;
					} else if (map[nr][nc] >= 'A' && map[nr][nc] <= 'F') {
						int door = 1 << (map[nr][nc] - 'A'); // 문 A=0, B=1, C=1, ... 숫자로 만들고 << 연산
						if ((now.key & door) > 0) { // 열쇠를 갖고 있는지 확인
							q.add(new Point(nr, nc, now.key));
							visited[nr][nc][now.key] = true;
						}
					} else {
						q.add(new Point(nr, nc, now.key));
						visited[nr][nc][now.key] = true;
					}
				}
			}
			dist++;
		}

		return -1;
	}

	static boolean checkRange(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}
}
