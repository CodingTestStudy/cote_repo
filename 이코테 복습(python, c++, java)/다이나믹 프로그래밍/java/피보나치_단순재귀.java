package javastudy.이코테.다이나믹프로그래밍;

public class 피보나치_단순재귀 {

    public static int fibo(int x){
        if (x == 1 || x == 2) {
            return 1;
        }
        return fibo(x - 1) + fibo(x - 2);
    }
    public static void main(String[] args) {
        System.out.println(fibo(4));
    }
}
