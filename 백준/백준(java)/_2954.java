package week3;

import java.util.Scanner;

public class _2954 {

	public static void main(String[] args) {
		// 창영이의 일기장
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		String answer = "";

		char[] chars = new char[] { 'a', 'e', 'i', 'o', 'u' };

		int index = 0;
		while (index < str.length()) {
			char c = str.charAt(index);
			boolean isFlag = false;
			for(char cc : chars) {
				if(cc == c) {
					isFlag = true;
					break;
				}
			}
			if(isFlag) {
				index += 3;
			}else {
				index += 1;
			}
			answer += c;
		}
		System.out.println(answer);
	}

}
