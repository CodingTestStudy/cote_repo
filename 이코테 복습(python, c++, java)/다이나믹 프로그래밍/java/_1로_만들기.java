package javastudy.이코테.다이나믹프로그래밍;

import java.util.Scanner;

public class _1로_만들기 {

    public static int[] dp = new int[30001];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        for (int i = 2; i <= x; i++) {
            dp[i] = dp[i - 1] + 1;
            if (i % 5 == 0) {
                dp[i] = Math.min(dp[i], dp[i / 5] + 1);
            }
            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i], dp[i / 3] + 1);
            }
            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            }
        }
        System.out.println(dp[x]);
    }
}
