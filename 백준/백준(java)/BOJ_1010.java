package day0812;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 다리 놓기, long 사용해야 함
public class BOJ_1010 {

	static ArrayList<Long> listN;
	static ArrayList<Long> listM;

	static void calc(long start, int cnt, ArrayList<Long> list) {
		while (cnt-- != 0) {
			list.add(start--);
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for (int x = 0; x < t; x++) {
			st = new StringTokenizer(br.readLine(), " ");
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());

			if (n == m) {
				System.out.println(1);
			} else {

				listN = new ArrayList<>();
				listM = new ArrayList<>();

				calc(n, n, listN);
				calc(m, n, listM);
				Long[] arrN = listN.toArray(new Long[listN.size()]);
				Long[] arrM = listM.toArray(new Long[listM.size()]);

				for (int i = 0; i < arrN.length; i++) {
					for (int j = 0; j < arrM.length; j++) {
						if (arrM[j] % arrN[i] == 0) {
							arrM[j] /= arrN[i];
							arrN[i] = 1l;
							break;
						}
					}
				}

				long resultM = 1;
				for (long a : arrM) {
					resultM *= a;
				}
				long resultN = 1;
				for (long a : arrN) {
					resultN *= a;
				}

				System.out.println(resultM / resultN);

			}

		}
	}
}
