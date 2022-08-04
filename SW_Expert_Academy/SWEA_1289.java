package day0801;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

//원재의 메모리 복구하기
public class SWEA_1289 {
	static int t;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {
			int answer = 0;
			String str = br.readLine();
			char c = '0';
			for (int i = 0; i < str.length(); i++) {
				if (str.charAt(i) != c) {
					answer++;
					c = str.charAt(i);
				}
			}

			System.out.println("#" + tc + " " + answer);
		}

	}
}
