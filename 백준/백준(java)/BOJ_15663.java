package pcs;

import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Scanner;

// N과 M(9)
public class BOJ_15663 {

	static int N, M;
	static int[] arr, result;
	static boolean[] used;

	static LinkedHashSet<String> ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();

		arr = new int[N];
		result = new int[M];
		used = new boolean[N];

		ans = new LinkedHashSet<>();
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);

		perm(0);
		for (String str : ans) {
			System.out.print(str);
		}

	}

	static void perm(int idx) {
		if (idx == M) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < M; i++) {
				sb.append(result[i] + " ");
			}
			sb.append('\n');
			ans.add(sb.toString());
			return;
		}

		for (int i = 0; i < N; i++) {
			if (used[i])
				continue;

			used[i] = true;
			result[idx] = arr[i];
			perm(idx + 1);
			used[i] = false;
		}
	}

	static boolean check(List<int[]> tempList) {
		for (int[] temp : tempList) {
			int cnt = 0;
			for (int i = 0; i < M; i++) {
				if (result[i] == temp[i]) {
					cnt++;
				}
			}
			if (cnt == M) {
				return false;
			}
		}
		return true;
	}
}
