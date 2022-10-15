import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//합이 0
public class BOJ_3151 {

	static int N, pCnt, nCnt;
	static long ans;
	static int[] arr, pArr, nArr;
	static int[] pVisited, nVisited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N];

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			arr[i] = num;

			if (num < 0) {
				nCnt++;
			} else
				pCnt++;
		}

		pArr = new int[pCnt + 1];
		nArr = new int[nCnt + 1];
		pVisited = new int[10001];
		nVisited = new int[10001];

		int pIdx = 0;
		int nIdx = 0;

		for (int i = 0; i < N; i++) {
			if (arr[i] < 0) {
				nArr[nIdx++] = arr[i];
				nVisited[Math.abs(arr[i])]++;
			} else {
				pArr[pIdx++] = arr[i];
				pVisited[arr[i]]++;
			}
		}

		// 양수2 음수1
		case1();
		// 양수1 음수2
		case2();

		System.out.println(ans);
	}

	// 양수2 음수1
	static void case1() {
		for (int i = 0; i < pCnt - 1; i++) {
			for (int j = i + 1; j < pCnt; j++) {
				int temp = pArr[i] + pArr[j];
				if (nVisited[temp] > 0) {
					ans += nVisited[temp];
				}
			}
		}
	}

	// 양수1 음수2
	static void case2() {
		for (int i = 0; i < nCnt - 1; i++) {
			for (int j = i + 1; j < nCnt - 1; j++) {
				int temp = nArr[i] + nArr[j];
				if (pVisited[Math.abs(temp)] > 0) {
					ans += pVisited[temp];
				}
			}
		}
	}
}
