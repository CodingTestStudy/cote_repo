import java.util.Arrays;

public class level1_K번째수 {
    static class Solution {
        public int[] solution(int[] array, int[][] commands) {
            int[] answer = new int[commands.length];

            for (int i = 0; i < commands.length; i++) {
                // better method
                // int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);

                int[] temp = new int[commands[i][1] - commands[i][0] + 1];
                for (int j = 0; j < temp.length; j++) {
                    temp[j] = array[j + commands[i][0] - 1];
                }
                Arrays.sort(temp);
                answer[i] = temp[commands[i][2] - 1];
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
        System.out.println(solution.solution(array, commands));
    }
}
