package funcionarios;

public abstract class Funcionario {
	private String nome;
	private short idade;
	private String cpf;
	private float salario;

	public Funcionario(String nome, short idade, String cpf, float salario) {
		if (!verificaIdade(idade))
			return;
		this.nome = nome;
		this.cpf = cpf;
		this.salario = salario;
	}

	public String getNome() {
		return nome;
	}

	public short getIdade() {
		return idade;
	}

	private void setIdade(short idade) {
		this.idade = idade;
	}

	public String getCpf() {
		return cpf;
	}

	public float getSalario() {
		return salario;
	}

	public boolean verificaIdade(short idade) {
		if (idade < 18 || idade > 100) {
			System.out.println("Idade inválida!");
			return false;
		}
		setIdade(idade);
		return true;
	}
}
