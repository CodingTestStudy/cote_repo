package level1;

import java.util.*;

public class level1_카카오_인턴_키패드_누르기 {
    static class Solution {
        public String solution(int[] numbers, String hand) {
            String answer = "";
            HashMap<String, int[]> hashMap = new HashMap<>();
            hashMap.put("1", new int[]{0, 0});
            hashMap.put("2", new int[]{0, 1});
            hashMap.put("3", new int[]{0, 2});
            hashMap.put("4", new int[]{1, 0});
            hashMap.put("5", new int[]{1, 1});
            hashMap.put("6", new int[]{1, 2});
            hashMap.put("7", new int[]{2, 0});
            hashMap.put("8", new int[]{2, 1});
            hashMap.put("9", new int[]{2, 2});
            hashMap.put("*", new int[]{3, 0});
            hashMap.put("0", new int[]{3, 1});
            hashMap.put("#", new int[]{3, 2});

            Set<String> rightHand = new HashSet<>();
            Set<String> leftHand = new HashSet<>();

            leftHand.add("1");
            leftHand.add("4");
            leftHand.add("7");
            leftHand.add("*");

            rightHand.add("3");
            rightHand.add("6");
            rightHand.add("9");
            rightHand.add("#");

            String nowLeft = "*";
            String nowRight = "#";
            for (int number : numbers) {
                String s = String.valueOf(number);
                // 왼손으로 치는 경우
                if (leftHand.contains(s)) {
                    nowLeft = s;
                    answer += "L";
                }
                // 오른손으로 치는 경우
                else if (rightHand.contains(s)) {
                    nowRight = s;
                    answer += "R";
                }
                // 왼손, 오른손 가까운 위치 결정해야 하는 경우
                else {
                    int[] now = hashMap.get(s);
                    int[] left = hashMap.get(nowLeft);
                    int[] right = hashMap.get(nowRight);
                    String calc = calculate(now, left, right, hand);
                    answer += calc;
                    if (calc.equals("L")) {
                        nowLeft = s;
                    } else {
                        nowRight = s;
                    }
                }
            }
            return answer;
        }

        private String calculate(int[] now, int[] left, int[] right, String hand) {
            double l = Math.abs(now[0] - left[0]) + Math.abs(now[1] - left[1]);
            double r = Math.abs(now[0] - right[0]) + Math.abs(now[1] - right[1]);
            if (l < r) {
                return "L";
            } else if (l > r) {
                return "R";
            } else {
                return hand.substring(0, 1).toUpperCase();
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] numbers1 = {1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5};
        int[] numbers2 = {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2};
        int[] numbers3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        String hand1 = "right", hand2 = "left", hand3 = "right";
        System.out.println(solution.solution(numbers1, hand1));
        System.out.println(solution.solution(numbers2, hand2));
        System.out.println(solution.solution(numbers3, hand3));
    }
}
