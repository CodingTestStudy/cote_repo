package pcs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 연산자 끼워넣기
public class BOJ_14888 {

	static int N, max, min;
	static int[] nums;
	static int[] opCnt = new int[4];
	static int[] opArr;
	static int[] result;
	static boolean[] used;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		nums = new int[N];
		result = new int[N - 1];
		opArr = new int[N - 1];
		used = new boolean[N - 1];
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < 4; i++) {
			opCnt[i] = Integer.parseInt(st.nextToken());
		}

		max = Integer.MIN_VALUE;
		min = Integer.MAX_VALUE;
		setOp();
		perm(0);
		
		System.out.println(max);
		System.out.println(min);
	}

	static void perm(int idx) {
		if (idx == N - 1) {
			calc();
			return;
		}

		for (int i = 0; i < N - 1; i++) {
			if (used[i]) {
				continue;
			}

			result[idx] = opArr[i];
			used[i] = true;
			perm(idx + 1);
			used[i] = false;

		}
	}

	static void calc() {
		int temp = nums[0];
		for (int i = 0; i < N - 1; i++) {
			switch (result[i]) {
			case 0:
				temp += nums[i + 1];
				break;
			case 1:
				temp -= nums[i + 1];
				break;
			case 2:
				temp *= nums[i + 1];
				break;
			case 3:
				temp /= nums[i + 1];
				break;
			}
		}
		max = Math.max(max, temp);
		min = Math.min(min, temp);
	}

	static void setOp() {
		int idx = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < opCnt[i]; j++) {
				opArr[idx++] = i;
			}
		}
	}
}
