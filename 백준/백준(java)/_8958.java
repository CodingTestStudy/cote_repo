package practice;

import java.util.Scanner;

public class _8958 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int[] answer = new int[t];
		
		for(int i=0; i<t; i++) {
			String str = sc.next();
			int[] scores = new int[str.length()];
			
			if(str.charAt(0) == 'O') {
				scores[0] = 1;
			}
			for(int j=1; j<str.length(); j++) {
				if(str.charAt(j) == 'O') {
					scores[j] = scores[j-1] + 1;
				}
			}
			
			for(int j=0; j<str.length(); j++) {
				answer[i] += scores[j];
			}
		}
		
		for(int i=0; i<t; i++) {
			System.out.println(answer[i]);
		}

	}

}
