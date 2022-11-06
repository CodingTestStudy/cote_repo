package week15;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 운동
public class BOJ_1956 {

	static int V, E, ans;
	static int[][] arr;
	static int maxValue;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		ans = Integer.MAX_VALUE;
		maxValue = 10000 * 401;

		arr = new int[V + 1][V + 1];
		for (int i = 1; i <= V; i++) {
			Arrays.fill(arr[i], maxValue);
		}

		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			arr[a][b] = c;
		}

		for (int k = 1; k <= V; k++) {
			for (int i = 1; i <= V; i++) {
				for (int j = 1; j <= V; j++) {
					arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j]);
				}
			}
		}

		for (int start = 1; start <= V; start++) {
			ans = Math.min(ans, arr[start][start]);
		}

		System.out.println(ans == maxValue ? -1 : ans);
	}
}
