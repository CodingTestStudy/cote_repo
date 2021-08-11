package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class level1_1차_다트_게임 {

    static class Solution {
        int calculate(int num, String s) {
            if (s == "S") {
                return num;
            } else if (s == "D") {
                return num * num;
            } else {
                return num * num * num;
            }
        }

        public int solution(String dartResult) {
            String[] split = dartResult.split("[0-9]");
            char[] chars = dartResult.toCharArray();
            List<Integer> numList = new ArrayList<>();
            List<Integer> answer = new ArrayList<>();
            numList.add(0); // 의미없는 값
            for (char aChar : chars) {
                int data = (int) aChar - 48;
                if (data >= 0 && data < 10) {
                    numList.add(data);
                }
            }
            for (int i = 1; i < numList.size(); i++) {
                System.out.println(i + " 번째");
                if (split[i].length() == 1) {
                    numList.set(i, calculate(numList.get(i), split[i]));
                } else {
                    String s1 = split[i].substring(0, 1);
                    String s2 = split[i].substring(1, 2);
                    numList.set(i, calculate(numList.get(i), s1));
                    if (s2.equals("*")) {
                        if (i == 1) {
                            numList.set(i, numList.get(i) * 2);
                        } else {
                            numList.set(i - 1, numList.get(i - 1) * 2);
                            numList.set(i, numList.get(i) * 2);
                        }
                    } else {
                        numList.set(i, -numList.get(i));
                    }
                }
            }
            int result = 0;
            for (Integer num : numList) {
                System.out.println(num);
                result += num;
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("1S2D*3T"));
//        System.out.println(solution.solution("1D2S#10S"));
//        System.out.println(solution.solution("1D2S0T"));
//        System.out.println(solution.solution("1S*2T*3S"));
//        System.out.println(solution.solution("1D#2S*3S"));
//        System.out.println(solution.solution("1R2D3D#"));
//        System.out.println(solution.solution("1D2S3T*"));
    }
}
