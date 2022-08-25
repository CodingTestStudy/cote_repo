package day0825;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 네트워크 연결(프림)
public class BOJ_1922 {

	static int N, M;
	static int[] distance;
	static boolean[] visited;

	static class Node {
		int vertex, weight;
		Node next;

		Node(int vertex, int weight, Node next) {
			this.vertex = vertex;
			this.weight = weight;
			this.next = next;
		}
	}

	static class Vertex {
		int num, weight;

		Vertex(int num, int weight) {
			this.num = num;
			this.weight = weight;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());

		Node[] adjList = new Node[N + 1];
		visited = new boolean[N + 1];
		distance = new int[N + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			adjList[a] = new Node(b, c, adjList[a]);
			adjList[b] = new Node(a, c, adjList[b]);
		}

		PriorityQueue<Vertex> pq = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
		pq.add(new Vertex(1, 0));
		distance[1] = 0;

		while (true) {
			Vertex v = pq.poll();

			if (visited[v.num]) {
				continue;
			}
			
			
		}

	}

}
