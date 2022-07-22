package practice;

import java.util.Scanner;

public class _2810 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String str = sc.next();
		//양쪽에 있으므로 0~n
		int[]holder = new int[n + 1];
		holder[0] = 1;
		holder[n] = 1;
		
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i) == 'S') {
				holder[i] = 1;
				holder[i+1] = 1;
			}else {
				holder[i+2] = 1;
				i += 1;				
			}
		}
		
		int answer = 0;
		for(int i=0; i<str.length(); i++) {
			if(holder[i] == 1) {
				answer += 1;
				holder[i] = 0;
			}else if(holder[i+1] == 1) {
				answer += 1;
				holder[i+1] = 0;
			}
		}
		
		System.out.println(answer);
	}

}
