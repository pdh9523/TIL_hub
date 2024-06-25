import java.io.*;
import java.util.*;

public class Main {
    static int white = 0;
    static int blue = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;

        // N : 배열의 크기
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        // arr : 색종이 배열
        int[][] arr = new int[N][N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dnc(arr,0,0,N);

        System.out.println(white);
        System.out.println(blue);
    }

    public static void dnc(int[][] arr, int x, int y, int n) {
        if (checkArr(arr,x,y,n)) {
            if (arr[x][y]==0) {
                white ++;
            } else {
                blue ++;
            }
            return;
        }
        int t = n/2;
        dnc(arr,x,y,t);
        dnc(arr,x,y+t,t);
        dnc(arr,x+t,y,t);
        dnc(arr,x+t,y+t,t);
    }

    public static boolean checkArr(int[][]arr,int x,int y,int n) {
        int col = arr[x][y];
        for (int i=x; i<x+n; i++) {
            for (int j=y; j<y+n; j++) {
                if (arr[i][j] != col) {
                    return false;
                }
            }
        }
        return true;
    }
}