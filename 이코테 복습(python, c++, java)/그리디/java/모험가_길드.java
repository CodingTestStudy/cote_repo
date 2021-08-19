package javastudy.이코테.그리디;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 모험가_길드 {

    public static int n;
    public static ArrayList<Integer> arrayList = new ArrayList<>();


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            arrayList.add(sc.nextInt());
        }
        Collections.sort(arrayList);

        int total = 0;
        int group = 0;

        for (int i = 0; i < n; i++) {
            total += 1;
            if (total >= arrayList.get(i)) {
                group += 1;
                total = 0;
            }
        }
        System.out.println(group);
    }
}
