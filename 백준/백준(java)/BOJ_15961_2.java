import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//회전 초밥
public class BOJ_15961 {
	static int N, d, k, c, ans;
	static int[] sushi;
	static int[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());

		sushi = new int[N];
		for (int i = 0; i < N; i++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}

		int[] cnt = new int[d + 1]; // 내가 먹은 초밥 카운트 기록 (초밥 번호 1~d번까지)
		cnt[c]++; // 쿠폰 초밥은 일단 먹고 시작

		int temp = 1; // 일단 쿠폰으로 한가지 초밥 먹음

		for (int i = 0; i < k; i++) { // 맨앞 k접시 먹어본 경우
			if (cnt[sushi[i]] == 0) { // 처음 먹는 초밥
				temp++;
			}
			cnt[sushi[i]]++; // 해당 번호 초밥 카운트++
		}

		for (int i = 1; i < N; i++) { // i접시부터 k개 시작임
			cnt[sushi[i - 1]]--; // 현재 시작접시 앞 접시의 초밥 카운트 빼기

			if (cnt[sushi[i - 1]] == 0) { // 앞 초밥은 이제 안먹어본 초밥
				temp--;
			}

			if (cnt[sushi[(i + k - 1) % N]] == 0) { // 처음먹어보는 초밥
				temp++;
			}
			cnt[sushi[(i + k - 1) % N]]++;
			ans = Math.max(ans, temp);
		}

		System.out.println(ans);
	}
}
