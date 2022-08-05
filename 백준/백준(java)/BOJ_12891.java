package day0805;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BOJ_12891 {

	static int s, p;
	static int a, c, g, t;
	static String dna;
	static HashMap<Character, Integer> needMap = new HashMap<>();
	static HashMap<Character, Integer> nowMap = new HashMap<>();

	static boolean check() {
		if (needMap.get('A') > nowMap.get('A')) {
			return false;
		}
		if (needMap.get('C') > nowMap.get('C')) {
			return false;
		}
		if (needMap.get('G') > nowMap.get('G')) {
			return false;
		}
		if (needMap.get('T') > nowMap.get('T')) {
			return false;
		}

		return true;
	}

	static void add(char c) {
		nowMap.put(c, nowMap.get(c) + 1);
	}

	static void remove(char c) {
		nowMap.put(c, (nowMap.get(c) == 0) ? 0 : nowMap.get(c) - 1);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int answer = 0;

		st = new StringTokenizer(br.readLine(), " ");
		s = Integer.parseInt(st.nextToken());
		p = Integer.parseInt(st.nextToken());
		dna = br.readLine();
		st = new StringTokenizer(br.readLine(), " ");
		a = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		g = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());
		needMap.put('A', a);
		needMap.put('C', c);
		needMap.put('G', g);
		needMap.put('T', t);
		nowMap.put('A', 0);
		nowMap.put('C', 0);
		nowMap.put('G', 0);
		nowMap.put('T', 0);

		for (int i = 0; i < p; i++) {
			add(dna.charAt(i));
		}

		if (check())
			answer++;

		// 슬라이딩 윈도우?
		for (int right = p; right < s; right++) {
			int left = right - p;
			add(dna.charAt(right));
			remove(dna.charAt(left));
			if (check())
				answer++;
		}

		System.out.println(answer);

	}
}
