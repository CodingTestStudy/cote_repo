package day0812;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// 신기한 소수
public class BOJ_2023 {

	static int maxValue;
	static int minValue;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		minValue = (int) Math.pow(10, n - 1);
		maxValue = (int) Math.pow(10, n);

		if (n == 1) {
			System.out.println(2);
			System.out.println(3);
			System.out.println(5);
			System.out.println(7);
			return;
		}

		findPrime(2);
		findPrime(3);
		findPrime(5);
		findPrime(7);

	}

	static void findPrime(int num) {
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(num);
		while (!q.isEmpty()) {
			int target = q.poll();
			if (target > maxValue) {
				continue;
			}

			if (minValue < target) {
				System.out.println(target);
			}

			for (int i = 1; i <= 9; i++) {
				int newNum = createNum(target, i);
				if (isPrime(newNum)) {
					q.add(newNum);
				}
			}
		}
	}

	static int createNum(int num, int a) {
		return num * 10 + a;
	}

	static boolean isPrime(int num) {
		for (int i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;
	}

}
