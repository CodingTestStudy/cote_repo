package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

// 캐슬 디펜스
public class BOJ_17135 {

	static class Archer {
		int r, c;

		Archer(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static class Enemy {
		int r, c;
		boolean life;

		Enemy(int r, int c, boolean life) {
			this.r = r;
			this.c = c;
			this.life = life;
		}
	}

	static int n, m, d, answer;
	static int[][] map;

	// 궁수 위치 조합에 필요한 자료들
	static int[] cards;
	static boolean[] selected;
	static ArrayList<int[]> list = new ArrayList<>();

	// 적 위치 저장 리스트
	static ArrayList<Enemy> enemyList = new ArrayList<>();

	static int[] dr = { -1, -1, -1 };
	static int[] dc = { -1, 0, 1 };

	static final int maxDist = 15 * 15;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		map = new int[n + 1][m];
		answer = -1;
		for (int r = 0; r < n; r++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int c = 0; c < m; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
				// 적 위치 리스트에 저장
				if (map[r][c] == 1) {
					enemyList.add(new Enemy(r, c, true));
				}
			}
		}

		cards = new int[m];
		selected = new boolean[m];
		for (int i = 0; i < m; i++) {
			cards[i] = i;
		}

		comb(0, 0);

		// 궁수 위치 조합
		for (int i = 0; i < list.size(); i++) {
			int[] temp = list.get(i);
			// 궁수 위치 조합별로 게임 시작 -> 처리 가능한 최대 적 수 리턴
			int result = playGame(temp, deepcopy(map));
			answer = Math.max(answer, result);
			saveLife(); // 죽은 적 life = true -> 새로운 궁수 조합에 대한 계산을 위해
		}
		System.out.println(answer);
	}

	static int playGame(int[] points, int[][] copy) {

		int archersR = n;
		int result = 0;

		// 궁수의 위치가 map을 벗어나지 않을 때까지 반복
		while (archersR >= 0) {

			// 죽은 적들을 저장하는 Set, 한번에 life=false 처리하기 위함
			// 동시에 공격당하는 적이 존재하기 때문
			Set<Enemy> deadList = new HashSet<>();
			for (int archerC : points) {
				// 임의의 적 생성(거리 비교하기 위해)
				Enemy target = new Enemy(maxDist, maxDist, true);
				for (Enemy enemy : enemyList) {
					// 이미 궁수를 지나친 적이면, 무시
					if (enemy.r >= archersR)
						continue;

					int dist = calcDistance(archersR, archerC, enemy.r, enemy.c); // 현재 적과 궁수와의 거리
					int targetDist = calcDistance(archersR, archerC, target.r, target.c); // 이전 적과 궁수와의 거리

					// 적이 살아있고, 적과의 거리가 d이하이며, 이전 적과의 거리 보다 작거나 같은 경우
					if (enemy.life && dist <= d && dist <= targetDist) {
						// 거리가 같으면, 왼쪽 적 처리
						if (dist == targetDist) {
							target = (target.c < enemy.c) ? target : enemy;
						} else {
							target = enemy;
						}
					}
				}

				// 적을 처리한 경우, 해당 적 저장
				if (target.r != maxDist) {
					deadList.add(target);
				}
			}

			// 처리 대상 적, 한번에 처리
			for (Enemy enemy : deadList) {
				enemy.life = false;
				result++;
			}

			// 궁수 한칸씩 이동
			archersR -= 1;

		}
		return result;
	}

	// 거리 계산
	static int calcDistance(int r1, int c1, int r2, int c2) {
		return Math.abs(r1 - r2) + Math.abs(c1 - c2);
	}

	// 모든 적 life 갱신
	static void saveLife() {
		for (int i = 0; i < enemyList.size(); i++) {
			enemyList.get(i).life = true;
		}
	}

	static void comb(int idx, int cnt) {
		if (cnt == 3) {
			int[] arr = new int[3];
			int x = 0;
			for (int i = 0; i < cards.length; i++) {
				if (selected[i]) {
					arr[x++] = cards[i];
				}
			}
			list.add(arr);
			return;
		}
		if (idx == m) {
			return;
		}

		selected[idx] = true;
		comb(idx + 1, cnt + 1);
		selected[idx] = false;
		comb(idx + 1, cnt);

	}

	static int[][] deepcopy(int[][] origin) {
		int[][] copy = new int[n][m];
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < m; c++) {
				copy[r][c] = origin[r][c];
			}
		}
		return copy;
	}
}
