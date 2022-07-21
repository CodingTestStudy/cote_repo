package practice;

import java.util.Scanner;

public class _3985 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int l = sc.nextInt();
		int n = sc.nextInt();
		
		//1번 ~ l번, 1번 ~ n번 
		//p번부터 k번까지 원함 
		int[]p = new int[n+1];
		int[]k = new int[n+1];
		
		int expectation = -1;
		int answer1 = 1;
		for(int i=1; i<=n; i++) {
			p[i] = sc.nextInt();
			k[i] = sc.nextInt();
			if(k[i] - p[i] > expectation) {
				expectation = k[i] - p[i];
				answer1 = i;				
			}
		}	
		System.out.println(answer1);
		int answer2 = 1;
		int[]answerArr = new int[n+1];
		int[] cake = new int[l + 1];
		for(int i=1; i<=n; i++) {
			int start = p[i];
			int end = k[i];
			for(int j=start; j<=end; j++) {
				if(cake[j] == 0) {
					cake[j] = i;
					answerArr[i] += 1;
				}
			}
		}
		
		int temp = -1;
		for(int i=1; i<=n; i++) {
			if(answerArr[i] > temp) {
				answer2 = i;
				temp = answerArr[i];
			}
		}
		
		System.out.println(answer2);
	}

}
