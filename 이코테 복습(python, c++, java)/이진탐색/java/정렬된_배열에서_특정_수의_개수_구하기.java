package javastudy.이코테.이진탐색;

import java.util.Scanner;

public class 정렬된_배열에서_특정_수의_개수_구하기 {

    public static int lowerBound(int[] arr, int target, int start, int end) {
        while (start < end) {
            int mid = (start + end) / 2;
            if (arr[mid] >= target) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return end;
    }

    public static int upperBound(int[] arr, int target, int start, int end) {
        while (start < end) {
            int mid = (start + end) / 2;
            if (arr[mid] > target) {
                end = mid;
            } else {
                start = mid = 1;
            }
        }
        return end;
    }

    public static int countByRange(int[] arr, int leftValue, int rightValue) {
        int rightIndex = upperBound(arr, rightValue, 0, arr.length);
        int leftIndex = lowerBound(arr, leftValue, 0, arr.length);
        return rightIndex - leftIndex;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int x = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int cnt = countByRange(arr, x, x);

        if (cnt == 0) {
            System.out.println(-1);
        } else {
            System.out.println(cnt);
        }
    }
}
