package level1;

import java.util.Arrays;

public class level1_완주하지_못한_선수 {

    static class Solution {
        public String solution(String[] participant, String[] completion) {
            String answer = "";
            Arrays.sort(participant);
            Arrays.sort(completion);
            for (int i = 0; i < completion.length; i++) {
                if (!participant[i].equals(completion[i])) {
                    System.out.println(participant[i]);
                    return participant[i];
                }
            }
            System.out.println(participant[participant.length - 1]);
            return participant[participant.length - 1];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] p1 = {"leo", "kiki", "eden"}, c1 = {"eden", "kiki"};
        String[] p2 = {"marina", "josipa", "nikola", "vinko", "filipa"}, c2 = {"josipa", "filipa", "marina", "nikola"};
        String[] p3 = {"mislav", "stanko", "mislav", "ana"}, c3 = {"stanko", "ana", "mislav"};
        solution.solution(p1, c1);
        solution.solution(p2, c2);
        solution.solution(p3, c3);
    }
}
