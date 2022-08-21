package pcs;

import java.util.Arrays;
import java.util.Scanner;

// 암호 만들기
public class BOJ_1759 {

	static int L, C; // 암호 길이, 알파벳 후보 개수
	static char[] cArr;
	static char[] vowels = new char[] { 'a', 'e', 'i', 'o', 'u' };
	static int cons, vowel;
	static boolean[] selected;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		L = sc.nextInt();
		C = sc.nextInt();
		cArr = new char[C];
		for (int i = 0; i < C; i++) {
			cArr[i] = sc.next().charAt(0);
		}
		Arrays.sort(cArr);

		selected = new boolean[C];
		comb(0, 0);
		System.out.println(sb.toString());
	}

	static void comb(int idx, int cnt) {
		if (cnt == L) {
			cons = 0;
			vowel = 0;
			char[] temp = new char[L];
			int j = 0;
			for (int i = 0; i < C; i++) {
				if (selected[i]) {
					temp[j++] = cArr[i];
					if (check(cArr[i]))
						vowel++;
					else
						cons++;
				}
			}
			if (vowel >= 1 && cons >= 2) {
				for (int i = 0; i < temp.length; i++) {
					sb.append(temp[i]);
				}
				sb.append('\n');
			}
			return;
		}

		if (idx == C) {
			return;
		}

		selected[idx] = true;
		comb(idx + 1, cnt + 1);
		selected[idx] = false;
		comb(idx + 1, cnt);
	}

	static boolean check(char c) {
		for (int i = 0; i < vowels.length; i++) {
			if (c == vowels[i])
				return true;
		}
		return false;
	}

}
