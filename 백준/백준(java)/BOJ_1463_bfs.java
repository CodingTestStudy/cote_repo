import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

//1로 만들기
public class BOJ_1463_bfs {

	static int N;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		System.out.println(bfs());
	}

	static int bfs() {
		Queue<Integer> q = new ArrayDeque<Integer>();
		boolean[] visited = new boolean[N + 1];
		visited[N] = true;
		q.add(N);
		int cnt = 0;

		while (!q.isEmpty()) {
			int loop = q.size();

			for (int i = 0; i < loop; i++) {
				int target = q.poll();
				if (target == 1) {
					return cnt;
				}

				if (target >= 3 && target % 3 == 0) {
					q.add(target / 3);
				}
				if (target >= 2 && target % 2 == 0) {
					q.add(target / 2);
				}
				q.add(target - 1);

			}
			cnt++;
		}

		return -1;
	}
}
