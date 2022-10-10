package week11;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 수족관 1
public class BOJ_8982 {

	static int N, K, area, maxC;
	static boolean[] visited;

	static class Point {
		int r, c;

		Point(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static class Edge implements Comparable<Edge> {
		Point start, end;

		Edge(Point p1, Point p2) {
			start = p1;
			end = p2;
		}

		@Override
		public int compareTo(Edge o) {
			return o.start.r - this.start.r;
		}
	}

	static Point[] points;
	static Edge[] edges;
	static PriorityQueue<Edge> pq = new PriorityQueue<>();
	static int[] heights;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		points = new Point[N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int column = Integer.parseInt(st.nextToken());
			int row = Integer.parseInt(st.nextToken());
			points[i] = new Point(row, column);
		}
		maxC = points[N - 1].c;
		visited = new boolean[maxC];
		heights = new int[maxC];
		calcArea(); // 수족관 전체 계산

		K = Integer.parseInt(br.readLine());
		edges = new Edge[K];

		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());

			Point start = new Point(b, a);
			Point end = new Point(d, c);
			edges[i] = new Edge(start, end);
			pq.add(edges[i]);
		}

		for (int i = 1; i < N - 1; i += 2) {
			Point start = points[i];
			Point end = points[i + 1];
			for (int c = start.c; c < end.c; c++) {
				heights[c] = start.r;
			}
		}

		simul();
		System.out.println(area);
	}

	static void simul() {
		while (!pq.isEmpty()) {
			Edge edge = pq.poll();
			Point start = edge.start;
			Point end = edge.end;

			System.out.println("구멍 시작");
			System.out.println("before area = " + area);
			for (int i = start.c; i < end.c; i++) {
				if (visited[i])
					continue;
				visited[i] = true;
				area -= start.r;
			}
			System.out.println("after area = " + area);

//			System.out.println("주변 범위 시작");
//			System.out.println("before area = " + area);
			search(start.r, start.c, end.c);
//			System.out.println("after area = " + area);
		}
	}

	static void search(int hr, int c1, int c2) {
		int nc = c1;
		// 왼쪽
//		System.out.println("왼쪽");
//		System.out.println("before area = " + area);

		while (checkRange(nc - 1) && heights[nc - 1] > hr) {
			nc -= 1;
			if (!visited[nc]) {
				visited[nc] = true;
				area -= hr;
			}
		}
//		System.out.println("after area = " + area);

		nc = c2 - 1;
		// 오른쪽
//		System.out.println("오른쪽");
//		System.out.println("before area = " + area);		
		while (checkRange(nc + 1) && heights[nc + 1] > hr) {
			nc += 1;
			if (!visited[nc]) {
				visited[nc] = true;
				area -= hr;

			}
		}
//		System.out.println("after area = " + area);
	}

	static void calcArea() {
		for (int i = 1; i < N - 1; i += 2) {
			Point p1 = points[i];
			Point p2 = points[i + 1];
			area += (p2.c - p1.c) * p1.r;
		}
	}

	static boolean checkRange(int c) {
		return c >= 0 && c < maxC;
	}
}
