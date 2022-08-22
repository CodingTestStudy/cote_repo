package day0822;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

// Contact
public class SWEA_1238 {

	static int N, start, answer;
	static ArrayList<ArrayList<Integer>> graph;
	static boolean[] visited;
	static Map<Integer, List<Integer>> map;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= 10; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			start = Integer.parseInt(st.nextToken());
			answer = 0;
			graph = new ArrayList<>();
			visited = new boolean[101];
			map = new HashMap<>();

			for (int i = 0; i <= 100; i++) {
				graph.add(new ArrayList<>());
			}

			st = new StringTokenizer(br.readLine(), " ");
			for (int i = 0; i < N / 2; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());

				graph.get(from).add(to);
			}

			bfs();
			sb.append("#" + tc + " " + answer).append('\n');
		}
		System.out.println(sb.toString());
	}

	static void bfs() {
		Queue<Integer> q = new ArrayDeque<Integer>();
		q.add(start);
		visited[start] = true;
		int time = 0;
		while (!q.isEmpty()) {
			time++;
			map.put(time, new ArrayList<>());
			int qSize = q.size();
			for (int x = 0; x < qSize; x++) {
				int now = q.poll();
				for (int i = 0; i < graph.get(now).size(); i++) {
					int target = graph.get(now).get(i);
					if (!visited[target]) {
						visited[target] = true;
						q.add(target);
						map.get(time).add(target);
					}
				}

			}
		}
		Collections.sort(map.get(time - 1));
		List<Integer> temp = map.get(time - 1);
		answer = temp.get(temp.size() - 1);
	}
}
