package day0825;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 최단 경로(방향 그래프)
public class BOJ_1753 {

	static int V, E;
	static int[] D;
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();

	static class Node {
		int vertex, weight;
		Node next;

		Node(int vertex, int weight, Node next) {
			this.vertex = vertex;
			this.weight = weight;
			this.next = next;
		}
	}

	static Node[] adjList;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		adjList = new Node[V + 1];
		D = new int[V + 1];
		Arrays.fill(D, Integer.MAX_VALUE);
		visited = new boolean[V + 1];

		int start = Integer.parseInt(br.readLine());
		D[start] = 0;

		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());

			adjList[u] = new Node(v, w, adjList[u]);
		}

		int min, minVertex;
		for (int i = 1; i <= V; i++) {
			min = Integer.MAX_VALUE;
			minVertex = -1;

			for (int j = 1; j <= V; j++) {
				if (!visited[j] && min > D[j]) {
					min = D[j];
					minVertex = j;
				}
			}
			
			if(minVertex == -1) {
				break;
			}
//			System.out.println(minVertex);
			visited[minVertex] = true;

			for (Node temp = adjList[minVertex]; temp != null; temp = temp.next) {
				if (!visited[temp.vertex] && D[temp.vertex] > D[minVertex] + temp.weight) {
					D[temp.vertex] = D[minVertex] + temp.weight;
				}
			}
		}

		for (int i = 1; i <= V; i++) {
			if (D[i] == Integer.MAX_VALUE) {
				sb.append("INF").append('\n');
			} else {
				sb.append(D[i]).append('\n');
			}
		}

		System.out.println(sb.toString());
	}
}
