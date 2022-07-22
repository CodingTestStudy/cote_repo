package practice;

import java.util.Scanner;

public class _1592 {
	static int n, m, l;
	static int throwBall(int start, int answer) {
		//시계 방향으로 l만큼 던짐
		if(answer % 2 == 1) {
			int target = start + l;
			//범위 안벗어남
			if(target <= n) {
				start = target;
			}
			//범위 벗어남
			else {
				start = target - n;
			}			
		}
		//반시계 방향으로 l만큼 던짐
		else {
			int target = start - l;
			//범위 안벗어남
			if(target >= 1) {
				start = target;
			}
			//범위 벗어남
			else {
				start = n + target;
			}
		}
		return start;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		l = sc.nextInt();
		int[] nums = new int[n+1];
		int maxCnt = 1;
		
		int answer = 0;
		int index = 1;
		nums[index] += 1;
		while(maxCnt != m) {
			index = throwBall(index, nums[index]);					
			nums[index] += 1;
			maxCnt = Math.max(maxCnt, nums[index]);
			answer += 1;
		}
		
		System.out.println(answer);
	}
}
