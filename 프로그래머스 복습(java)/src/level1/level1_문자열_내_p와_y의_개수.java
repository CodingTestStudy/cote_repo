package level1;

import java.security.KeyStore;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class level1_문자열_내_p와_y의_개수 {
    static class Solution {
        boolean solution(String s) {
            s = s.toUpperCase(Locale.ROOT);
            String[] sp = s.split("");
            int p = 0, y = 0;
            for (String value : sp) {
                if (value.equals("P")) p++;
                if (value.equals("Y")) y++;
            }
            return p == y;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("pPoooyY"));
        System.out.println(solution.solution("Pyy"));
    }
}
