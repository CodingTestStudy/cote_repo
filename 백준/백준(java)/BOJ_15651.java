package pcs;

import java.util.Scanner;

// N과 M(3)
public class BOJ_15651 {

	static int N, M;
	static int[] cards, result;

	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();

		cards = new int[N];
		result = new int[M];

		for (int i = 0; i < N; i++) {
			cards[i] = i + 1;
		}

		perm2(0);
		System.out.println(sb.toString());
	}

	static void perm2(int cnt) {
		if (cnt == M) {
			for (int i = 0; i < M; i++) {
				sb.append(result[i] + " ");
			}
			sb.append('\n');
			return;
		}

		for (int i = 0; i < N; i++) {
			result[cnt] = cards[i];
			perm2(cnt + 1);
		}
	}

}
