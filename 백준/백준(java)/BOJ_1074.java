package day0816;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

// Z
public class BOJ_1074 {

	static int N, R, C;
	static int answer;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		int len = (int) Math.pow(2, N) / 2;
		find(0, 0, len, 0);
		System.out.println(answer);
	}

	static void find(int r, int c, int len, int cnt) {

		if (len == 1) {
			if (r == R && c == C) {
				answer = cnt;
			} else if (r == R && c + 1 == C) {
				answer = cnt + 1;
			} else if (r + 1 == R && c == C) {
				answer = cnt + 2;
			} else {
				answer = cnt + 3;
			}
		}

		int next = (int) Math.pow(len, 2);

		if (checkRange(r, c, r + len, c + len)) {
			find(r, c, len / 2, cnt);
		} else if (checkRange(r, c + len, r + len, c + len * 2)) {
			find(r, c + len, len / 2, cnt + next);
		} else if (checkRange(r + len, c, r + len * 2, c + len)) {
			find(r + len, c, len / 2, cnt + next * 2);
		} else if (checkRange(r + len, c + len, r + len * 2, c + len * 2)) {
			find(r + len, c + len, len / 2, cnt + next * 3);
		}
	}

	static boolean checkRange(int r1, int c1, int r2, int c2) {
		return (R >= r1) && (R < r2) && (C >= c1) && (C < c2);
	}
}
