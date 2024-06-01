package Dowhile;

import java.util.Scanner;

public class Dowhile {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int i = 0 ;
		do {
			System.out.println(i);
			i ++ ;
		} while (i<=10);
	}
}
