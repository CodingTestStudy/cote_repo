package day0804;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// [S/W 문제해결 기본] 7일차 - 암호생성기
public class SWEA_1225 {

	static int cycle(int[] arr) {
		int index = -1;
		int cnt = 1;
		while (index == -1) {

			for (int i = 0; i < 8; i++) {
				arr[i] -= cnt;
				cnt = cnt % 5 + 1;

				if (arr[i] <= 0) {
					arr[i] = 0;
					index = i;
					break;
				}
			}
		}
		return index;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		for (int tc = 1; tc <= 10; tc++) {
			int n = Integer.parseInt(br.readLine());
			int[] arr = new int[8];
			st = new StringTokenizer(br.readLine(), " ");
			for (int i = 0; i < 8; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}

			int end = cycle(arr);
			sb.append("#").append(tc);
			for (int i = end + 1; i < 8; i++) {
				sb.append(' ').append(arr[i]);
			}
			for (int i = 0; i <= end; i++) {
				sb.append(' ').append(arr[i]);
			}
			sb.append('\n');
		}
		System.out.println(sb.toString());

	}

}
