package practice;

import java.util.Scanner;

public class _8320 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int answer = 0;
		for(int r=1; r<=n; r++) {
			for(int c=r; c*r<=n; c++) {
				answer += 1;
			}
		}

		System.out.println(answer);
	}

}
