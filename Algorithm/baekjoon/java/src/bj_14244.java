import java.io.*;
import java.util.*;

public class bj_14244 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int leaf=0, last=0;
        if (M==2) leaf=1;

        for (int i=1; i<N; i++) {
            if (M>leaf) {
                System.out.printf("0 %s%n",i);
                leaf ++;
            } else {
                System.out.printf("%s %s%n", last, i);
            }
            last = i;
        }
    }
}