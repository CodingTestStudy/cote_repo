package day0830;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

// 결혼식
public class BOJ_5567 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());

		boolean[] visited = new boolean[n + 1];
		visited[1] = true;

		ArrayList<ArrayList<Integer>> friends = new ArrayList<>();
		for (int i = 0; i <= n; i++) {
			friends.add(new ArrayList<>());
		}

		for (int i = 0; i < m; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			friends.get(a).add(b);
			friends.get(b).add(a);
		}

		List<Integer> list = new ArrayList<>();
		for (int x : friends.get(1)) {
			list.add(x);
		}

		Set<Integer> set = new HashSet<>();
		for (int x : list) {
			set.add(x);
			for (int y : friends.get(x)) {
				if (y != 1)
					set.add(y);
			}
		}
		System.out.println(set.size());

	}

}
