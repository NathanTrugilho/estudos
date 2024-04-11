package funcionarios;

public class Estagiario extends Funcionario {
	private String cpfSupervisor;
	private short diasEstagio;

	public Estagiario(String nome, short idade, String cpf, float salario, String cpfSupervisor, short diasEstagio) {
		super(nome, idade, cpf, salario);
		this.cpfSupervisor = cpfSupervisor;
		this.diasEstagio = diasEstagio;
	}

	public String getCpfSupervisor() {
		return cpfSupervisor;
	}

	public short getDiasEstagio() {
		return diasEstagio;
	}

	@Override
	public String toString() {
		return "Estagiário: " + this.getNome() + "\nIdade: " + this.getIdade() + "\nCPF: " + this.getCpf()
				+ "\nSalario: " + this.getSalario() + " reais" + "\nSupervisor: " + getCpfSupervisor()
				+ "\nDias de Estágio: " + getDiasEstagio() + "\n";
	}
}
