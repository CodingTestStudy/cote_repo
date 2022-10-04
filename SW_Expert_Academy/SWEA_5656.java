import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// 벽돌 깨기
public class SWEA_5656 {
	static int T, N, R, C, ans;
	static int board[][];
	static int[] result;
	static List<int[]> list;
	static StringBuilder sb = new StringBuilder();

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Point {
		int r, c, value;

		Point() {
		};

		Point(int r, int c, int value) {
			this.r = r;
			this.c = c;
			this.value = value;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());
			R = Integer.parseInt(st.nextToken());
			ans = Integer.MAX_VALUE;

			board = new int[R][C];
			result = new int[N];
			list = new ArrayList<>();
			for (int r = 0; r < R; r++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int c = 0; c < C; c++) {
					board[r][c] = Integer.parseInt(st.nextToken());
				}
			}

			perm(0);

			for (int[] temp : list) {
				int[][] copy = deepCopy(board);
				for (int i : temp) {
					copy = remove(copy, i);
				}

				ans = Math.min(ans, count(copy));
				if (ans == 0) {
					break;
				}
			}

			sb.append("#" + tc + " " + ans + "\n");
		}
		System.out.println(sb.toString());
	}

	static void perm(int cnt) {
		if (cnt == N) {
			int[] temp = new int[N];
			for (int i = 0; i < N; i++) {
				temp[i] = result[i];
			}
			list.add(temp);
			return;
		}

		for (int i = 0; i < C; i++) {
			result[cnt] = i;
			perm(cnt + 1);
		}
	}

	static int[][] remove(int[][] arr, int idx) {
		Point p = new Point();
		for (int r = 0; r < R; r++) {
			if (arr[r][idx] != 0) {
				p.r = r;
				p.c = idx;
				p.value = arr[r][idx];
				break;
			}
		}

		Queue<Point> q = new ArrayDeque<>();
		q.add(p);
		while (!q.isEmpty()) {
			Point now = q.poll();
			int repeat = now.value;

			for (int i = 0; i < 4; i++) {
				int nr = now.r;
				int nc = now.c;

				for (int j = 0; j < repeat - 1; j++) {
					nr += dr[i];
					nc += dc[i];
					// 범위 이탈
					if (!checkRange(nr, nc)) {
						break;
					}

					if (arr[nr][nc] == 1) {
						arr[nr][nc] = 0;
					} else if (!(nr == now.r && nc == now.c) && arr[nr][nc] != 0) {
						q.add(new Point(nr, nc, arr[nr][nc]));
					}

				}
			}
			arr[now.r][now.c] = 0;
		}

		Queue<Point> newQ = new ArrayDeque<>();
		for (int c = 0; c < C; c++) {
			for (int r = R - 1; r >= 0; r--) {
				if (arr[r][c] != 0) {
					newQ.add(new Point(r, c, arr[r][c]));
					arr[r][c] = 0;
				}
			}

			int rr = R - 1;
			while (!newQ.isEmpty()) {
				Point temp = newQ.poll();
				arr[rr][c] = temp.value;
				rr--;
			}

		}

		return arr;
	}

	static int[][] deepCopy(int[][] arr) {
		int[][] copy = new int[R][C];
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				copy[r][c] = arr[r][c];
			}
		}
		return copy;
	}

	static int count(int[][] arr) {
		int cnt = 0;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (arr[r][c] != 0) {
					cnt++;
				}
			}
		}
		return cnt;
	}

	static void print(int[][] arr) {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				System.out.print(arr[r][c] + " ");
			}
			System.out.println();
		}
	}

	static boolean checkRange(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}
}
