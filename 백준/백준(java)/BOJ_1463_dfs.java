import java.util.Arrays;
import java.util.Scanner;

//1로 만들기
public class BOJ_1463_dfs {

	static int N, answer;
	static int[] arr;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N + 1];
		Arrays.fill(arr, Integer.MAX_VALUE);
		arr[N] = 0;

		answer = Integer.MAX_VALUE;
		dfs(N, 0);

		System.out.println(answer);
	}

	static void dfs(int target, int cnt) {

		if (target == 1) {
			answer = Math.min(answer, cnt);
			return;
		}

		if (target >= 3 && target % 3 == 0 && arr[target / 3] > arr[target] + 1) {
			arr[target / 3] = arr[target] + 1;
			dfs(target / 3, cnt + 1);
		}

		if (target >= 2 && target % 2 == 0 && arr[target / 2] > arr[target] + 1) {
			arr[target / 2] = arr[target] + 1;
			dfs(target / 2, cnt + 1);
		}

		if (arr[target - 1] > arr[target] + 1) {
			arr[target - 1] = arr[target] + 1;
			dfs(target - 1, cnt + 1);
		}
	}
}
