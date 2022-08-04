package day0802;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

//[S/W 문제해결 기본] 1일차 - Flatten
public class SWEA_1208 {
	static int x = 100;
	static int[] box = new int[x];

	static void swap() {

		for (int i = 1; i < 100; i++) {
			if (box[0] > box[i]) {
				int temp = box[0];
				box[0] = box[i];
				box[i] = temp;
			}

			if (box[99] < box[99 - i]) {
				int temp = box[99];
				box[99] = box[99 - i];
				box[99 - i] = temp;
			}

		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = 10;
		for (int tc = 1; tc <= t; tc++) {
			int dump = Integer.parseInt(br.readLine());

			String str = br.readLine();
			StringTokenizer st = new StringTokenizer(str, " ");
			for (int i = 0; i < 100; i++) {
				box[i] = Integer.parseInt(st.nextToken());
			}

			Arrays.sort(box);

			for (int i = 0; i < dump; i++) {
				int maxValue = box[99];
				int minValue = box[0];

				if (Math.abs(maxValue - minValue) <= 1) {
					break;
				}

				box[99] -= 1;
				box[0] += 1;
				swap();
			}

			int answer = Math.abs(box[0] - box[99]);
			System.out.println("#" + tc + " " + answer);
		}

	}
}
