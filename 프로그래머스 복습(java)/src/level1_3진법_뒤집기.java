import java.util.ArrayList;

public class level1_3진법_뒤집기 {
    static class Solution {

        public int solution(int n) {
            int answer = 0;
            ArrayList<Integer> three = new ArrayList<>();
            while (n > 3) {
                int x = n % 3;
                n /= 3;
                three.add(x);
            }
            three.add(n);
            for (int i = 0; i < three.size(); i++) {
                answer += three.get(i) * Math.pow(3, (three.size() - 1 - i));
            }
            return answer;

            //Simple Code
//            String a = "";
//
//            while(n > 0){
//                a = (n % 3) + a;
//                n /= 3;
//            }
//            a = new StringBuilder(a).reverse().toString();
//
//
//            return Integer.parseInt(a,3);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n1 = 45, n2 = 125;
        System.out.println(solution.solution(n1));
        System.out.println(solution.solution(n2));
    }
}
