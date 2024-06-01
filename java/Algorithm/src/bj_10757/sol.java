package bj_10757;

import java.math.BigInteger;
import java.util.Scanner;

public class sol {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		String a,b ;
		a = sc.next();
		b = sc.next();
		
		BigInteger A = new BigInteger(a);
		BigInteger B = new BigInteger(b);
		
		BigInteger sum = A.add(B);
		
		System.out.println(sum);
	}
}
