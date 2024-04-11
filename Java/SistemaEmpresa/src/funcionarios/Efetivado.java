package funcionarios;

import java.util.ArrayList;

public class Efetivado extends Funcionario {
	public ArrayList<Estagiario> estagiariosSupervisionados = new ArrayList<>();

	public Efetivado(String nome, short idade, String cpf, float salario) {
		super(nome, idade, cpf, salario);
	}

	public void getEstagiariosSupervisionados() {
		System.out.println("======= Supervisiona =======");
		for (Estagiario estag : estagiariosSupervisionados) {
			System.out.println(estag.getCpf());
		}
		System.out.println("============================");
	}

	@Override
	public String toString() {
		return "Efetivado: " + this.getNome() + "\nIdade: " + this.getIdade() + "\nCPF: " + this.getCpf()
				+ "\nSalario: " + this.getSalario() + " reais";
	}
}
