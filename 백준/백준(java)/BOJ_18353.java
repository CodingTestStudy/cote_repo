package week10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_18353 {

	static int N;
	static int[] arr, dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		dp = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		if (N == 1) {
			System.out.println(0);
		} else {
			for (int i = 1; i < N; i++) {
				if (arr[i] >= arr[i - 1]) {
					dp[i] = dp[i - 1] + 1;
				} else {
					dp[i] = dp[i - 1];
				}

			}

			System.out.println(dp[N - 1]);
		}

	}
}
