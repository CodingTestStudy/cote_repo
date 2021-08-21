package javastudy.이코테.구현;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 문자열_재정렬 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        ArrayList<Character> result = new ArrayList<Character>();
        int num = 0;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (Character.isAlphabetic(c)) {
                result.add(c);
            } else {
                num += c - '0';
            }
        }
        Collections.sort(result);

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
        }

        if (num != 0) {
            System.out.print(num);
        }
        System.out.println();
    }
}
