package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;

//단지번호붙이기(BFS)
public class BOJ_2667_1 {

	static int n;
	static char[][] map;
	static List<Integer> list = new ArrayList<Integer>();
	static int maxValue = 26;

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

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
					list.add(bfs(r, c));
				}
			}
		}

		Collections.sort(list);
		System.out.println(list.size());
		for (int i = 0; i < list.size(); i++) {
			System.out.println(list.get(i));
		}
	}

	static int bfs(int r, int c) {
		int result = 1;
		Queue<int[]> q = new ArrayDeque<int[]>();
		q.add(new int[] { r, c });
		map[r][c] = 'x';

		while (!q.isEmpty()) {
			int[] now = q.poll();
			for (int i = 0; i < 4; i++) {
				int nr = now[0] + dr[i];
				int nc = now[1] + dc[i];
				if (!checkRange(nr, nc) || map[nr][nc] != '1') {
					continue;
				}

				result++;
				map[nr][nc] = 'x';
				q.add(new int[] { nr, nc });
			}
		}
		return result;
	}

	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < n) && (c >= 0) && (c < n);
	}

}
