package day0830;

import java.util.Scanner;

// 차량 번호판1
public class BOJ_16968 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] cArr = sc.next().toCharArray();
		int answer = 1;
		boolean digit = true;
		for (int i = 0; i < cArr.length; i++) {
			if (i == 0) {
				answer *= cArr[i] == 'd' ? 10 : 26;
				digit = cArr[i] == 'd' ? true : false;
			} else {
				if (cArr[i] == 'd') {
					if (digit) {
						answer *= 9;
					} else {
						answer *= 10;
					}
				} else {
					if (!digit) {
						answer *= 25;
					} else {
						answer *= 26;
					}
				}
				digit = cArr[i] == 'd' ? true : false;
			}

		}
		System.out.println(answer);

	}
}
