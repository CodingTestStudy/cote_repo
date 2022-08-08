package day0808;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

//[S/W 문제해결 기본] 8일차 - 암호문1
public class SWEA_1228 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		for (int tc = 1; tc <= 10; tc++) {
			StringBuilder sb = new StringBuilder();

			int n = Integer.parseInt(br.readLine()); // 원본 암호문 길이
			LinkedList<String> pw = new LinkedList<>();// 원본 암호문

			st = new StringTokenizer(br.readLine(), " ");
			for (int i = 0; i < n; i++) {
				pw.add(st.nextToken());
			}

			int s = Integer.parseInt(br.readLine()); // 명렁어 개수

			st = new StringTokenizer(br.readLine(), "I"); // 명령어
			while (st.hasMoreTokens()) {
				String[] temp = st.nextToken().split(" ");
				int x = Integer.parseInt(temp[1]); // 삽입 위치
				int y = Integer.parseInt(temp[2]); // 삽입 숫자 개수

				for (int i = 3; i < temp.length; i++) {
					pw.add(x++, temp[i]);
				}
			}

			sb.append("#").append(tc).append(" ");
			for (int i = 0; i < 10; i++) {
				sb.append(pw.get(i)).append(" ");
			}
			System.out.println(sb.toString());

		}

	}
}
