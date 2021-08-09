package level1;

import java.util.*;

public class level1_문자열_내림차순으로_배치하기 {
    static class Solution {
        public String solution(String s) {
//            HashMap<Integer, Character> hashMap = new HashMap<>();
//            List<Integer> list = new ArrayList<>();
//            for (int i = 0; i < s.length(); i++) {
//                hashMap.put(s.charAt(i) - '0', s.charAt(i));
//                list.add(s.charAt(i) - '0');
//            }
//            list.sort(Comparator.reverseOrder());
//            StringBuilder answer = new StringBuilder();
//            for (int i = 0; i < s.length(); i++) {
//                answer.append(hashMap.get(list.get(i)));
//            }
//            return answer.toString();

            // More Simple and Better Code
            char[] sol = s.toCharArray();
            Arrays.sort(sol);
            return new StringBuilder(new String(sol)).reverse().toString();
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("Zbcdefg"));
    }
}
