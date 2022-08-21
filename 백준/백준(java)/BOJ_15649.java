package pcs;

import java.util.Scanner;

// N과 M(1)
public class BOJ_15649 {

	static int N, M;
	static int[] cards, result;
	static boolean[] used;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();

		cards = new int[N];
		result = new int[M];
		used = new boolean[N];

		for (int i = 0; i < N; i++) {
			cards[i] = i + 1;
		}

		perm(0);
		System.out.println(sb.toString());
	}

	static void perm(int idx) {
		if (idx == M) {
			for (int i = 0; i < M; i++) {
				sb.append(result[i] + " ");
			}
			sb.append('\n');
			return;
		}

		for (int i = 0; i < N; i++) {
			if (used[i])
				continue;

			result[idx] = cards[i];
			used[i] = true;
			perm(idx + 1);
			used[i] = false;
		}
	}
}
