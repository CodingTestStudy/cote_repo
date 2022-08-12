package day0812;

import java.util.Scanner;

// 도형이가 만든 맛있는 음식
public class BOJ_2961 {
	static int n;
	static food[] foods;
	static int answer;

	static class food {
		int s, b;

		food(int s, int b) {
			this.s = s;
			this.b = b;

		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		foods = new food[n];
		answer = Integer.MAX_VALUE;
		for (int i = 0; i < n; i++) {
			foods[i] = new food(sc.nextInt(), sc.nextInt());
		}

		subset(0, 1, 0);
		System.out.println(answer);
	}

	static void subset(int idx, int sumS, int sumB) {
		if (sumS != 0 && sumB != 0) {
			answer = Math.min(answer, Math.abs(sumS - sumB));
		}

		if (idx == n)
			return;
		subset(idx + 1, sumS * foods[idx].s, sumB + foods[idx].b);
		subset(idx + 1, sumS, sumB);
	}
}
