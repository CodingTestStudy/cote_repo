package pcs;

import java.util.Scanner;

// N과 M(4)
public class BOJ_15652 {

	static int N, M;
	static int[] cards, result;
	static boolean[] selected;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		cards = new int[N];
		result = new int[N];
		selected = new boolean[N];
		for (int i = 0; i < N; i++) {
			cards[i] = i + 1;
		}

		comb(0, 0);
		System.out.println(sb.toString());
	}

	static void comb(int idx, int cnt) {
		if (cnt == M) {
			for (int i = 0; i < M; i++) {
				sb.append(result[i] + " ");
			}
			sb.append('\n');
			return;
		}

		for (int i = idx; i < N; i++) {
			result[cnt] = cards[i];
			comb(i, cnt + 1);
		}
	}
}
