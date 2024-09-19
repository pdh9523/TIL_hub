import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_1850 {

    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.parseLong(st.nextToken());
        long M = Long.parseLong(st.nextToken());

        long ans = gcd(N,M);

        for (long i=0; i<ans; i++) {
            sb.append("1");
        }
        System.out.println(sb);
    }

    private static long gcd(long a, long b) {
        while (a != b) {
            a = a%b;
            if (a==0) {
                return b;
            }

            if (b>a) {
                long tmp = a;
                a = b;
                b = tmp;
            }

        }

        return a;
    }
}
