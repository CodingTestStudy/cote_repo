package day0824;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// ABCDE
public class BOJ_13023 {

	static int N, M, answer;
	static ArrayList<ArrayList<Integer>> list = new ArrayList<>();
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		for (int i = 0; i < N; i++) {
			list.add(new ArrayList<>());
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			list.get(a).add(b);
			list.get(b).add(a);
		}

		for (int i = 0; i < N; i++) {
			visited = new boolean[N];
			visited[i] = true;
			dfs(i, 0);
			if (answer == 1) {
				break;
			}
		}

		System.out.println(answer);

	}

	static void dfs(int num, int cnt) {
		if (cnt ==4) {
			answer = 1;
			return;
		}

		for (int i = 0; i < list.get(num).size(); i++) {
			int target = list.get(num).get(i);
			if (!visited[target]) {
				visited[target] = true;
				dfs(target, cnt + 1);
				visited[target] = false;
			}
		}
	}
}
