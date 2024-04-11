package empresa;

import funcionarios.*;

public class Main {

	public static void main(String[] args) {

		Efetivado e1 = new Efetivado("Nathan Trugilho Braga", (short) 19, "159.835.397-79", (float) 8500.50);
		Estagiario i1 = new Estagiario("Serginho do pandeiro", (short) 25, "123.456.789-00", (float) 1500, "159.835.397-79", (short) 60);
		
		e1.estagiariosSupervisionados.add(i1);
		
		System.out.println(i1);
		System.out.println(e1);
		e1.getEstagiariosSupervisionados();
	}	
}
