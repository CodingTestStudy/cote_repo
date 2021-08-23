package javastudy.이코테.이진탐색;

import java.util.Scanner;

public class 떡볶이_떡_만들기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int start = 0;
        int end = (int) 1e9;

        int result = 0;
        while (start <= end) {
            long total = 0;
            int mid = (start + end) / 2;

            for (int i = 0; i < n; i++) {
                if (arr[i] > mid) {
                    total += arr[i] - mid;
                }
            }

            if (total < m) {
                end = mid - 1;
            } else {
                start = mid + 1;
                result = mid;
            }
        }
        System.out.println(result);
    }
}
