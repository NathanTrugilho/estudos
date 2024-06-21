package triangulo;

import java.util.Scanner;

public class Testa_triangulo {
	
	public static void main(String[] args) {
		
		System.out.println("Insira o valor dos 3 catetos: ");
		Scanner input = new Scanner(System.in);
		Triangulo t1 = new Triangulo();

		t1.cateto_A = input.nextInt();
		t1.cateto_B = input.nextInt();
		t1.cateto_C = input.nextInt();

		t1.VerificaTriang(t1.cateto_A, t1.cateto_B, t1.cateto_C);

		input.close();
	}
}