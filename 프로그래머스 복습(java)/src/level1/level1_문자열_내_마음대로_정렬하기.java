package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class level1_문자열_내_마음대로_정렬하기 {
    static class Solution {
        public String[] solution(String[] strings, int n) {
            List<String> list = new ArrayList<>();
            for (int i = 0; i < strings.length; i++) {
                list.add(strings[i].charAt(n) + strings[i]);
            }
            Collections.sort(list);
            String[] answer = new String[list.size()];
            for (int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i).substring(1, list.get(i).length());
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] s1 = {"sun", "bed", "car"}, s2 = {"abce", "abcd", "cdx"};
        int n1 = 1, n2 = 2;
        System.out.println(Arrays.toString(solution.solution(s1, n1)));
        System.out.println(Arrays.toString(solution.solution(s2, n2)));
    }
}
