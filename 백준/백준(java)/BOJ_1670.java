package week14;

import java.util.Scanner;

// 정상 회담2
public class BOJ_1670 {

	static int N;
	static long[] dp;
	static long mod = 987654321;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		dp = new long[N + 1];
		dp[0] = 1;
		dp[2] = 1;

		for (int i = 4; i <= N; i += 2) {
			for (int j = 0; j <= i - 2; j += 2) {
				// 임의의 선을 긋고(-2), 위에 j명 아래에 i-j-2명
				dp[i] += (dp[j] * dp[i - j - 2]);
				dp[i] %= mod;
			}
		}
		System.out.println(dp[N]);

	}

//	static long calc(int idx) {
//		if (idx == 0 || idx == 2) {
//			return 1;
//		}
//
//		long temp = 0;
//
//		// i명 짝짓고, 나머지 idx-i명 경우
//		for (int i = 2; i <= idx; i += 2) {
//			temp += calc(i - 2) * calc(idx - i) % 987654321;
//		}
//		return temp;
//	}
}
