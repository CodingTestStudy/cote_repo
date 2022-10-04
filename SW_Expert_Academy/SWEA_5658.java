import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

// 보물상자 비밀번호
public class SWEA_5658 {

	static int TC, N, K, length;
	static long ans;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		TC = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= TC; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			length = N / 4;
			String str = br.readLine();
			char[] cArr = str.toCharArray();
			Set<Long> set = new HashSet<>();
			Set<String> checkSet = new HashSet<>();

			Deque<Character> q = new ArrayDeque<>();
			for (int i = 0; i < N; i++) {
				q.add(cArr[i]);
			}

			// 중복 발생 확인하기 위해 checkSet에 초기값 삽입
			for (int i = 0; i < N; i += length) {
				String temp = "";
				for (int j = i; j < i + length; j++) {
					temp += cArr[j];
				}
				checkSet.add(temp);
				set.add(Long.parseLong(temp, 16));
			}

			// q 갱신하면서 중복이 발생하기 전까지 반복, set에 16진수 변환값 삽입
			while (true) {
				q.addFirst(q.pollLast());
				for (int i = 0; i < N; i++) {
					cArr[i] = q.poll();
				}
				for (int i = 0; i < N; i++) {
					q.add(cArr[i]);
				}

				// 중복 발생 확인 변수
				boolean flag = true;
				int dupCnt = 0;

				for (int i = 0; i < N; i += length) {
					String temp = "";
					for (int j = i; j < i + length; j++) {
						temp += cArr[j];
					}

					// 중복 갯수 갱신
					if (checkSet.contains(temp)) {
						dupCnt++;
					}
					// 4변에서 모두 중복이 발생한 경우, 반복 종료
					if (dupCnt == 4) {
						flag = false;
						break;
					}

					long test = Long.parseLong(temp, 16);
					set.add(test);
				}

				// 4번 중복 발생시, 반복 종료
				if (!flag) {
					break;
				}

			}

			List<Long> list = new ArrayList<>();
			for (long x : set) {
				list.add(x);
			}

			Collections.sort(list, Collections.reverseOrder());

			ans = list.get(K - 1);

			sb.append("#" + tc + " " + ans + "\n");
		}
		System.out.println(sb.toString());
	}

}
