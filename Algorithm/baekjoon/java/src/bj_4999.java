import java.io.*;
import java.util.*;

public class bj_4999 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;
        // jh 재환
        st = new StringTokenizer(br.readLine());
        int jh = st.nextToken().length();

        // doctor 의사
        st = new StringTokenizer(br.readLine());
        int doctor = st.nextToken().length();

        // 길이 비교
        String ans ;
        if (jh<doctor) {
            ans = "no";
        } else {
            ans = "go";
        }
        // 출력
        System.out.println(ans);
    }
}
