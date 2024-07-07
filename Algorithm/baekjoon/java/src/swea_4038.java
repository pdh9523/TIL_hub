import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_4038 {
    static int[] table ;

    static void KMP_table(String pattern) {
        int pidx = 0;
        for (int idx=1; idx<pattern.length(); idx++) {
            while (pidx>0 && pattern.charAt(idx) != pattern.charAt(pidx)) {
                pidx = table[pidx-1];
            }
            if (pattern.charAt(idx) == pattern.charAt(pidx)) {
                pidx ++;
                table[idx] = pidx;
            }
        }

    }

    static int KMP(String word, String pattern) {
        KMP_table(pattern);
        int cnt = 0;
        int pidx = 0;

        for (int idx=0; idx<word.length(); idx++) {
            while (pidx>0 && word.charAt(idx) != pattern.charAt(pidx)) {
                pidx = table[pidx-1];
            }

            if (word.charAt(idx) == pattern.charAt(pidx)) {
                if (pidx == pattern.length()-1) {
                    cnt ++;
                    pidx = table[pidx];
                } else {
                    pidx ++ ;
                }
            }
        }
        return cnt ;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // tc
        StringTokenizer st = new StringTokenizer(br.readLine());
        int TC = Integer.parseInt(st.nextToken());

        for (int tc=1; tc<=TC; tc++) {
            String a = new StringTokenizer(br.readLine()).nextToken();
            String b = new StringTokenizer(br.readLine()).nextToken();
            table = new int[a.length()];
            System.out.println("#"+tc+" "+KMP(a,b));
        }
    }
}
