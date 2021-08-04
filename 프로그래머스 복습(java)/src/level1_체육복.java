import java.util.Arrays;

public class level1_체육복 {
    static class Solution {
        public int solution(int n, int[] lost, int[] reserve) {
            int answer = n - lost.length;
            Arrays.sort(lost);
            Arrays.sort(reserve);

            //여벌 체육복 가져온 학생이 도난당한 경우
            for (int i = 0; i < lost.length; i++) {
                for (int j = 0; j < reserve.length; j++) {
                    if (lost[i] == reserve[j]) {
                        answer++;
                        lost[i] = -1;
                        reserve[j] = -1;
                        break;
                    }
                }
            }
            //도난당한 학생에게 빌려주는 경우
            for (int i = 0; i < lost.length; i++) {
                for (int j = 0; j < reserve.length; j++) {
                    int left = lost[i] - 1;
                    int right = lost[i] + 1;
                    if (left == reserve[j] || right == reserve[j]) {
                        answer++;
                        reserve[j] = -1;
                        break;
                    }
                }
            }
            System.out.println(answer);
            return answer;


            //Better Code
//            int[] people = new int[n];
//            int answer = n;
//
//            for (int l : lost)
//                people[l-1]--;
//            for (int r : reserve)
//                people[r-1]++;
//
//            for (int i = 0; i < people.length; i++) {
//                if(people[i] == -1) {
//                    if(i-1>=0 && people[i-1] == 1) {
//                        people[i]++;
//                        people[i-1]--;
//                    }else if(i+1< people.length && people[i+1] == 1) {
//                        people[i]++;
//                        people[i+1]--;
//                    }else
//                        answer--;
//                }
//            }
//            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n1 = 5, n2 = 5, n3 = 3;
        int[] lost1 = {2, 3}, lost2 = {2, 4}, lost3 = {3};
        int[] reserve1 = {1, 3, 5}, reserve2 = {3}, reserve3 = {1};
        solution.solution(n1, lost1, reserve1);
        solution.solution(n2, lost2, reserve2);
        solution.solution(n3, lost3, reserve3);
    }
}
