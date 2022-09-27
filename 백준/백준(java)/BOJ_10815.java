package binarySearch;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_10815 {

	static int N, M;
	static int[] cards;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		cards = new int[N];
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(cards);

		M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < M; i++) {
			if (binarySearch(Integer.parseInt(st.nextToken()))) {
				sb.append("1 ");
			} else {
				sb.append("0 ");
			}
		}
		System.out.println(sb.toString());

	}

	static boolean binarySearch(int target) {
		int left = 0;
		int right = N - 1;
		boolean isExist = false;

		while (left <= right) {
			int mid = (left + right) / 2;

			if (cards[mid] == target) {
				isExist = true;
			}

			if (cards[mid] > target) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}

		return isExist;
	}
}
