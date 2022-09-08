package week7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

// 어드벤처 게임
public class BOJ_2310_최규림 {

	static int n;
	static boolean flag;
	static StringBuilder sb = new StringBuilder();

	static class Room {
		char alphabet;
		int price;
		List<Integer> list = new ArrayList<Integer>();
	}

	static Room[] rooms;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 재귀문제 같음
		while (true) {
			n = Integer.parseInt(br.readLine());
			if (n == 0) {
				break;
			}

			flag = false;
			rooms = new Room[n + 1];
			visited = new boolean[n + 1];

			for (int i = 1; i <= n; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				rooms[i] = new Room();
				rooms[i].alphabet = st.nextToken().charAt(0);
				rooms[i].price = Integer.parseInt(st.nextToken());

				while (true) {
					int r = Integer.parseInt(st.nextToken());
					if (r == 0)
						break;

					rooms[i].list.add(r);
				}

			}
			visited[1] = true;
			dfs(1, 0);
			sb.append(flag ? "YES" : "NO").append('\n');
		}
		System.out.println(sb.toString());
	}

	static void dfs(int idx, int price) {
		if (flag)
			return;
		Room target = rooms[idx];

		if (idx == n) {
			if (target.alphabet == 'T' && target.price > price) {
				return;
			}
			flag = true;
			return;
		}

		// 문
		switch (target.alphabet) {
		case 'E':
			for (int nxt : target.list) {
				if (visited[nxt])
					continue;
				visited[nxt] = true;
				dfs(nxt, price);
				visited[nxt] = false;
			}
			break;
		case 'L':
			for (int nxt : target.list) {
				if (visited[nxt])
					continue;
				visited[nxt] = true;
				dfs(nxt, Math.max(target.price, price));
				visited[nxt] = false;
			}
			break;
		case 'T':
			for (int nxt : target.list) {
				if (visited[nxt])
					continue;
				int p = price - target.price;
				if (p < 0) {
					return;
				}
				visited[nxt] = true;
				dfs(nxt, p);
				visited[nxt] = false;
			}
			break;
		}
	}
}
