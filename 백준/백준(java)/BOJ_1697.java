package boj;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

//숨바꼭질
public class BOJ_1697 {
	static int N, K, answer;
	static boolean[] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();
		visited = new boolean[200001];
		if (N == K) {
			System.out.println(0);
		} else {
			bfs();
			System.out.println(answer);
		}
	}

	static void bfs() {
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(N);
		visited[N] = true;
		int time = 0;
		while (!q.isEmpty()) {
			time++;
			int qSize = q.size();
			for (int x = 0; x < qSize; x++) {
				int NOW = q.poll();

				int n1 = NOW - 1;
				int n2 = NOW + 1;
				int n3 = NOW * 2;
				if (n1 == K || n2 == K || n3 == K) {
					answer = time;
					return;
				}

				// 1
				if (checkRange(n1) && !visited[n1]) {
					visited[n1] = true;
					q.add(n1);
				}
				// 2
				if (checkRange(n2) && !visited[n2]) {
					visited[n2] = true;
					q.add(n2);
				}
				// 3
				if (checkRange(n3) && !visited[n3]) {
					visited[n3] = true;
					q.add(n3);
				}

			}

		}
	}

	static boolean checkRange(int num) {
		return (num >= 0) && (num <= 100000);
	}
}
