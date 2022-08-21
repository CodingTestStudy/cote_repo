package pcs;

import java.util.Scanner;

// N과 M(2)
public class BOJ_15650 {

	static int N, M;
	static int[] cards;
	static boolean[] selected;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		cards = new int[N];
		selected = new boolean[N];

		for (int i = 0; i < N; i++) {
			cards[i] = i + 1;
		}

		comb(0, 0);
		System.out.println(sb.toString());
	}

	static void comb(int idx, int cnt) {
		if (cnt == M) {
			for (int i = 0; i < N; i++) {
				if (selected[i]) {
					sb.append(cards[i] + " ");
				}
			}
			sb.append('\n');
			return;
		}
		
		if(idx == N) {
			return;
		}

		selected[idx] = true;
		comb(idx + 1, cnt + 1);
		selected[idx] = false;
		comb(idx + 1, cnt);
	}
}
