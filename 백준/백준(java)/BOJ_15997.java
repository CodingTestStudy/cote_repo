package week7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

// 승부 예측
public class BOJ_15997_최규림 {

	static Map<String, Integer> map = new HashMap<String, Integer>();

	static class Team implements Comparable<Team> {
		String name;
		int score, idx;

		Team(int idx, String name, int score) {
			this.idx = idx;
			this.name = name;
			this.score = score;
		}

		@Override
		public int compareTo(Team o) {
			return o.score - this.score;
		}
	}

	static Team[] teams = new Team[4];
	static double[] answers = new double[4];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		for (int i = 0; i < 4; i++) {
			String name = st.nextToken();
			teams[i] = new Team(i, name, 0);
			map.put(name, 0);
		}

		for (int i = 0; i < 6; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			String t1 = st.nextToken();
			String t2 = st.nextToken();

			float w = Float.parseFloat(st.nextToken());
			float d = Float.parseFloat(st.nextToken());
			float l = Float.parseFloat(st.nextToken());

			float max = Math.max(w, Math.max(d, l));

			// 비기는 경우
			if ((max == w && max == l) || max == d) {
				map.put(t1, map.get(t1) + 1);
				map.put(t2, map.get(t2) + 1);
			}
			// t1 이 t2를 이기는 경우
			else if (max == w) {
				map.put(t1, map.get(t1) + 3);
			}
			// t2가 t1을 이기는 경우
			else {
				map.put(t2, map.get(t2) + 3);
			}
		}

		for (String name : map.keySet()) {
			for (int i = 0; i < 4; i++) {
				if (name.equals(teams[i].name)) {
					teams[i].score = map.get(name);
				}
			}
		}

		Arrays.sort(teams);
		int[] cnts = { 1, 0 };
		int idx = 0;
		int temp = teams[0].score;

		for (int i = 1; i < 4; i++) {
			if (temp != teams[i].score) {
				if (idx == 1) {
					break;
				}
				idx++;
				temp = teams[i].score;
			}

			cnts[idx]++;
		}

		// 전부 승점 같은 경우
		if (cnts[0] == 4) {
			System.out.printf("%.10f", 0.25);
			System.out.printf("%.10f", 0.25);
			System.out.printf("%.10f", 0.25);
			System.out.printf("%.10f", 0.25);
		}
		// 1등이 3팀인 경우
		else if (cnts[0] == 3) {
			int maxScore = teams[0].score;
			for (int i = 0; i < 4; i++) {
				if (teams[i].score == maxScore) {
					answers[teams[i].idx] = makePercentage(2 / 3);
				} else {
					answers[teams[i].idx] = makePercentage(0);
				}
			}
		}
		// 1등이 2팀인 경우
		else if (cnts[0] == 2) {
			int maxScore = teams[0].score;
			for (int i = 0; i < 4; i++) {
				if (teams[i].score == maxScore) {
					answers[teams[i].idx] = makePercentage(1);
				} else {
					answers[teams[i].idx] = makePercentage(0);
				}
			}
		}
		// 1등이 1팀이 경우
		else if (cnts[0] == 1) {			
			answers[teams[0].idx] = makePercentage(1);
			int maxScore = teams[1].score;
			int cnt = cnts[1];
			for (int i = 1; i < 4; i++) {
				if (teams[i].score == maxScore) {
					answers[teams[i].idx] = 1/ makePercentage(cnt);
				} else {
					answers[teams[i].idx] = makePercentage(0);
				}
			}
		}

		for (double ans : answers) {
			System.out.println(ans);
		}
	}

	static double makePercentage(double d) {
		double x = Math.pow(10, 6);
		return Math.round(d * x) / x;
	}
}
