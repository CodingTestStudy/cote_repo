package level1;

public class level1_1차_다트_게임 {

    static class Solution {
        int calculate1(int num, String s) {
            if (s.equals("S")) {
                return num;
            } else if (s.equals("D")) {
                return num * num;
            } else {
                return num * num * num;
            }
        }

        public int solution(String dartResult) {
            int[] answer = new int[3];
            int index = -1;
            for (int i = 0; i < dartResult.length(); i++) {
                char c = dartResult.charAt(i);
                if (Character.isDigit(c)) {
                    index++;
                    if (dartResult.charAt(i + 1) == '0') {
                        answer[index] = 10;
                        i++;
                    } else {
                        answer[index] = Character.getNumericValue(c);
                    }
                } else if (Character.isAlphabetic(c)) {
                    int num = calculate1(answer[index], String.valueOf(c));
                    if (i + 1 != dartResult.length() && (dartResult.charAt(i + 1) == '*' || dartResult.charAt(i + 1) == '#')) {
                        i++;
                        char c1 = dartResult.charAt(i);
                        if (c1 == '*') {
                            num *= 2;
                            if (index != 0) {
                                answer[index - 1] *= 2;
                            }
                        } else {
                            num *= -1;
                        }
                    }
                    answer[index] = num;
                }
            }
            int result = 0;
            for (int i : answer) {
                result += i;
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("1S2D*3T"));
        System.out.println(solution.solution("1D2S#10S"));
        System.out.println(solution.solution("1D2S0T"));
        System.out.println(solution.solution("1S*2T*3S"));
        System.out.println(solution.solution("1D#2S*3S"));
        System.out.println(solution.solution("1R2D3D#"));
        System.out.println(solution.solution("1D2S3T*"));
    }
}
