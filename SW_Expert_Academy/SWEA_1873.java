package day0803;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//상호의 배틀필드
public class SWEA_1873 {
	static int h, w; // 높이, 너비
	static char[][] board; // 맵
	static int n; // 명령 문자열 길이
	static String order; // 명령 문자열
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static char[] dir = { '^', 'v', '<', '>' };
	static char[] move = { 'U', 'D', 'L', 'R' };
	static char flat = '.'; // 평지(전차 진입 가능)
	static char brick = '*'; // 벽돌(포탄에 부서짐)
	static char steel = '#'; // 강철(포탄에 부서지지 않음)
	static char water = '-'; // 물(전차 진입 불가능)

	// 범위 확인
	static boolean checkRange(int r, int c) {
		return (r >= 0) && (r < h) && (c >= 0) && (c < w);
	}

	// 탱크 방향 찾기
	static int[] findTank(int r, int c) {
		if (board[r][c] == '^' || board[r][c] == 'v' || board[r][c] == '<' || board[r][c] == '>') {
			for (int i = 0; i < 4; i++) {
				if (board[r][c] == dir[i]) {
					return new int[] { r, c, i };
				}
			}
		}

		return null;
	}

	// 좌표, 방향, 명령어
	static int[] act(int r, int c, int d, int s) {
		// 포탄 쏘는 경우
		if (s == 'S') {
			int cannonR = r;
			int cannonC = c;
			while (checkRange(cannonR + dr[d], cannonC + dc[d])) {
				cannonR += dr[d];
				cannonC += dc[d];
				// 벽돌 만난 경우
				if (board[cannonR][cannonC] == brick) {
					board[cannonR][cannonC] = flat;
					break;
				}

				// 강철 만난 경우
				if (board[cannonR][cannonC] == steel) {
					break;
				}
			}
		}
		// 방향 이동
		else {
			int nr, nc;
			for (int i = 0; i < 4; i++) {
				if (s == move[i]) {
					// 이동과 상관없이 방향 전환
					d = i;
					// 범위 확인
					if (checkRange(r + dr[i], c + dc[i])) {
						// 평지 확인
						if (board[r + dr[i]][c + dc[i]] == flat) {
							r += dr[i];
							c += dc[i];
						}

					}

					break;
				}
			}
		}
		return new int[] { r, c, d };
	}

	static void printState() {
		StringBuilder sb = new StringBuilder();
		for (int r = 0; r < h; r++) {
			for (int c = 0; c < w; c++) {
				sb.append(board[r][c]);
			}
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}

	public static void main(String[] args) throws IOException, NumberFormatException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			h = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			board = new char[h][w];

			int[] now = new int[3];
			for (int r = 0; r < h; r++) {
				String str = br.readLine();
				for (int c = 0; c < w; c++) {
					board[r][c] = str.charAt(c);
					int[] result = findTank(r, c);
					if (result != null) {
						now = result;
					}
				}
			}

			n = Integer.parseInt(br.readLine());
			order = br.readLine();

			int r = now[0];
			int c = now[1];
			int d = now[2];
			for (int i = 0; i < order.length(); i++) {
				char s = order.charAt(i);
				int temp[] = act(r, c, d, s);
				board[r][c] = flat;
				r = temp[0];
				c = temp[1];
				d = temp[2];
				board[r][c] = dir[d];
			}

			System.out.print("#" + tc + " ");
			printState();
		}
	}
}
