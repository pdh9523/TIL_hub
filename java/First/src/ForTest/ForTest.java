package ForTest;

import java.util.*;

public class ForTest {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int j,i,a;
		a = sc.nextInt() ;
		int sum = 0 ;
		int ans = 0 ;
		for (i=0 ; i<=a ; i++) {
			sum += i;
			for (j=0 ; j<=a ; j++) {
				ans += sum;
			}
		}
		System.out.println(ans);
	}
}
