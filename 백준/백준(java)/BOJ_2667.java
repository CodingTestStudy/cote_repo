package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;

//단지번호붙이기(DFS)
public class BOJ_2667 {

	static int n;
	static char[][] map;
	static List<Integer> list = new ArrayList<Integer>();
	static int maxValue = 26;

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new char[n][];

		for (int r = 0; r < n; r++) {
			map[r] = br.readLine().toCharArray();
		}

		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				if (map[r][c] == '1') {
					dfs(r, c);
					list.add(result);
					result = 0;
				}
			}
		}
		
		Collections.sort(list);
		System.out.println(list.size());
		for(int i=0; i<list.size(); i++) {
			System.out.println(list.get(i));
		}

	}

	static void dfs(int r, int c) {
		map[r][c] = 'x';
		result++;
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];

			if (!checkRange(nr, nc) || map[nr][nc] != '1') {
				continue;
			}

			dfs(nr, nc);
		}

	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < n) && (c >= 0) && (c < n);
	}

}
