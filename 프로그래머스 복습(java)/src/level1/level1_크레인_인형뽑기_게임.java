package level1;

import java.util.Stack;

public class level1_크레인_인형뽑기_게임 {
    static class Solution {
        public boolean isPop(Stack<Integer> stack, int x, int answer) {
            if (stack.isEmpty() || stack.peek() != x) {
                stack.push(x);
                return false;
            } else {
                stack.pop();
                return true;
            }
        }

        public int solution(int[][] board, int[] moves) {
            int answer = 0;
            Stack<Integer> stack = new Stack<>();
            int size = board.length;
            for (int i = 0; i < moves.length; i++) {
                int pick = moves[i] - 1;
                for (int j = 0; j < size; j++) {
                    if (board[j][pick] != 0) {
                        if (isPop(stack, board[j][pick], answer)) {
                            answer += 2;
                        }
                        board[j][pick] = 0;
                        break;
                    }
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int board[][] = {{0, 0, 0, 0, 0}, {0, 0, 1, 0, 3}, {0, 2, 5, 0, 1}, {4, 2, 4, 4, 2}, {3, 5, 1, 3, 1}};
        int moves[] = {1, 5, 3, 5, 1, 2, 1, 4};
        System.out.println(solution.solution(board, moves));
    }
}
