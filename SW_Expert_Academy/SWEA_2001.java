package day0803;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 파리 퇴치
public class SWEA_2001 {

	static int t, n, m;
	static int[][] arr;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			arr = new int[n][n];
			int answer = 0;
			for (int r = 0; r < n; r++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int c = 0; c < n; c++) {
					arr[r][c] = Integer.parseInt(st.nextToken());
				}
			}

			for (int r = 0; r < n - m + 1; r++) {
				for (int c = 0; c < n - m + 1; c++) {
					int temp = 0;
					for (int x = 0; x < m; x++) {
						for (int y = 0; y < m; y++) {
							temp += arr[r + x][c + y];
						}
					}
					answer = Math.max(answer, temp);
				}
			}
			System.out.println("#" + tc + " " + answer);
		}
	}

}
