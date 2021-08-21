package javastudy.이코테.구현;

import java.util.Scanner;

public class 왕실의_나이트 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int r = str.charAt(1) - '0';
        int c = str.charAt(0) - 'a' + 1;

        int[] dr = {-2, -1, 1, 2, 2, 1, -1, -2};
        int[] dc = {-1, -2, -2, -1, 1, 2, 2, 1};

        int cnt = 0;
        for (int i = 0; i < 8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr < 1 || nc < 1 || nr > 8 || nc > 8) {
                continue;
            }
            cnt++;
        }
        System.out.println(cnt);
    }
}
