package triangulo;

public class Triangulo {

	int cateto_A;
	int cateto_B;
	int cateto_C;

	public int getCateto_A() {
		return cateto_A;
	}

	public void setCateto_A(int cateto_A) {
		this.cateto_A = cateto_A;
	}

	public int getCateto_B() {
		return cateto_B;
	}

	public void setCateto_B(int cateto_B) {
		this.cateto_B = cateto_B;
	}

	public int getCateto_C() {
		return cateto_C;
	}

	public void setCateto_C(int cateto_C) {
		this.cateto_C = cateto_C;
	}

	public void VerificaTriang(int cat_A, int cat_B, int cat_C) {
		if (cat_A < 0 || cat_B < 0 || cat_C < 0) {
			System.out.println("Dados inválidos!");
			return;
		}
		
		if (cat_A >= (cat_B + cat_C) || cat_B >= (cat_A + cat_C) || cat_C >= (cat_A + cat_B)) {
			System.out.println("O triângulo não existe!");
			return;
		}
		System.out.print("O triângulo existe e ");
		if ((cat_A == cat_B) && cat_B == cat_C) {
			System.out.println("é equilátero!");
			return;
		}
		if ((cat_A == cat_B) || cat_B == cat_C) {
			System.out.println("é isósceles!");
			return;
		}
		else {
			System.out.println("é escaleno!");
			return;
		}
	}
}
