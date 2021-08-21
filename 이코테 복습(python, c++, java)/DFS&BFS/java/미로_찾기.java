package javastudy.이코테.DFS_BFS;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


class Node{
    private int r;
    private int c;

    public Node(int r, int c) {
        this.r = r;
        this.c = c;
    }

    public int getR() {
        return this.r;
    }

    public int getC() {
        return this.c;
    }
}

public class 미로_찾기 {

    public static int n, m;
    public static int[][] graph = new int[201][201];

    public static int dr[] = {-1, 1, 0, 0};
    public static int dc[] = {0, 0, -1, 1};

    public static int bfs(int r, int c) {
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(r, c));

        while (!q.isEmpty()) {
            Node node = q.poll();
            r = node.getR();
            c = node.getC();

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nc >= 0 && nr < n && nc < m) {
                    if (graph[nr][nc] == 0) {
                        continue;
                    }
                    if (graph[nr][nc] == 1) {
                        graph[nr][nc] = graph[r][c] + 1;
                        q.offer(new Node(nr, nc));
                    }
                }
            }
        }
        return graph[n - 1][m - 1];
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
        System.out.println(bfs(0, 0));
    }
}
