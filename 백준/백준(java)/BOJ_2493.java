package day0805;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

//탑
public class BOJ_2493 {

	static class Top {
		int idx, height;

		Top(int idx, int height) {
			this.idx = idx;
			this.height = height;
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		Stack<Top> stack = new Stack<>();

		int n = Integer.parseInt(br.readLine()); // 탑의 수
		st = new StringTokenizer(br.readLine(), " "); // 탑 높이 입력

		for (int i = 1; i <= n; i++) {
			int height = Integer.parseInt(st.nextToken());
			// 스택 빈 경우
			if (stack.isEmpty()) {
				sb.append(0).append(' ');
				stack.add(new Top(i, height)); // 현재 탑이 제일 높은 위치로 간주
				continue;
			}

			// i번째 탑과 수신할 적절한 탑 위치 찾을 때까지 반복
			while (true) {
				// stack이 빈 경우 == 수신할 top을 못 찾은 경우 -> 0, 현재 top 높이를 stack에 저장
				if (stack.isEmpty()) {
					sb.append(0).append(' ');
					stack.add(new Top(i, height));
					break;
				}

				Top top = stack.peek();
				// i번째 탑이 top의 높이보다 낮은 경우 -> top이 수신
				if (top.height > height) {
					sb.append(top.idx).append(' ');
					stack.add(new Top(i, height));
					break;
				}
				// i번째 탑이 top보다 높이보다 높은 경우 -> 다른 top과 비교해보기
				else {
					stack.pop();
				}
			}

		}
		System.out.println(sb.toString());

	}
}
