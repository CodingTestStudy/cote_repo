package week3;

import java.util.Scanner;

public class _18512 {

	static int x, y, p1, p2;
	static boolean[] visited = new boolean[100001];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		x = sc.nextInt();
		y = sc.nextInt();
		p1 = sc.nextInt();
		p2 = sc.nextInt();

		if (p1 == p2) {
			System.out.println(p1);
			return;
		}

		if (p1 > p2) {
			while (p1 < 100001) {
				visited[p1] = true;
				p1 += x;
			}
			while (p2 < 100001) {
				if (visited[p2]) {
					break;
				}
				p2 += y;
			}
			if (p2 > 100001) {
				System.out.println(-1);
			} else {
				System.out.println(p2);
			}
		} else {
			while (p2 < 100001) {
				visited[p2] = true;
				p2 += y;
			}
			while (p1 < 100001) {
				if (visited[p1]) {
					break;
				}
				p1 += x;
			}
			if (p1 > 100001) {
				System.out.println(-1);
			} else {
				System.out.println(p1);
			}
		}
	}

}
