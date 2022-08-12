package day0812;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 스타트와 링크
public class BOJ_14889 {
	static int n;
	static int[][] map;
	static int[] person;
	static boolean[] select;
	static ArrayList<int[]> listA = new ArrayList<>();
	static ArrayList<int[]> listB = new ArrayList<>();
	static int answer;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];
		person = new int[n];
		for (int i = 0; i < n; i++) {
			person[i] = i + 1;
		}
		select = new boolean[n];

		for (int r = 0; r < n; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < n; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		comb(0, 0);
		answer = Integer.MAX_VALUE;
		// i번째 조합된 각 팀의 점수 계산
		for (int x = 0; x < listA.size(); x++) {
			int[] tempA = listA.get(x);
			int[] tempB = listB.get(x);
			int sumA = 0, sumB = 0;
			for (int i = 0; i < tempA.length - 1; i++) {
				for (int j = i + 1; j < tempA.length; j++) {
					sumA += map[tempA[i]][tempA[j]];
					sumA += map[tempA[j]][tempA[i]];
					sumB += map[tempB[i]][tempB[j]];
					sumB += map[tempB[j]][tempB[i]];
				}
			}

			answer = Math.min(answer, Math.abs(sumA - sumB));

		}
		System.out.println(answer);

	}

	static void comb(int idx, int cnt) {
		if (cnt == n / 2) {

			int[] a = new int[n / 2];
			int[] b = new int[n / 2];
			int idxA = 0, idxB = 0;
			for (int i = 0; i < n; i++) {
				// 스타트 팀
				if (select[i]) {
					a[idxA++] = i;
				}
				// 링크 팀
				else {
					b[idxB++] = i;
				}
			}
			listA.add(a);
			listB.add(b);
			return;
		}
		if (idx == n) {
			return;
		}

		select[idx] = true;
		comb(idx + 1, cnt + 1);
		select[idx] = false;
		comb(idx + 1, cnt);
	}

}
