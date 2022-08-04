package day0804;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
public class SWEA_1218 {

	static int c1, c2, c3, c4;

	static boolean check(char c) {
		switch (c) {
		case '(':
			++c1;
			break;
		case ')':
			--c1;
			break;
		case '[':
			++c2;
			break;
		case ']':
			--c2;
			break;
		case '{':
			++c3;
			break;
		case '}':
			--c3;
			break;
		case '<':
			++c4;
			break;
		case '>':
			--c4;
			break;
		}

		if ((c1 < 0) || (c2 < 0) || (c3 < 0) || (c4 < 0)) {
			return false;
		}
		return true;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		for (int tc = 1; tc <= 10; tc++) {
			int answer = 1;
			int n = Integer.parseInt(br.readLine());
			String str = br.readLine();

			c1 = 0;
			c2 = 0;
			c3 = 0;
			c4 = 0;

			for (int i = 0; i < n; i++) {
				char c = str.charAt(i);
				if (!check(c)) {
					answer = 0;
					break;
				}
			}

			sb.append("#").append(tc).append(" ").append(answer).append('\n');
		}
		System.out.println(sb);

	}

}
