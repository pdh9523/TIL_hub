import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_18679 {

    static StringBuffer sb = new StringBuffer();
    static HashMap<String, String> data = new HashMap<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            st.nextToken();
            String b = st.nextToken();
            data.put(a,b);
        }

        int M = Integer.parseInt(br.readLine());
        for (int i=0; i<M; i++) {
            int a = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());
            for (int j=0; j<a; j++) {
                String str = st.nextToken();
                sb.append(data.getOrDefault(str, str)).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
