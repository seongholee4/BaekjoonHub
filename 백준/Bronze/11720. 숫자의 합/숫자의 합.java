import java.util.Scanner;

class Main {
    static Scanner sc;
    static int N;
    static String str;
    static int sum;

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        N = sc.nextInt();
        str = sc.next();
        sum = 0;
        
        for (int i = 0; i < N; i++) {
            sum += str.charAt(i) - '0';
        }
        System.out.println(sum);
    }
}