import java.io.*;
import java.util.*;


public class swea_idontknow {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int tc = Integer.parseInt(st.nextToken());
        int N ;
        int M ;
        String ans = "" ;
        for (int i=1; i<tc+1; i++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            for (int j=0; j<N; j++) {
                if ((1<<j & M) !=0) {
                    ans = "ON";
                }
                else {
                    ans = "OFF";
                    break;
                }
            }
            System.out.println("#"+i+" "+ ans);
        }
    }
}
