package javastudy.이코테.그리디;

import java.util.Scanner;

public class _1이_될_때까지 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int cnt = 0;

        while (true) {
            int target = (n / k) * k;
            cnt += n - target;
            n = target;

            if (n < k) {
                cnt += n - 1;
                break;
            }

            n /= k;
            cnt += 1;
        }
        System.out.println(cnt);
    }
}
