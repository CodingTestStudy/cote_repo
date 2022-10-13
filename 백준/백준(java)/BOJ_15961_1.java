import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;
import java.util.StringTokenizer;

// 회전 초밥
public class BOJ_15961 {

	static int N, d, k, c, ans, answer;
	static int[] sushi;
	static boolean isCoupon;
	static int[] visited;

	static Queue<Integer> q = new ArrayDeque<Integer>();
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken()); // 접시 수
		d = Integer.parseInt(st.nextToken()); // 초밥 가짓수
		k = Integer.parseInt(st.nextToken()); // 연속해서 먹는 접시 수
		c = Integer.parseInt(st.nextToken()); // 쿠폰 번호

		visited = new int[d + 1];

		sushi = new int[N + k - 1];
		for (int i = 0; i < N; i++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}

		for (int i = 0; i < k - 1; i++) {
			sushi[N + i] = sushi[i];
		}

		ans = 0;
		for (int i = 0; i < k; i++) {
			if (visited[sushi[i]] == 0) {
				ans++;
			}
			q.add(sushi[i]);
			visited[sushi[i]]++;
		}

		if (visited[c] == 0) {
			answer = ans + 1;
			isCoupon = true;
		}

		for (int i = k; i < N + k - 1; i++) {
			int front = q.poll();
			visited[front]--;
			if (visited[front] == 0) {
				ans--;
			}

			int back = sushi[i];
			// 중복
			if (visited[back] == 0) {
				ans++;
			}

			q.add(back);
			visited[back]++;

			if (visited[c] == 0) {
				answer = Math.max(answer, ans + 1);
			} else {
				answer = Math.max(answer, ans);
			}

		}
		System.out.println(answer);
	}
}
