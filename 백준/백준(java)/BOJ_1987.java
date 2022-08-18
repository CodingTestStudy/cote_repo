package day0818;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 알파벳 (DFS)
public class BOJ_1987 {

	static int R, C;
	static char[][] map;
	static boolean[][] visited;

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static int answer;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R + 1][C + 1];
		visited = new boolean[R + 1][C + 1];

		for (int r = 1; r <= R; r++) {
			String temp = br.readLine();
			for (int c = 1; c <= C; c++) {
				map[r][c] = temp.charAt(c - 1);
			}
		}

		answer = 1;
		dfs(1, 1, String.valueOf(map[1][1]));
		System.out.println(answer);
	}

	static void dfs(int r, int c, String alphabet) {
		visited[r][c] = true;
		answer = Math.max(answer, alphabet.length());

		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (!checkRange(nr, nc) || visited[nr][nc])
				continue;

			if (checkAlpha(alphabet, map[nr][nc])) {
				continue;
			}
			dfs(nr, nc, alphabet.concat(String.valueOf(map[nr][nc])));
			visited[nr][nc] = false;
		}
	}

	static boolean checkRange(int r, int c) {
		return (r >= 1) && (r <= R) && (c >= 1) && (c <= C);
	}

	static boolean checkAlpha(String alpha, char temp) {
		for (int i = 0; i < alpha.length(); i++) {
			if (alpha.charAt(i) == temp) {
				return true;
			}
		}
		return false;
	}
}
