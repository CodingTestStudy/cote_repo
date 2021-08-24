package javastudy.이코테.다이나믹프로그래밍;

import java.util.Arrays;
import java.util.Scanner;

public class 효율적인_화폐_구성 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }

        int[] dp = new int[m + 1];
        Arrays.fill(dp, 10001);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i < m + 1; i++) {
                if (dp[i - coin] != 10001) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        if (dp[m] == 10001) {
            System.out.println(-1);
        } else {
            System.out.println(dp[m]);
        }
    }
}
