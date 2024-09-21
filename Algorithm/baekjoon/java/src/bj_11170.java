import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_11170 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            int cnt = 0;
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            for (int j=a; j<=b; j++) {
                String s = String.valueOf(j);
                for (int l=0; l<s.length(); l++) {
                    if (s.charAt(l) == '0') {
                        cnt ++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}
