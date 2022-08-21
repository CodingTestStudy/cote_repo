package pcs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 부분수열의 합
public class BOJ_1182 {

	static int N, S, answer;
	static int[] arr, cards;
	static boolean[] used;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		arr = new int[N];
		cards = new int[N];
		used = new boolean[N];
		for (int i = 0; i < N; i++) {
			cards[i] = i;
		}

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		subset(0);
		System.out.println(answer);
	}

	static void subset(int cnt) {
		if (cnt == N) {
			int temp = 0;
			boolean flag = false;
			for (int i = 0; i < N; i++) {
				if (used[i]) {
					flag = true;
					temp += arr[cards[i]];
				}
			}
			
			if (temp == S && flag) {				
				answer++;
			}
			return;
		}

		used[cnt] = true;
		subset(cnt + 1);
		used[cnt] = false;
		subset(cnt + 1);
	}
}
