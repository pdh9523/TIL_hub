import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int[][] dr = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        boolean[][] visit = new boolean[m][n];

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (picture[i][j] !=0 && !visit[i][j]) {
                    int target = picture[i][j];
                    Queue<int[]> q = new LinkedList<>();
                    q.offer(new int[]{i,j});
                    visit[i][j] = true;
                    int cnt = 1;

                    while (!q.isEmpty()) {
                        int[] cur = q.poll();

                        int x = cur[0];
                        int y = cur[1];

                        for (int[] d : dr) {
                            int di = x + d[0];
                            int dj = y + d[1];
                            if ( 0<= di && di <m && 0<=dj && dj<n && !visit[di][dj] && picture[di][dj] == target) {
                                cnt ++;
                                visit[di][dj] = true;
                                q.offer(new int[]{di,dj});
                            }
                        }
                    }
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea,cnt);
                    numberOfArea ++ ;
                }
            }
        }


        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}