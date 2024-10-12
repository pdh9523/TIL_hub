import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_17072 {

  static StringBuffer sb = new StringBuffer();
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    int tmp;
    for (int i=0; i<N; i++) {
      tmp = 0;
      st = new StringTokenizer(br.readLine());
      for (int j=0; j<M; j++) {
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        tmp = a * 2126 + b * 7152 + c * 722;
        if (510000 > tmp) {
          sb.append("#");
        } else if (1020000 > tmp) {
          sb.append("o");
        } else if (1530000 > tmp) {
          sb.append("+");
        } else if (2040000 > tmp) {
          sb.append("-");
        } else {
          sb.append(".");
        }
      }
      sb.append("\n");
    }
    System.out.println(sb);
  }

}
