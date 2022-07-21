package practice;

import java.util.HashSet;
import java.util.Scanner;

public class _3052 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashSet<Integer> set = new HashSet<Integer>();
		int[] numArr = new int[10];
		for(int i=0; i<10; i++) {
			numArr[i] = sc.nextInt();
		}
		
		for(int i=0; i<10; i++) {
			int value = numArr[i] % 42;
			set.add(value);
		}
		
		System.out.println(set.size());
	}

}
