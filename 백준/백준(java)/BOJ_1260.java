package day0818;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// DFS와 BFS
public class BOJ_1260 {

	static int n, m, v;
	static Node[] graph;
	static boolean[] visited;

	static class Node {
		List<Integer> list = new ArrayList<>();
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		v = Integer.parseInt(st.nextToken());

		graph = new Node[n + 1];
		for (int i = 1; i <= n; i++) {
			graph[i] = new Node();
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());

			graph[from].list.add(to);
			graph[to].list.add(from);
		}

		for (int i = 1; i <= n; i++) {
			Collections.sort(graph[i].list);
		}

		visited = new boolean[n + 1];
		dfs(v);
		System.out.println();

		visited = new boolean[n + 1];
		bfs();
		System.out.println();
	}

	static void bfs() {
		Queue<Integer> q = new ArrayDeque<Integer>();
		q.add(v);
		visited[v] = true;
		System.out.print(v + " ");
		while (!q.isEmpty()) {
			int target = q.poll();
			for (int i = 0; i < graph[target].list.size(); i++) {
				int temp = graph[target].list.get(i);
				if (!visited[temp]) {
					visited[temp] = true;
					q.add(temp);
					System.out.print(temp + " ");
				}
			}
		}
	}

	static void dfs(int cur) {

		visited[cur] = true;
		System.out.print(cur + " ");

		for (int i = 0; i < graph[cur].list.size(); i++) {
			int target = graph[cur].list.get(i);
			if (!visited[target]) {
				dfs(target);
			}
		}

	}

}
