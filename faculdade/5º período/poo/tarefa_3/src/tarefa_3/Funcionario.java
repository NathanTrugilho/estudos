package tarefa_3;

public class Funcionario extends Pessoa {
	
	private final int matricula;
	private boolean disponivel;
	
	public Funcionario(int matricula, boolean disponivel, long cpf, String nome, long telefone, String email) {
		super(cpf, nome, telefone, email);
		this.matricula = matricula;
		this.disponivel = disponivel;
		
	}

	public boolean isDisponivel() {
		return disponivel;
	}

	public void setDisponivel(boolean disponivel) {
		this.disponivel = disponivel;
	}

	public int getMatricula() {
		return matricula;
	}

}
