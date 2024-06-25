import java.io.*;
import java.util.*;

public class Main {
    private static Map<Integer, Integer> memo = new HashMap<>();
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        System.out.println(fibonacci(n));

    }
    static int fibonacci(int num) {
        if (num==0) return 0;
        if (num==1) return 1;
        if (memo.containsKey(num)) return memo.get(num);
        int result = fibonacci(num-1) + fibonacci(num-2);

        memo.put(num, result);
        return result;

    }
}
