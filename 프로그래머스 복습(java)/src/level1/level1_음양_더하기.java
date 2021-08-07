package level1;

public class level1_음양_더하기 {
    static class Solution {
        public int solution(int[] absolutes, boolean[] signs) {
            int answer = 0;
            for (int i = 0; i < absolutes.length; i++) {
                if (signs[i]) {
                    answer += absolutes[i];
                } else {
                    answer -= absolutes[i];
                }
            }
            System.out.println("answer = " + answer);
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] absolutes1 = {4, 7, 12}, absolutes2 = {1, 2, 3};
        boolean[] sign1 = {true, false, true}, sign2 = {false, false, true};
        solution.solution(absolutes1, sign1);
        solution.solution(absolutes2, sign2);
    }
}
