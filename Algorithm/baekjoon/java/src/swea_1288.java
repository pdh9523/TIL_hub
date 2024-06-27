import java.io.*;
import java.util.*;

public class swea_1288 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int tc = Integer.parseInt(st.nextToken());
        int n ;
        for (int i=0; i<tc; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());

            int visit = 0;
            int cnt = 0;

            for (cnt=1; ; cnt++) {
                char[] arr = String.valueOf(n*cnt).toCharArray();
                for (char c : arr) {
                    int num = c - '0';
                    visit = visit | (1<<num);

                }
                if (visit == (1 << 10) -1) break ;
            }

            System.out.println("#" + i + " " + n*cnt);
        }
    }
}
