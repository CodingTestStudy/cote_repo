package day0804;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

// 카드2
public class BOJ_2164 {

	static Deque<Integer> change(Deque<Integer> q) {
		Deque<Integer> temp = new ArrayDeque<>();
		Object[] arr = q.toArray();

		// q내의 짝수번째 값만 저장
		for (int i = 1; i < q.size(); i += 2) {
			temp.add((Integer) arr[i]);
		}

		// q의 길이가 홀수였다면? -> 맨 위 카드 아래로 이동
		if (q.size() % 2 == 1) {
			int x = temp.pollFirst();
			temp.add(x);
		}
		return temp;
	}

	// 처음 초기화할 때, 짝수만 남음
	static Deque<Integer> init(int n) {
		Deque<Integer> temp = new ArrayDeque<>();
		for (int i = 0; i < n / 2; i++) {
			temp.add((i + 1) * 2);

		}

		// 카드가 홀수개였을 경우, 맨 위 카드 아래로 이동
		if (n % 2 == 1) {
			int x = temp.pollFirst();
			temp.add(x);
		}
		return temp;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		/**
		 * 1. 맨 위 카드 버리기 2. 제일 위 카드 -> 제일 아래로 이동
		 */
		if (n == 1) {
			System.out.println(1);
			return;
		}

		Deque<Integer> q;
		q = init(n);

		int answer = 0;
		while (true) {
			// 카드가 2장 이하로 남았을 때, 맨 아래 카드 확인
			if (q.size() <= 2) {
				answer = q.pollLast();
				break;
			}
			q = change(q);
		}

		System.out.println(answer);
	}

}
