package pcs;

import java.util.Scanner;

// N-Queen
public class BOJ_9663 {

	static int N, answer;
	static int[] cols;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		cols = new int[N + 1];
		setQueen(1);
		System.out.println(answer);
	}

	static void setQueen(int rowNo) {
		if (!isAvailable(rowNo - 1)) {
			return;
		}

		if (rowNo > N) {
			answer++;
			return;
		}

		for (int i = 1; i <= N; i++) {
			cols[rowNo] = i;
			setQueen(rowNo + 1);
		}
	}

	static boolean isAvailable(int rowNo) {
		for (int i = 1; i < rowNo; i++) {
			if (cols[i] == cols[rowNo] || rowNo - i == Math.abs(cols[i] - cols[rowNo])) {
				return false;
			}
		}
		return true;
	}
}
