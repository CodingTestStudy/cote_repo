package practice;

import java.util.Arrays;
import java.util.Scanner;

public class _2798 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int answer = 0;
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[]cards = new int[n];
		for(int i=0; i<n; i++) {
			cards[i] = sc.nextInt();
		}		
		
		
		for(int i=0; i<n-2; i++) {
			for(int j=i+1; j<n-1; j++) {
				for(int k=j+1; k<n; k++) {
					int sum = cards[i] + cards[j] + cards[k];
					if(sum <= m && sum > answer) {
						answer = sum;
					}
				}
			}
		}
		System.out.println(answer);

	}

}
