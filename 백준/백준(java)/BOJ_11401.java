package pcs;

import java.util.Scanner;

// 이항 계수3
public class BOJ_11401 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		double answer = calc(N, K) / calc(K, K);
		System.out.println(answer % 1000000007);
	}

	// 팩토리얼
	static double calc(int x, int cnt) {
		double result = 1;
		while (cnt-- != 0) {
			result *= x;
			result %= 1000000007;
			x -= 1;
		}
		return result;
	}
}
