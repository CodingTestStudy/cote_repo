package day0826;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

// 톱니바퀴(2)
public class BOJ_15662 {

	static int T, K;
	static ArrayList<Deque<Character>> wheels = new ArrayList<>();

	static class Status {
		int index, turn;

		Status(int index, int turn) {
			this.index = index;
			this.turn = turn;
		}
	}

	static Deque<Status> turnQ = new ArrayDeque<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			Deque<Character> q = new ArrayDeque<Character>();
			char[] cArr = br.readLine().toCharArray();
			for (char c : cArr) {
				q.add(c);
			}
			wheels.add(q);
		}

		K = Integer.parseInt(br.readLine());
		while (K-- != 0) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int index = Integer.parseInt(st.nextToken()) - 1;
			int turn = Integer.parseInt(st.nextToken());

			checkLeft(index, turn);
			checkRight(index, turn);
			if (turn == 1) {
				turnRight(wheels.get(index));
			} else {
				turnLeft(wheels.get(index));
			}

			while (!turnQ.isEmpty()) {
				Status status = turnQ.poll();
				if (status.turn == 1) {
					turnRight(wheels.get(status.index));
				} else {
					turnLeft(wheels.get(status.index));
				}
			}

		}
		System.out.println(calc());
	}

	static void checkLeft(int index, int turn) {
		Deque<Character> right = wheels.get(index);
		while (--index >= 0) {
			turn *= -1;
			Deque<Character> left = wheels.get(index);
			char r = (char) right.toArray()[6];
			char l = (char) left.toArray()[2];

			if (r == l) {
				return;
			}

			turnQ.add(new Status(index, turn));
			right = left;
		}
	}

	static void checkRight(int index, int turn) {
		Deque<Character> left = wheels.get(index);
		while (++index < T) {
			turn *= -1;
			Deque<Character> right = wheels.get(index);
			char l = (char) left.toArray()[2];
			char r = (char) right.toArray()[6];

			if (l == r) {
				return;
			}

			turnQ.add(new Status(index, turn));
			left = right;
		}
	}

	static void turnLeft(Deque<Character> q) {
		q.addLast(q.pollFirst());
	}

	static void turnRight(Deque<Character> q) {
		q.addFirst(q.pollLast());
	}

	static int calc() {
		int answer = 0;
		for (int i = 0; i < T; i++) {
			char c = (char) wheels.get(i).toArray()[0];
			if (c == '1') {
				answer++;
			}
		}
		return answer;
	}

	static void print() {
		for (int i = 0; i < T; i++) {
			System.out.println(wheels.get(i).toString());
		}
	}
}
