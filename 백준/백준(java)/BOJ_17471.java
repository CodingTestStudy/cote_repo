import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

//게리맨더링
public class BOJ_17471 {
	static int N, ans;
	static int[] people;
	static ArrayList<ArrayList<Integer>> list = new ArrayList<>();

	static boolean[] selected;
	static ArrayList<Set<Integer>> combList = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		ans = Integer.MAX_VALUE;
		N = Integer.parseInt(br.readLine());
		people = new int[N + 1];
		selected = new boolean[N + 1];

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 1; i <= N; i++) {
			people[i] = Integer.parseInt(st.nextToken());
			list.add(new ArrayList<>());
		}
		list.add(new ArrayList<>());

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine(), " ");

			int n = Integer.parseInt(st.nextToken());
			for (int x = 0; x < n; x++) {
				int target = Integer.parseInt(st.nextToken());
				list.get(i).add(target);
				list.get(target).add(i);
			}

		}

		for (int i = 1; i <= N; i++) {
			comb(1, 0, i);
		}

		for (Set<Integer> part1 : combList) {

			if (part1.size() == 0 || part1.size() == N) {
				continue;
			}

			Set<Integer> part2 = new HashSet<>();
			for (int i = 1; i <= N; i++) {
				if (!part1.contains(i)) {
					part2.add(i);
				}
			}

			if (isConnected(part1) && isConnected(part2)) {

				ans = Math.min(ans, Math.abs(calc(part1) - calc(part2)));
			}
		}

		if (ans == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {

			System.out.println(ans);
		}

	}

	static int calc(Set<Integer> set) {
		int result = 0;
		for (int x : set) {
			result += people[x];
		}
		return result;
	}

	static void comb(int idx, int cnt, int R) {
		if (cnt == R) {
			Set<Integer> result = new HashSet<>();
			for (int i = 1; i <= N; i++) {
				if (selected[i]) {
					result.add(i);
				}
			}

			combList.add(result);
			return;
		}

		if (idx == N + 1) {
			return;
		}

		selected[idx] = true;
		comb(idx + 1, cnt + 1, R);
		selected[idx] = false;
		comb(idx + 1, cnt, R);
	}

	static boolean isConnected(Set<Integer> set) {
		if (set.size() == 1)
			return true;

		List<Integer> temp = new ArrayList<>();
		for (int x : set) {
			temp.add(x);
		}

		int start = temp.get(0);
		Queue<Integer> q = new ArrayDeque<>();
		boolean[] visited = new boolean[N + 1];
		q.add(start);
		visited[start] = true;

		int cnt = 1;
		while (!q.isEmpty()) {
			int now = q.poll();
			for (int next : list.get(now)) {
				if (!visited[next] && set.contains(next)) {
					visited[next] = true;
					cnt++;
					q.add(next);
				}
			}
		}

		return cnt == set.size();
	}
}
