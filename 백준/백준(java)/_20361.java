package week3;

import java.util.Scanner;

public class _20361 {
	
	static int n, x, k;

	public static void main(String[] args) {
		// 일우는 야바위꾼
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		x = sc.nextInt();
		k = sc.nextInt();
		
		for(int i=0; i<k; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if(a == x) {
				x = b;
			}else if(b == x) {
				x = a;
			}
		}
		System.out.println(x);

	}

}
