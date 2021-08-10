package level1;

public class level1_서울에서_김서방_찾기 {
    static class Solution {
        public String solution(String[] seoul) {
            for (int i = 0; i < seoul.length; i++) {
                if (seoul[i].equals("Kim")) {
                    return "김서방은 " + i + "에 있다";
                }
            }
            return "";
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] seoul = {"Jane", "Kim"};
        System.out.println(solution.solution(seoul));
    }
}
