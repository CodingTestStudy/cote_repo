package practice;

import java.util.Arrays;
import java.util.Scanner;

public class _11399 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[]p = new int[n+1];
		int[]arr = new int[n+1];
		for(int i=1; i<=n; i++) {
			p[i] = sc.nextInt();
		}

		Arrays.sort(p);
		int answer = 0;
		for(int i=1; i<=n; i++) {
			arr[i] += arr[i-1] + p[i];
			answer += arr[i];
		}
		System.out.println(answer);
	}

}
