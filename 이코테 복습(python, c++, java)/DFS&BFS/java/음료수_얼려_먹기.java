package javastudy.이코테.DFS_BFS;

import java.util.Scanner;

public class 음료수_얼려_먹기 {

    public static int n, m;
    public static int[][]graph = new int[1001][1001];

    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static boolean dfs(int r, int c) {
        if (r < 0 || c < 0 || r >= n || c >= m) {
            return false;
        }

        if (graph[r][c] == 0) {
            graph[r][c] = 1;
            for (int i = 0; i < 4; i++) {
                dfs(r + dr[i], c + dc[i]);
            }
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine(); //버퍼 지우기

        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = str.charAt(j) - '0';
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dfs(i, j)) {
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}
