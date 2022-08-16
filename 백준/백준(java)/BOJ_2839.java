package day0816;

import java.util.Scanner;

// 설탕 배달
public class BOJ_2839 {

	static int n;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();

		int five = n / 5;
		int r = n - five * 5;
		while (r % 3 != 0) {
			--five;
			r += 5;
			if (five < 0) {
				System.out.println(-1);
				return;
			}
		}

		int three = r / 3;
		System.out.println(five + three);

	}
}
