import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class swea_7701 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int tc=1; tc<=t; tc++) {
            TreeSet<String> data = new TreeSet<>(
                    Comparator.comparingInt(String::length)
                            .thenComparing(String::compareTo)
            );

            int N = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());

            for (int i=0; i<N; i++) {
                String d = new StringTokenizer(br.readLine()).nextToken();
                data.add(d);
            }

            System.out.println("#" + tc);

            for (String str : data) {
                System.out.println(str);
            }
        }
    }
}
