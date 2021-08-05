import java.util.ArrayList;

public class level1_모의고사 {
    static class Solution {
        public int[] solution(int[] answers) {
            int[] student1 = {1, 2, 3, 4, 5};
            int[] student2 = {2, 1, 2, 3, 2, 4, 2, 5};
            int[] student3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
            int[] answer = {0, 0, 0};
            for (int i = 0; i < answers.length; i++) {
                if (student1[i % 5] == answers[i]) answer[0]++;

                if (student2[i % 8] == answers[i]) answer[1]++;

                if (student3[i % 10] == answers[i]) answer[2]++;
            }

            int max_value = Math.max(answer[0], Math.max(answer[1], answer[2]));
            ArrayList<Integer> list = new ArrayList<>();

            if (answer[0] == max_value) list.add(1);
            if (answer[1] == max_value) list.add(2);
            if (answer[2] == max_value) list.add(3);

            int[] result = new int[list.size()];
            for (int i = 0; i < result.length; i++) {
                result[i] = list.get(i);
            }

            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] answers1 = {1, 2, 3, 4, 5};
        int[] answers2 = {1, 3, 2, 4, 2};
        solution.solution(answers1);
        solution.solution(answers2);
    }
}
