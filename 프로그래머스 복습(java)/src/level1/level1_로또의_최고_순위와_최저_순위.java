package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class level1_로또의_최고_순위와_최저_순위 {
    static class Solution {
        public int[] solution(int[] lottos, int[] win_nums) {
            int[] answer = new int[2];
            int zero = 0;
            int matches = 0;
            List<Integer> list = new ArrayList<>();
            for (int lotto : lottos) {
                if (lotto == 0) {
                    zero++;
                } else {
                    list.add(lotto);
                }
            }
            for (int win_num : win_nums) {
                if (list.contains(win_num)) {
                    matches++;
                }
            }
            answer[0] = ranking(matches + zero);
            answer[1] = ranking(matches);

            return answer;

            //BETTER SIMPLE CODE
//            int[] answer = new int[2];
//            int cnt1 = 0;
//            int cnt2 = 0;
//            for(int i : lottos) {
//                if(i == 0) {
//                    cnt1++;
//                    continue;
//                }
//                for(int j : win_nums) {
//                    if(i == j) cnt2++;
//                }
//            }
//            answer[0] = getGrade(cnt1+cnt2);
//            answer[1] = getGrade(cnt2);
//            return answer;
        }

        private int ranking(int num) {
            return switch (num) {
                case 6 -> 1;
                case 5 -> 2;
                case 4 -> 3;
                case 3 -> 4;
                case 2 -> 5;
                default -> 6;
            };
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] l1 = {44, 1, 0, 0, 31, 25}, l2 = {0, 0, 0, 0, 0, 0}, l3 = {45, 4, 35, 20, 3, 9};
        int[] w1 = {31, 10, 45, 1, 6, 19}, w2 = {38, 19, 20, 40, 15, 25}, w3 = {20, 9, 3, 45, 4, 35};
        System.out.println(Arrays.toString(solution.solution(l1, w1)));
        System.out.println(Arrays.toString(solution.solution(l2, w2)));
        System.out.println(Arrays.toString(solution.solution(l3, w3)));
    }
}
