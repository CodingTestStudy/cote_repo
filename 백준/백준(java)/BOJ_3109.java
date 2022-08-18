package day0818;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 빵집
public class BOJ_3109 {

	static int R, C, answer;
	static char[][] map;
	static int[] dr = { -1, 0, 1 };

	static char load = '.';
	static char pipe = '!';
	static char wall = 'x';

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R][C];

		for (int r = 0; r < R; r++) {
			char[] arr = br.readLine().toCharArray();
			for (int c = 0; c < C; c++) {
				map[r] = arr;
			}
		}

		for (int r = 0; r < R; r++) {
			if (dfs(r, 0)) {
				answer++;
			}
		}
		System.out.println(answer);

	}

	static boolean dfs(int r, int c) {

		if (c == C - 1) {
			return true;
		}

		for (int i = 0; i < 3; i++) {
			int nr = r + dr[i];
			int nc = c + 1;

			if (checkRange(nr, nc) && map[nr][nc] == load) {
				map[nr][nc] = pipe;
				if (dfs(nr, nc)) {
					return true;
				}
			}
		}

		return false;
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < R) && (c >= 0) && (c < C);
	}

	static void print() {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				System.out.print(map[r][c]);
			}
			System.out.println();
		}
	}
}
