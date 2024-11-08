import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj_11947 {

    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());

        for (int i=0; i<N; i++) {
            String s = br.readLine();

            StringBuilder tmp = new StringBuilder();
            for (int j=0; j < s.length(); j++) {
                tmp.append("9");
            }
            int a = Integer.parseInt(tmp.toString());
            int b = Integer.parseInt(s);

            sb.append(a*b).append("\n");
        }
        System.out.println(sb);
    }
}
